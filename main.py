from client import process_replay, anonymize, anonymize_nicknames
from multiprocessing import Pool
import argparse
import os
import logging
from itertools import product

# Initiate multiprocessing spawning processes that are using load_replay
# This must be done by popping a list so that processes don't have the same replay by accident.

def get_replays(replay_directory:str):

    absolute_filepaths = []
    for replay in os.listdir(replay_directory):
        if replay.endswith(".SC2Replay"):
            absolute_filepaths.append(os.path.abspath(replay))

    return absolute_filepaths


def start_processing(replay_directory:str, output_directory:str):

    list_of_replays = get_replays(replay_directory)

    # process_jobs = []
    # while process_jobs < 24:
    #     while list_of_replays:
    #         p = mp.Process(target=process_replays, args=(list_of_replays.pop(),))

    agents = 23
    chunksize = 20
    with Pool(processes=agents) as pool:
        replay = list_of_replays.pop()
        pool.map(process_replay, product(replay, output_directory), chunksize)
