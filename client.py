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
    nicknames = [replay.client[0], replay.client[1]] # TODO: Fix this line for the exact object

    with grpc.insecure_channel("localhost:9999") as channel:
        stub = anonymize_pb2_grpc.AnonymizeServiceStub(channel)

        for index, nickname in enumerate(nicknames):
            response = stub.getAnonymizedID(anonymize_pb2.SendNickname(nickname=nickname))
            replay.client[index] = response # TODO: Fix this line for the exact object

    return replay


def anonymize(replay):
    # Delete player
    replay = anonymize_nicknames(replay)
    replay.client[0].toon_handle = 'redacted'
    replay.client[0].toon_id = 'redacted'
    replay.client[0].url = 'redacted'

    return replay


def process_replays(replay_file:str, output_dir:str):
    replay = sc2reader.load_replay(f'{replay_file}', load_level=4)

    name_of_replay = os.path.splitext(os.path.basename(replay.filename))[0]
    replay = anonymize(replay)
    with open(f'{output_dir + name_of_replay}.pickle', 'wb') as f:
        pickle.dump(anonymize(replay), f)