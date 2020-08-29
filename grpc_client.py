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

sc2reader.engine.register_plugin(PACAnalyzer())

CONNECTION = None

def initialize_worker():

    global CONNECTION

    # TODO: Comment
    logging.basicConfig(level=logging.DEBUG)
    # TODO: Comment
    CONNECTION = grpc.insecure_channel("localhost:9999")

    logging.info("Initialized Worker")


def anonymize_nicknames(replay, stub):

    for key, client in replay.client.items():

        # Calling the server to see if the nicknames were already assigned with arbitrary anonymized ID:
        response = stub.getAnonymizedID(anonymize_pb2.SendNickname(nickname=client.name))

        # Overwriting  existing values:
        client.name = response.anonymizedID


    return replay


def anonymize(replay, stub):

    # Anonymizing known sensitive variables by hand (there should always be 2 players in 1v1 ranked play)
    # TODO: for all clients
    for key, client in replay.client.items():
        client.toon_handle = 'redacted'
        client.toon_id = 'redacted'

    # Calling anonymize nicknames to check if they were processed before:
    replay = anonymize_nicknames(replay, stub)


    return replay

def process_replay(arguments:tuple):

    logging.info(f"Entered process_replay got arguments = {arguments}")

    try:

        replay_file, output_dir = arguments

        # Opening communication with gRPC
        stub = anonymize_pb2_grpc.AnonymizeServiceStub(CONNECTION)

        # Loading the file
        replay = sc2reader.load_replay(replay_file, load_level=4)

        # Getting filename of the provided replay
        name_of_replay = os.path.splitext(os.path.basename(replay.filename))[0]
        replay = anonymize(replay, stub)
        with open(f'{output_dir + name_of_replay}.pickle', 'wb') as f:
            pickle.dump(replay, f)

    except:
        logging.exception("Got exception")