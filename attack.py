import pyautogui
import random
import config as cfg

def align_screen():
    # zoom out first by holding the zoom key for configured duration
    pyautogui.keyDown(cfg.ALIGN_ZOOM_KEY)
    pyautogui.sleep(cfg.ALIGN_ZOOM_DURATION)
    pyautogui.keyUp(cfg.ALIGN_ZOOM_KEY)
    for key, wait in cfg.ALIGN_KEYS:
        pyautogui.keyDown(key)
        pyautogui.sleep(wait)
        pyautogui.keyUp(key)
    return

def search_attack():
    for key, wait in cfg.SEARCH_SEQUENCE:
        pyautogui.press(key)
        pyautogui.sleep(wait)
    return

def deploy_troops():
    # select troop
    for troop_key in cfg.TROOP_SELECT_KEYS:
        pyautogui.press(troop_key)
        pyautogui.sleep(cfg.TROOP_SELECT_SLEEP)
        for _ in range(cfg.DEPLOY_COUNT):
            pyautogui.press(cfg.DEPLOY_KEY)
            pyautogui.sleep(cfg.DEPLOY_INTERVAL)
    # pyautogui.press(cfg.TROOP_SELECT_KEY)
    # pyautogui.sleep(cfg.TROOP_SELECT_SLEEP)
    # deploy troops by pressing DEPLOY_KEY multiple times
    # select heroes and deploy abilities
    for hero_key in cfg.HERO_KEYS:
        pyautogui.press(hero_key)
        pyautogui.sleep(cfg.HERO_DEPLOY_SLEEP)
        pyautogui.press(cfg.HERO_DEPLOY_KEY)
        pyautogui.sleep(cfg.HERO_DEPLOY_SLEEP)
    # deploy battle machine
    pyautogui.press(cfg.BATTLE_MACHINE_KEY)
    pyautogui.sleep(cfg.BATTLE_MACHINE_DEPLOY_SLEEP)
    pyautogui.press(cfg.HERO_DEPLOY_KEY)
    pyautogui.sleep(cfg.BATTLE_MACHINE_DEPLOY_SLEEP)
    # select spell and deploy at random positions inside configured area
    pyautogui.press(cfg.SPELL_KEY)
    pyautogui.sleep(cfg.SPELL_SELECT_SLEEP)
    w, h = pyautogui.size().width, pyautogui.size().height
    x_min = int(w * cfg.SPELL_AREA['x_min_frac'])
    x_max = int(w * cfg.SPELL_AREA['x_max_frac'])
    y_min = int(h * cfg.SPELL_AREA['y_min_frac'])
    y_max = int(h * cfg.SPELL_AREA['y_max_frac'])
    for _ in range(cfg.SPELL_COUNT):
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        pyautogui.click(x, y)
        pyautogui.sleep(cfg.SPELL_INTERVAL)
    # press hero abilities again
    for hero_key in cfg.HERO_KEYS:
        pyautogui.press(hero_key)
        pyautogui.sleep(cfg.HERO_ABILITY_SLEEP)
        pyautogui.press(cfg.HERO_DEPLOY_KEY)
        pyautogui.sleep(cfg.HERO_ABILITY_SLEEP)
    return

def surrender():
    pyautogui.sleep(cfg.SURRENDER_WAIT)
    for key, wait in cfg.SURRENDER_SEQUENCE:
        pyautogui.press(key)
        pyautogui.sleep(wait)
    return