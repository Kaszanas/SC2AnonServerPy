import os

# gRPC imports:
import grpc
import anonymize_pb2
import anonymize_pb2_grpc

# Replay processing imports:
import sc2reader
from PACAnalyzer.pacanalyzer import PACAnalyzer
import pickle

sc2reader.engine.register_plugin(PACAnalyzer())

def anonymize_nicknames(replay):

    # Selecting nicknames from supplied replay:
    nicknames = [replay.client[0].name, replay.client[1].name]

    # Opening communication with gRPC
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = anonymize_pb2_grpc.AnonymizeServiceStub(channel)

        for index, nickname in enumerate(nicknames):
            # Calling the server to see if the nicknames were already assigned with arbitrary anonymized ID:
            response = stub.getAnonymizedID(anonymize_pb2.SendNickname(nickname=nickname))

            # Overwriting  existing values:
            replay.client[index].name = response

    return replay


def anonymize(replay):

    # Calling anonymize nicknames to check if they were processed before:
    replay = anonymize_nicknames(replay)

    # Anonymizing known sensitive variables by hand (there should always be 2 players in 1v1 ranked play)
    for index in range(2)
        replay.client[index].toon_handle = 'redacted'
        replay.client[index].toon_id = 'redacted'
        replay.client[index].url = 'redacted'

    return replay


def process_replay(replay_file:str, output_dir:str):
    # Loading the file
    replay = sc2reader.load_replay(f'{replay_file}', load_level=4)

    # Getting filename of the provided replay
    name_of_replay = os.path.splitext(os.path.basename(replay.filename))[0]
    replay = anonymize(replay)
    with open(f'{output_dir + name_of_replay}.pickle', 'wb') as f:
        pickle.dump(replay, f)