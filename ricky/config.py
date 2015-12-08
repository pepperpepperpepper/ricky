import os

"""ALL GLOBAL CONSTANTS GO HERE"""


USERNAME = "RICHARD_GIOVANNI"
TEST_URL = (
    "http://i.asdf.us/im/"
    "65/imBreak5qI6DN2_14254-PbPattern_1444004782_pepper.png"
)
PB_BASE = "http://asdf.us/"


def _add_pb_base(path):
    return os.path.join(PB_BASE, path)

PATTERN_URL_BASE = _add_pb_base("impattern/patterns")
PB_DATA_URL = _add_pb_base("im/data")

PBPATTERN_URL = _add_pb_base("im/api/impattern")
PBGRID_URL = _add_pb_base("im/api/imgrid")
PBGRADIENT_URL = _add_pb_base("im/api/imgradient")
PBBREAKER_URL = _add_pb_base("im/api/imbreak")

# offline mode, true by default
OFFLINE = True

PROBABILITIES_DIR = "share/probabilities"
