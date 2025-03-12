from pathlib import Path
import pickle


# def format_replay(replay):
#     pass
# output = replay.name
# for team in replay.teams:
#     for player in team.players:
#         if player.is_human:
# output += str(player.PACStats.ppm)

# return output


if __name__ == "__main__":
    filepath = Path(
        "./processing/demos/output/0efefaaddb4e76d4f0ff030ab8155eff.pickle"
    ).resolve()

    with filepath.open("rb") as filepath:
        messages_0 = pickle.load(filepath)
        print(messages_0)

        event_dict = {}
        for event in messages_0.events:
            if event.name == "ChatEvent":
                print(event.text)
            if event.name in event_dict:
                event_dict[event.name] = event_dict[event.name] + 1
            else:
                event_dict[event.name] = 1
