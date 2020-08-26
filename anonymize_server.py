from concurrent import futures
import grpc
import anonymize_pb2
import anonymize_pb2_grpc
import logging
import time


class Listener(anonymize_pb2_grpc.AnonymizeServiceServicer):

    def SendNickname(self, request, context):
        logging.info(f"Received nickname = {request.nickname}")

        # TODO: Check if the nickname is currently in a saved .pickle file

        # If the nickname is not in the file add it

        # Add the nickname as the key and check for highest current value of generated ID and add new key/value pair with highest_id += 1
        logging.info(f"Mapped nickname = {request.nickname} to ID = {}")
        return anonymize_pb2.ReceiveID(anonymized_id=1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    anonymize_pb2_grpc.add_AnonymizeServiceServicer_to_server(Listener(), server)
    server.add_insecure_port()
    server.start()

    try:
        while True:
            logging.info("Server listening")
            time.sleep(10)

    except KeyboardInterrupt:
        logging.info("Detected KeyboardInterrupt, Stopping server")
        server.stop()


if __name__ == "__main__":
    serve()