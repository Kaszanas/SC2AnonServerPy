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

from datetime import datetime
loop_start_time = datetime.now()
replays = sc2reader.load_replays('./DEMOS/Input', load_level=4)
for index, replay in enumerate(replays):

    replay_start_time = datetime.now()

    name_of_replay = os.path.splitext(os.path.basename(replay.filename))[0]
    with open(f'./DEMOS/Output/{name_of_replay}.pickle', 'wb') as f:
        pickle.dump(replay, f)
    print(format_replay(replay))

    replay_end_time = datetime.now() - replay_start_time
    print(replay_end_time)

loop_end_time = datetime.now() - loop_start_time
print(loop_end_time)
