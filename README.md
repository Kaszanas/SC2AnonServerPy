# SC2AnonServerPy

This project is used for weak anonymization of StarCraft II replays for research. Depending on further parsing and extraction implementations this project can assist with replacing toon identifiers (unique) or nicknames (not unique) with a week anonymized ID or a customized function.

## Usage

```grpc_server.py``` - Server used to synchronize anonymization.
```grpc_client.py``` - Client with multiprocessing of replays using gRPC.

In order to begin processing please install ```requirements.txt``` and follow these steps:

1. Place replays in ```./DEMOS/Input```
2. Run ```python grpc_server.py```, which is responsible for anonymization process.
3. Run ```python grpc_client.py```, which parses 

## Notes

If You would like to implement a custom anonymization function please see the ```Listener``` class in ```grpc_server.py```.

Pleaase keep in mind that the ```grpc_client.py``` is a sample implementation and uses https://github.com/ggtracker/sc2reader to perform processing.