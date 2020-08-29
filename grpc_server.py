from concurrent import futures
import grpc
import anonymize_pb2
import anonymize_pb2_grpc
import logging
import time
import pickle
import hashlib


class Listener(anonymize_pb2_grpc.AnonymizeServiceServicer):

    def __init__(self, pickle_filepath:str):
        self.loaded_data = {}
        self.pickle_filepath = pickle_filepath

        self.load_data()


    def getAnonymizedID(self, request, context):
        logging.info(f"Received nickname = {request.nickname}")

        # TODO: use self.loaded data as the object to chech and hash the players
        if request.nickname not in self.loaded_data:
            self.loaded_data[request.nickname] = hashlib.md5(request.nickname.encode()).hexdigest()

        hashed_player = self.loaded_data[request.nickname]

        # Add the nickname as the key and check for highest current value of generated ID and add new key/value pair with highest_id += 1
        logging.info(f"Mapped nickname = {request.nickname} to ID = {hashed_player}")
        return anonymize_pb2.ReceiveID(anonymizedID=hashed_player)


    def load_data(self):
        """
        Used to check if .pickle file was created for anonymizing player nicknames.
        If .pickle file exists it opens it and loads the information into memory,
        If it doesn't it returns empty dictionary to be populated with {"nickname": ID} mapping.
        """

        try:
            with open(self.pickle_filepath, mode="rb") as anonymized_db:
                # If there's already a dict there return it
                self.loaded_data = pickle.load(anonymized_db)
                # TODO: How much objects in object

        except:
            # TODO: Couldn't find objects
            self.loaded_data = {}



    def save_data(self):
        """
        Used before server shutdown to write all of the {"nickname": ID} mappings to a pickle file.
        """

        with open(self.pickle_filepath, mode="wb") as anonymized_db:
            pickle.dump(self.loaded_data, anonymized_db)

            # TODO: Get number of currently saved objects


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))

    # Initializing empty Listener:
    my_listener = Listener("./test_anonymized_players.pickle")
    # Loading pickle data which will be contained within class object:
    my_listener.load_data()

    # Starting server:
    anonymize_pb2_grpc.add_AnonymizeServiceServicer_to_server(my_listener, server)
    server.add_insecure_port("[::]:9999")
    server.start()

    # Logging server status:
    try:
        while True:
            logging.info("Server listening")
            time.sleep(10)

    except KeyboardInterrupt:
        logging.info("Detected KeyboardInterrupt, Stopping server")
        my_listener.save_data()
        server.stop(grace=10)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    serve()