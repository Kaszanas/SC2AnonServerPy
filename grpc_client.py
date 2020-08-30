import os
import logging

# gRPC imports:
import grpc
import anonymize_pb2
import anonymize_pb2_grpc

# Replay processing imports:
import sc2reader
from PACAnalyzer.pacanalyzer import PACAnalyzer
import pickle

# Own imports:
from settings import LOGGING_FORMAT

sc2reader.engine.register_plugin(PACAnalyzer())

CONNECTION = None

def initialize_worker():

    global CONNECTION

    logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT)

    # Creating connection once per batch of replay files:
    CONNECTION = grpc.insecure_channel("localhost:9999")

    logging.info("Initialized Worker")


def anonymize_nicknames(replay, stub):

    logging.info("Entered anonymize nicknames")

    logging.info("Starting to iterate over players and anonymizing their nicknames")
    for key, client in replay.client.items():

        # Calling the server to see if the nicknames were already assigned with arbitrary anonymized ID:
        response = stub.getAnonymizedID(anonymize_pb2.SendNickname(nickname=client.name))

        # Overwriting  existing values:
        client.name = response.anonymizedID
    logging.info("Finished anonymizing nicknames")

    return replay


def anonymize(replay, stub):

    logging.info("Entered anonymize")

    # Anonymizing known sensitive variables by hand (there should always be 2 players in 1v1 ranked play)
    logging.info("Starting to iterate over players, anonymizing toon_handle and toon_id")
    for key, client in replay.client.items():
        client.toon_handle = 'redacted'
        client.toon_id = 'redacted'
    logging.info("Finished anonymizing toon_handle and toon_id")

    # Calling anonymize nicknames to check if they were processed before:
    logging.info("Calling anonymize_nicknames()")
    replay = anonymize_nicknames(replay, stub)
    logging.info("Exited anonymize_nicknames, returning replay object")

    replay = anonymize_chat(replay)

    return replay

def anonymize_chat(replay):

    events = [not_chat for not_chat in replay.events if not not_chat.name == "ChatEvent"]
    replay.events = events

    return replay


def process_replay(arguments:tuple):

    logging.info(f"Entered process_replay got arguments = {arguments}")

    try:

        # Unpacking tuple of supplied arguments (this is required with multiprocessing)
        replay_file, output_dir = arguments

        # Opening communication with gRPC
        logging.info("Initializing gRPC stub")
        stub = anonymize_pb2_grpc.AnonymizeServiceStub(CONNECTION)

        # Loading the file
        logging.info("Loading replay")
        replay = sc2reader.load_replay(replay_file, load_level=4)

        # Getting filename of the provided replay
        logging.info("Checking replay filename")
        name_of_replay = os.path.splitext(os.path.basename(replay.filename))[0]

        logging.info("Calling anonymize()")
        replay = anonymize(replay, stub)

        with open(f'{output_dir + name_of_replay}.pickle', 'wb') as f:
            pickle.dump(replay, f)

    except:
        logging.exception("Exception detected")