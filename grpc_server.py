from concurrent import futures
import grpc
import anonymize_pb2
import anonymize_pb2_grpc
import logging
import time
import pickle

from settings import LOGGING_FORMAT

class Listener(anonymize_pb2_grpc.AnonymizeServiceServicer):

    def __init__(self, pickle_filepath:str):
        self.loaded_data = {}
        self.pickle_filepath = pickle_filepath

        # Loading data from persisted anonymization mapping (pickle):
        self.load_data()


    def getAnonymizedID(self, request, context):
        logging.info(f"Received nickname = {request.nickname}")

        logging.info("Checking if nickname is not in currently defined {nickname: ID} mapping.")
        player_counter = 0
        if request.nickname not in self.loaded_data:
            logging.info("Nickname not within current mapping object.")
            self.loaded_data[request.nickname] = player_counter
            player_counter += 1
        else:
            logging.info("Nickname is within current mapping. Reusing existing anonymized ID.")

        anonymized_player = self.loaded_data[request.nickname]

        # Add the nickname as the key and check for highest current value of generated ID and add new key/value pair with highest_id += 1
        logging.info(f"Mapped nickname = {request.nickname} to ID = {anonymized_player}")
        return anonymize_pb2.ReceiveID(anonymizedID=anonymized_player)


    def load_data(self):
        """
        Used to check if .pickle file was created for anonymizing player nicknames.
        If .pickle file exists it opens it and loads the information into memory,
        If it doesn't it returns empty dictionary to be populated with {"nickname": ID} mapping.
        """

        try:
            with open(self.pickle_filepath, mode="rb") as anonymized_db:
                # If there's already a dict within the file, return it
                logging.info("Attempting to load supplied DB of anonymized players.")
                self.loaded_data = pickle.load(anonymized_db)
                logging.info("Loaded existing database of {nickname: ID} mappings.")
                logging.info(f"Detected {len(self.loaded_data)} nicknames that were hashed.")
        except:
            logging.info("Did not detect any objects in .pickle for anonymizing nicknames.")
            self.loaded_data = {}


    def save_data(self):
        """
        Used before server shutdown to write all of the {"nickname": "ID"} mappings to a pickle file.
        """

        logging.info("Entered save_data()")

        with open(self.pickle_filepath, mode="wb") as anonymized_db:
            logging.info(f"Opened {self.pickle_filepath} as anonymized_db.")

            logging.info("Attempting to dump all of recently mapped nicknames into a pickle file and save it.")
            logging.info(f"Currently detected {len(self.loaded_data)} hashed nicknames.")

            pickle.dump(self.loaded_data, anonymized_db)

            logging.info("Successfully performed pickle.dump().")


def serve():

    logging.info("Attempting to initialize grpc server.")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))

    # Initializing empty Listener:
    logging.info("Initializing Listener() class with a file to keep hashed nicknames.")
    my_listener = Listener("./persist_anonymized_players.pickle")

    # Loading pickle data which will be contained within class object:
    logging.info("Calling .load_data() on initialized Listener to check if file used for hashing exists.")
    my_listener.load_data()

    # Starting server:
    logging.info("Adding Service to server.")
    anonymize_pb2_grpc.add_AnonymizeServiceServicer_to_server(my_listener, server)

    insecure_port = "[::]:9999"
    logging.info(f"calling server.add_insecure_port({insecure_port}).")
    server.add_insecure_port(insecure_port)
    logging.info("Starting server by calling server.start().")
    server.start()

    # Logging server status:
    try:
        while True:
            logging.info("Server listening")
            time.sleep(10)

    except KeyboardInterrupt:
        logging.info("Detected KeyboardInterrupt, Stopping server.")

        logging.info("Calling .save_data() on Listener().")
        my_listener.save_data()
        server.stop(grace=10)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT)
    logging.info("Set up logging config, attempting to call serve().")
    serve()