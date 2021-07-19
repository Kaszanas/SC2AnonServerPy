# SC2Science

## Usage

```main.py``` - Multiprocessing of replays using gRPC.
```grpc_server.py``` - Server used to synchronize anonymization.

In order to begin processing please install ```requirements.txt``` and follow these steps:

1. Place replays in ```./DEMOS/Input```
2. Run ```python grpc_server.py```
3. Run ```python main.py```
