import os
import logging

# gRPC imports:
import grpc

import sc2anonserverpy.grpc_functions.anonymize_pb2 as anonymize_pb2
import sc2anonserverpy.grpc_functions.anonymize_pb2_grpc as anonymize_pb2_grpc

# Replay processing imports:
import sc2reader
import pickle

# Own imports:
from sc2anonserverpy.settings import LOGGING_FORMAT

CONNECTION = None


def initialize_worker():
    global CONNECTION

    logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT)

    # Creating connection once per batch of replay files:
    CONNECTION = grpc.insecure_channel("localhost:9999")

    logging.info("Initialized Worker")


def anonymize_toon_fn(replay, stub):
    logging.info("Entered anonymize_toon()")

    logging.info("Starting to iterate over players and anonymizing their toons")
    for _, client in replay.client.items():
        # Calling the server to see if the nicknames were already assigned with arbitrary anonymized ID:
        response = stub.getAnonymizedID(
            anonymize_pb2.SendNickname(nickname=client.toon_handle)
        )
        # Overwriting  existing values:
        client.toon_handle = response.anonymizedID

    logging.info("Finished anonymizing client.toon_handle")
    return replay


def anonymize(replay, stub, anonymize_toon_bool: bool, anonymize_chat_bool: bool):
    logging.info("Entered anonymize()")

    # Anonymizing known sensitive variables by hand (there should always be 2 players in 1v1 ranked play):
    if anonymize_toon_bool:
        logging.info(
            "Starting to iterate over players, anonymizing nickname and toon_id"
        )
        for _, client in replay.client.items():
            # Anonymizing nickname:
            client.name = "redacted"
            # Anonymizing toon_id:
            client.toon_id = "redacted"

        # Calling anonymize nicknames to check if they were processed before:
        logging.info("Calling anonymize_nicknames()")
        replay = anonymize_toon_fn(replay, stub)
        logging.info("Exited anonymize_nicknames, returning replay object")

    if anonymize_chat_bool:
        replay = anonymize_chat(replay)

    return replay


def anonymize_chat(replay):
    for message_object in replay.messages:
        if message_object.name == "ChatEvent":
            message_object.text = "redacted"

    return replay


def process_replay(arguments: tuple):
    logging.info("Entered process_replay()")

    replay_file, output_dir, anonymize_toon, anonymize_chat = arguments

    logging.info("Unpacked arguments")

    try:
        # Opening communication with gRPC:
        stub = None
        if anonymize_toon:
            logging.info("Detected anonymize_toon = True, Initializing gRPC stub")
            stub = anonymize_pb2_grpc.AnonymizeServiceStub(CONNECTION)

        # Loading the file:
        logging.info("Loading replay")
        replay = sc2reader.load_replay(replay_file, load_level=4)

        # Getting filename of the provided replay:
        logging.info("Checking replay filename.")
        name_of_replay = os.path.splitext(os.path.basename(replay.filename))[0]

        # Anonymizing the file:
        logging.info("Calling anonymize().")
        replay = anonymize(
            replay=replay,
            stub=stub,
            anonymize_toon_bool=anonymize_toon,
            anonymize_chat_bool=anonymize_chat,
        )
        logging.info("Exited anonymize().")

        with open(f"{output_dir + name_of_replay}.pickle", "wb") as f:
            logging.info("Attempting to create .pickle file.")
            pickle.dump(replay, f)
            logging.info("Created .pickle file with the result of processing.")

    except:  # noqa E722
        logging.exception("Exception detected")
