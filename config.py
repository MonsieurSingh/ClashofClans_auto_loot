# General
START_DELAY_SECONDS = 5
STORAGE_CHECK_LIMIT = 20000

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
HOME_ALIGN_KEYS = [
    ('w', 1),
    ('d', 1),
]

# Troop deployment
TROOP_SELECT_KEYS = ['1', '2', '3']
TROOP_SELECT_SLEEP = 1

DEPLOY_KEY = 'g'
DEPLOY_COUNT = 20
DEPLOY_INTERVAL = 0.1

HERO_KEYS = ['5', '6', '7', '8']
HERO_DEPLOY_KEY = 'q'
HERO_DEPLOY_SLEEP = 0.25
HERO_ABILITY_SLEEP = 0.5

BATTLE_MACHINE_KEY = '4'
BATTLE_MACHINE_DEPLOY_SLEEP = 0.5

# Spells
SPELL_KEY = '9'
SPELL_SELECT_SLEEP = 0.5
SPELL_COUNT = 15
# Spell placement area (fractions of screen). Example 0.25..0.75 = middle half
SPELL_AREA = {
    'x_min_frac': 0.44,
    'x_max_frac': 0.52,
    'y_min_frac': 0.25,
    'y_max_frac': 0.50,
}
SPELL_INTERVAL = 0.15

# Surrender / end of attack sequence
SURRENDER_WAIT = 25
SURRENDER_SEQUENCE = [
    ('e', 2),  # open surrender
    ('o', 2),  # confirm
    ('h', 5),  # return home
]

# Upgrade / walls configuration
WALL_UPGRADE_TRIES = 50
WALL_CLICK_X_MIN_FRAC = 0.44
WALL_CLICK_X_MAX_FRAC = 0.52
WALL_CLICK_Y_MIN_FRAC = 0.20
WALL_CLICK_Y_MAX_FRAC = 0.80
WALL_CLICK_SLEEP = 0.15

# keys used during wall upgrade
WALL_UPGRADE_KEY_GOLD = 'u'
WALL_UPGRADE_KEY_ELIXIR = 'k'
WALL_UPGRADE_CONFIRM_KEY = 'k'
WALL_EXIT_KEY = 'x'

UPGRADE_WALLS_EVERY = 30