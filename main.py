from grpc_sc2reader_client import process_replay, anonymize, anonymize_nicknames, initialize_worker
from multiprocessing import Pool
import argparse
import os
import logging
from itertools import product


USE_MULTIPROCESSING = True

# Initiate multiprocessing spawning processes that are using load_replay
# This must be done by popping a list so that processes don't have the same replay by accident.
def get_replays(replay_directory:str):

    absolute_filepaths = []
    # Listing the files available in a supplied directory, checking for the right extension and obtaining absolute path:
    for replay in os.listdir(replay_directory):
        if replay.endswith(".SC2Replay"):
            absolute_filepaths.append(os.path.abspath(os.path.join(replay_directory, replay)))

    return absolute_filepaths


def start_processing(replay_directory:str, output_directory:str):

    # Getting a list of replay filepaths by using a helper function:
    list_of_replays = get_replays(replay_directory)
    logging.info(f"Got list_of_replays= {len(list_of_replays)}")

    processing_arguments = product(list_of_replays, [output_directory])

    if USE_MULTIPROCESSING:


        # Defining available pool of processes for replay processing:
        agents = 44
        chunksize = 1000
        with Pool(processes=agents, initializer=initialize_worker) as pool:
            # test_var = list(product(list_of_replays, [output_directory]))
            pool.imap_unordered(process_replay, processing_arguments, chunksize)

            pool.close()
            pool.join()
    else:

        initialize_worker()
        for arguments in processing_arguments:
            process_replay(arguments)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    start_processing("./DEMOS/Input", "./DEMOS/Output/")