import s2protocol
import logging
import mpyq
from s2protocol import versions
from settings import LOGGING_FORMAT

logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT)
archive = mpyq.MPQArchive(
    "D:\\Projects\\SC2Science\\DEMOS\\Input\\15483236_1595287901_1162.SC2Replay"
)

contents = archive.header["user_data_header"]["content"]
logging.info(contents)

header = versions.latest().decode_replay_header(contents)
logging.info(header)

base_build = header["m_version"]["m_baseBuild"]
logging.info(base_build)

protocol = versions.build(base_build)

contents = archive.read_file("replay.game.events")
game_events = protocol.decode_replay_game_events(contents)

cmdEventList = []
for event in game_events:
    if event["_event"] == "NNet.Game.SCmdEvent":
        cmdEventList.append(event)

print(cmdEventList)
