import sc2reader
from PACAnalyzer.pacanalyzer import PACAnalyzer
import pickle

import os

sc2reader.engine.register_plugin(PACAnalyzer())


def format_replay(replay):
    pass
    # output = replay.name
    # for team in replay.teams:
    #     for player in team.players:
    #         if player.is_human:
                # output += str(player.PACStats.ppm)

    # return output

replays = sc2reader.load_replays('./DEMOS/Input', load_level=4)
for replay in replays:

    name_of_replay = os.path.splitext(os.path.basename(replay.filename))[0]
    with open(f'./DEMOS/Output/{name_of_replay}.pickle', 'wb') as f:
        pickle.dump(replay, f)
    print(format_replay(replay))