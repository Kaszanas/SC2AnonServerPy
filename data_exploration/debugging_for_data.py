import sc2reader
from PACAnalyzer.pacanalyzer import PACAnalyzer
import pickle

infile_0 = open('./DEMOS/Output/11506437_1566325283_230842.pickle','rb')
messages_0 = pickle.load(infile_0)
print(messages_0)

event_dict = {}
for event in messages_0.events:
    if event.name == "ChatEvent":
        print(event.text)
    if event.name in event_dict:
        event_dict[event.name] = event_dict[event.name] + 1
    else:
        event_dict[event.name] = 1


# def format_replay(replay):
#     pass
    # output = replay.name
    # for team in replay.teams:
    #     for player in team.players:
    #         if player.is_human:
                # output += str(player.PACStats.ppm)

    # return output