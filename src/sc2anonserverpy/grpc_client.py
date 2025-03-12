import logging
from multiprocessing import Pool
from pathlib import Path

import typer
from typing_extensions import Annotated

from sc2anonserverpy.client_functions.grpc_sc2reader_client_functions import (
    ProcessReplayArguments,
    initialize_worker,
    process_replay,
)
from sc2anonserverpy.settings import LOGGING_FORMAT


# NOTE: For clean output of CLI arguments for README:
# import typer.core

# typer.core.rich = None


# Initiate multiprocessing spawning processes that are using load_replay
# This must be done by popping a list so that processes don't have the same replay by accident.
def get_replays(replay_directory: Path):
    return list(replay_directory.rglob("*.SC2Replay"))


def main(
    replay_directory: Annotated[
        Path,
        typer.Option(
            exists=True,
            file_okay=False,
            dir_okay=True,
            resolve_path=True,
            help="Path to the directory that contains .SC2Replay files.",
        ),
    ],
    output_directory: Annotated[
        Path,
        typer.Option(
            exists=True,
            file_okay=False,
            dir_okay=True,
            resolve_path=True,
            help="Path to the directory where .pickle files for processed replays will be saved.",
        ),
    ],
    agents: Annotated[
        int,
        typer.Option(
            help="Number of multiprocessing agents.",
        ),
    ] = 1,
    chunksize: Annotated[
        int,
        typer.Option(
            help="Number of replays to process by each agent.",
        ),
    ] = 1,
    multiprocessing: Annotated[
        bool,
        typer.Option(
            help="True if multiprocessing should be used.",
        ),
    ] = False,
    anonymize_toon: Annotated[
        bool,
        typer.Option(
            help="True if the unique toon should be anonymized.",
        ),
    ] = True,
    anonymize_chat: Annotated[
        bool,
        typer.Option(
            help="True if chat should be anonymized.",
        ),
    ] = True,
):
    # Setting up logging:
    logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT)

    # Starting the processing of replays:
    start_processing(
        replay_directory=replay_directory,
        output_directory=output_directory,
        agents=agents,
        chunksize=chunksize,
        multiprocessing=multiprocessing,
        anonymize_toon=anonymize_toon,
        anonymize_chat=anonymize_chat,
    )


def start_processing(
    replay_directory: Path,
    output_directory: Path,
    agents: int,
    chunksize: int,
    multiprocessing: bool,
    anonymize_toon: bool,
    anonymize_chat: bool,
):
    logging.info("Entered start_processing()")

    # Getting a list of replay filepaths by using a helper function:
    list_of_replays = get_replays(replay_directory)
    logging.info(f"Got len(list_of_replays)=={len(list_of_replays)}")

    processing_arguments = []
    for replay_path in list_of_replays:
        processing_arguments.append(
            ProcessReplayArguments(
                replay_filepath=replay_path,
                output_dir=output_directory,
                anonymize_toon=anonymize_toon,
                anonymize_chat=anonymize_chat,
            )
        )

    processing_arguments_iterator = iter(processing_arguments)

    if multiprocessing:
        logging.info(f"Detected {multiprocessing=}")
        # Defining available pool of processes for replay processing:
        with Pool(processes=agents, initializer=initialize_worker) as pool:
            pool.imap_unordered(
                process_replay,
                processing_arguments_iterator,
                chunksize,
            )
            pool.close()
            pool.join()
    else:
        logging.info(f"Detected {multiprocessing=}")
        initialize_worker()
        for replay_file in list_of_replays:
            process_replay(
                replay_file=replay_file,
                output_dir=output_directory,
                anonymize_toon=anonymize_toon,
                anonymize_chat=anonymize_chat,
            )


if __name__ == "__main__":
    typer.run(main)
