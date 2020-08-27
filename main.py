from client import process_replays, anonymize, anonymize_nicknames
import multiprocessing as mp
import argparse
import os

# Initiate multiprocessing spawning processes that are using load_replay
# This must be done by popping a list so that processes don't have the same replay by accident.

def get_replays(replay_directory:str):

    absolute_filepaths = []
    for replay in os.listdir(replay_directory):
        if replay.endswith(".SC2Replay"):
            absolute_filepaths.append(os.path.abspath(replay))

    return absolute_filepaths


def start_processing(replay_directory:str):

    list_of_replays = get_replays(replay_directory)

    process_jobs = []
    while process_jobs < 24:
        while list_of_replays:
            p = mp.Process(target=process_replays, args=(list_of_replays.pop(),))
