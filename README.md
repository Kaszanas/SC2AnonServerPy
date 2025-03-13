[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5138313.svg)](https://doi.org/10.5281/zenodo.5138313)

# SC2AnonServerPy

This project is used for weak anonymization of StarCraft II replays for research. Depending on further parsing and extraction implementations this project can assist with replacing toon identifiers (unique) or nicknames (not unique) with a weak anonymized ID or a customized function.

## Installation

> [!NOTE]
> To run this project there are some prerequisites that you need to have installed on your system:
> - Docker
> - **Optional** make (if you do not wish to use make, please refer to the commands defined in the `makefile` and run them manually)

Our prefered way of distributing the toolset is through DockerHub. We use the Docker Image to provide a fully reproducible environment for our scripts.

To pull the image from DockerHub, run the following command:

```bash
docker pull kaszanas/datasetpreparator:latest
```

If you wish to clone the repository and build the Docker image yourself, run the following command:

```bash
make docker_build
```

## Usage


1. Place replays in ```./processing/demos/input``` which is a default path for the replay input.
2. Open a terminal and run ```make grpc_server```, which is responsible for persistent anonymization process.
3. Open another terminal and run ```make grpc_client``` with default command line arguments to start up a sample replay processing.
4. The resulting processed files will be placed in ```./processing/demos/output``` by default.
5. Turn off the server by a keyboard interrupt (CTRL+C).

### CLI Usage

The ```grpc_server.py``` script is used to start the gRPC anonymization server. The script has the following command line arguments:

```
Usage: grpc_server.py [OPTIONS]

Options:
  --anonymized-db-path FILE  Path to the .pickle file that will be used to
                             store anonymized nicknames.  [required]
  --help                     Show this message and exit.
```

The ```grpc_client.py``` script is used to start the replay processing. The script has the following command line arguments:

```
Usage: grpc_client.py [OPTIONS]

Options:
  --replay-directory DIRECTORY    Path to the directory that contains
                                  .SC2Replay files.  [required]
  --output-directory DIRECTORY    Path to the directory where .pickle files
                                  for processed replays will be saved.
                                  [required]
  --agents INTEGER                Number of multiprocessing agents.  [default:1]
  --chunksize INTEGER             Number of replays to process by each agent.
                                  [default: 1]
  --multiprocessing / --no-multiprocessing
                                  True if multiprocessing should be used.
                                  [default: no-multiprocessing]
  --anonymize-toon / --no-anonymize-toon
                                  True if the unique toon should be
                                  anonymized.  [default: anonymize-toon]
  --anonymize-chat / --no-anonymize-chat
                                  True if chat should be anonymized.
                                  [default: anonymize-chat]
  --help                          Show this message and exit.
```


## Implementation Notes

If You would like to implement a custom anonymization function please see the `Listener` class in `grpc_server.py`.

For the sake of logging and comments when "nickname" is mentioned it means any string that is meant to be anonymized and is sent to the gRPC server for that matter.

Pleaase keep in mind that the `grpc_client.py` is a sample implementation and uses https://github.com/ggtracker/sc2reader to perform processing.

## Cite Us!

```
@software{Bialecki2021,
  author       = {Białecki, Andrzej and
                  Białecki, Piotr},
  title        = {{Kaszanas/SC2AnonServerPy: 1.0.0 SC2AnonServerPy
                   Release}},
  month        = jul,
  year         = 2021,
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.5138313},
  url          = {https://doi.org/10.5281/zenodo.5138313}
}
```
