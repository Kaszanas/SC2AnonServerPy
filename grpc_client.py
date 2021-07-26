from grpc_sc2reader_client_functions import process_replay, anonymize, anonymize_nicknames, initialize_worker
from multiprocessing import Pool
import argparse
import os
import logging
from itertools import product

from settings import LOGGING_FORMAT

# Initiate multiprocessing spawning processes that are using load_replay
# This must be done by popping a list so that processes don't have the same replay by accident.
def get_replays(replay_directory:str):

    absolute_filepaths = []
    # Listing the files available in a supplied directory, checking for the right extension and obtaining absolute path:
    for replay in os.listdir(replay_directory):
        if replay.endswith(".SC2Replay"):
            absolute_filepaths.append(os.path.abspath(os.path.join(replay_directory, replay)))

    return absolute_filepaths


def start_processing(args_replay_directory:str,
                    args_output_directory:str,
                    args_agents:int,
                    args_chunksize:int,
                    args_multiprocessing:bool):

    # Getting a list of replay filepaths by using a helper function:
    list_of_replays = get_replays(args_replay_directory)
    logging.info(f"Got list_of_replays= {len(list_of_replays)}")

    processing_arguments = product(list_of_replays, [args_output_directory])

    if args_multiprocessing:
        # Defining available pool of processes for replay processing:
        with Pool(processes=args_agents, initializer=initialize_worker) as pool:
            # test_var = list(product(list_of_replays, [output_directory]))
            pool.imap_unordered(process_replay, processing_arguments, args_chunksize)
            pool.close()
            pool.join()
    else:
        initialize_worker()
        for arguments in processing_arguments:
            process_replay(arguments)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="StarCraft II replay processing tool that uses multiprocessing.")
    parser.add_argument("--input_dir", type=str, default="./DEMOS/Input", help="Provide the path to the input directory that contains .SC2Replay files.")
    parser.add_argument("--output_dir", type=str, default="./DEMOS/Output", help="Provide the path to the output directory that will contain .pickle files.")
    parser.add_argument("--agents", type=int, default=44, help="Provide how much agents will be available in the pool for execution.")
    parser.add_argument("--chunksize", type=int, default=1000, help="Provide how much replays are to be processed at once.")
    parser.add_argument("--use_multiprocessing", type=bool, default=True, help="Set this flag to true if You would like to use multiprocessing.")

    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT)
    start_processing(replay_directory=args.input_dir,
                    output_directory=args.output_dir,
                    args_agents=args.agents,
                    args_chunksize=args.chunksize,
                    args_multiprocessing=args.use_multiprocessing)