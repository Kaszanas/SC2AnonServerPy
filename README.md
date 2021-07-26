[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5138314.svg)](https://doi.org/10.5281/zenodo.5138314)

# SC2AnonServerPy

This project is used for weak anonymization of StarCraft II replays for research. Depending on further parsing and extraction implementations this project can assist with replacing toon identifiers (unique) or nicknames (not unique) with a week anonymized ID or a customized function.

## Usage

- ```grpc_server.py``` - Server used to synchronize anonymization.
- ```grpc_client.py``` - Client with multiprocessing of replays using gRPC server for persistent anonymization.

1. Install Python 3.7.7
2. **OPTIONAL**: Create a virtual environment by running the following command (replace ```<path_to_venv>``` with a path) ```python -m venv <path_to_venv>```.
3. **OPTIONAL**: Activate the environment which You created.
4. Install ```requirements.txt``` by performing the following command ```pip install -r requirements.t``` In order to begin processing please install ```requirements.txt``` and follow these steps:

5. Place replays in ```./DEMOS/Input``` which is a default path for the replay input.
6. Run ```python grpc_server.py```, which is responsible for persistent anonymization process.
7. Run ```python grpc_client.py``` with command line arguments which will start up a sample replay processing usage below:

```
usage: grpc_client.py [-h] [--input_dir INPUT_DIR] [--output_dir OUTPUT_DIR]
                      [--agents AGENTS] [--chunksize CHUNKSIZE]
                      [--use_multiprocessing USE_MULTIPROCESSING]
                      [--anonymize_toon ANONYMIZE_TOON]
                      [--anonymize_chat ANONYMIZE_CHAT]

StarCraft II replay processing tool that uses multiprocessing.

optional arguments:
  -h, --help            show this help message and exit
  --input_dir INPUT_DIR
                        Provide the path to the input directory that contains
                        .SC2Replay files.
  --output_dir OUTPUT_DIR
                        Provide the path to the output directory that will
                        contain .pickle files.
  --agents AGENTS       Provide how much agents will be available in the pool
                        for execution.
  --chunksize CHUNKSIZE
                        Provide how much replays are to be processed at once.
  --use_multiprocessing USE_MULTIPROCESSING
                        Set this flag to true if You would like to use
                        multiprocessing.
  --anonymize_toon ANONYMIZE_TOON
                        Set this flag to true if You would like to perform
                        toon/nickname anonymization.
  --anonymize_chat ANONYMIZE_CHAT
                        Set this flag to true if You would like to perform
                        chat anonymization.
```

8. The resulting processed files will be placed in ```./DEMOS/Output``` by default.

## Notes

If You would like to implement a custom anonymization function please see the ```Listener``` class in ```grpc_server.py```.

For the sake of logging and comments when "nickname" is mentioned it means any string that is meant to be anonymized and is sent to the gRPC server for that matter.

Pleaase keep in mind that the ```grpc_client.py``` is a sample implementation and uses https://github.com/ggtracker/sc2reader to perform processing.

## Cite Us!

Citation required!