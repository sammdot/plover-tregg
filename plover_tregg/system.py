# fmt: off
#
#   # # # # # # # # # #
#   ย ง บ ด * ก ต ร น ม
#   ว ม ก น * ค ป ล ง ย
#
#       O o  ⋂ ⋃
#
# Note the unconventional steno order -- right side first left-to-right,
# then thumbs left-to-right, then left side right-to-left. This is according
# to the creator's design, since Thai has more complex onsets than codas.
KEYS = (
  "#",
  "ก-", "ค-", "ต-", "ป-", "ร-", "ล-", "น-", "ง-", "ม-", "ย-",
  "O-", "o-",
  "*",
  "-⋂", "-⋃",
  "-ด", "-น", "-บ", "-ก", "-ง", "-ม", "-ย", "-ว"
)
# fmt: on

IMPLICIT_HYPHEN_KEYS = ("O-", "o-", "*", "-⋂", "-⋃")
SUFFIX_KEYS = ()
NUMBER_KEY = "#"
NUMBERS = {
  "-ย": "-1",
  "-ง": "-2",
  "-บ": "-3",
  "-ด": "-4",
  "O-": "5-",
  "o-": "0-",
  "ก-": "6-",
  "ต-": "7-",
  "ร-": "8-",
  "น-": "9-",
}
FERAL_NUMBER_KEY = False

UNDO_STROKE_STENO = "*"

ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_RULES_ALIASES = {}
ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
  "Keyboard": {
    "#": ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"),
    "-ย": "q",
    "-ว": "a",
    "-ง": "w",
    "-ม": "s",
    "-บ": "e",
    "-ก": "d",
    "-ด": "r",
    "-น": "f",
    "O-": "c",
    "o-": "v",
    "*": ("t", "g", "y", "h"),
    "-⋂": "n",
    "-⋃": "m",
    "ก-": "u",
    "ค-": "j",
    "ต-": "i",
    "ป-": "k",
    "ร-": "o",
    "ล-": "l",
    "น-": "p",
    "ง-": ";",
    "ม-": "[",
    "ย-": "'",
    "no-op": ("z", "x", "b", ",", ".", "/", "]", "\\"),
  },
  "Gemini PR": {
    # fmt: off
    "#": (
      "#1", "#2", "#3", "#4", "#5", "#6",
      "#7", "#8", "#9", "#A", "#B", "#C",
    ),
    # fmt: on
    "-ย": "S1-",
    "-ว": "S2-",
    "-ง": "T-",
    "-ม": "K-",
    "-บ": "P-",
    "-ก": "W-",
    "-ด": "H-",
    "-น": "R-",
    "O-": "A-",
    "o-": "O-",
    "*": ("*1", "*2", "*3", "*4"),
    "-⋂": "-E",
    "-⋃": "-U",
    "ก-": "-F",
    "ค-": "-R",
    "ต-": "-P",
    "ป-": "-B",
    "ร-": "-L",
    "ล-": "-G",
    "น-": "-T",
    "ง-": "-S",
    "ม-": "-D",
    "ย-": "-Z",
    "no-op": ("Fn", "pwr", "res1", "res2"),
  },
}

DICTIONARIES_ROOT = "asset:plover_tregg:dictionaries"
DEFAULT_DICTIONARIES = []
