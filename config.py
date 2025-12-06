# General
START_DELAY_SECONDS = 5
STORAGE_CHECK_LIMIT = 90

# Search / matchmaking sequence: list of (key, sleep_after_seconds)
SEARCH_SEQUENCE = [
    ('space', 1),
    ('e', 1),
    ('i', 4),
]

# Screen alignment
ALIGN_ZOOM_KEY = 'down'
ALIGN_ZOOM_DURATION = 2  # seconds to hold zoom key
ALIGN_KEYS = [
    ('s', 1),
    ('d', 1),
]

# Troop deployment
TROOP_SELECT_KEY = '1'
TROOP_SELECT_SLEEP = 1

DEPLOY_KEY = 'g'
DEPLOY_COUNT = 20
DEPLOY_INTERVAL = 0.1

HERO_KEYS = ['3', '4', '5', '6']
HERO_DEPLOY_KEY = 'q'
HERO_DEPLOY_SLEEP = 0.25
HERO_ABILITY_SLEEP = 0.5

BATTLE_MACHINE_KEY = '2'
BATTLE_MACHINE_DEPLOY_SLEEP = 0.5

# Spells
SPELL_KEY = '7'
SPELL_SELECT_SLEEP = 0.5
SPELL_COUNT = 15
# Spell placement area (fractions of screen). Example 0.25..0.75 = middle half
SPELL_AREA = {
    'x_min_frac': 0.25,
    'x_max_frac': 0.75,
    'y_min_frac': 0.25,
    'y_max_frac': 0.75,
}
SPELL_INTERVAL = 0.15

# Surrender / end of attack sequence
SURRENDER_WAIT = 20
SURRENDER_SEQUENCE = [
    ('e', 2),  # open surrender
    ('o', 2),  # confirm
    ('h', 5),  # return home
]