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
    # Listing the files available in a supplied directory, checking for the right extension and obtaining absolute path:
    for replay in os.listdir(replay_directory):
        if replay.endswith(".SC2Replay"):
            absolute_filepaths.append(os.path.abspath(replay))

    return absolute_filepaths


def start_processing(replay_directory:str, output_directory:str):

    # Getting a list of replay filepaths by using a helper function:
    list_of_replays = get_replays(replay_directory)

    # Defining available pool of processes for replay processing:
    agents = 24
    chunksize = 1000
    with Pool(processes=agents) as pool:
        replay = list_of_replays.pop()
        pool.map(process_replay, product(list_of_replays, output_directory), chunksize)
