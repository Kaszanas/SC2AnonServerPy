# SC2AnonServerPy

## Usage

```grpc_server.py``` - Server used to synchronize anonymization.
```grpc_client.py``` - Client with multiprocessing of replays using gRPC.

In order to begin processing please install ```requirements.txt``` and follow these steps:

1. Place replays in ```./DEMOS/Input```
2. Run ```python grpc_server.py```, which is responsible for anonymization process.
3. Run ```python grpc_client.py```, which parses 

