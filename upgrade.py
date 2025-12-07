import random
import pyautogui
import config as cfg

def check_walls():
    """
    Clicks near the center vertical band of the screen to select walls and attempts to upgrade them.
    Uses configuration values from config.py.
    """
    w, h = pyautogui.size().width, pyautogui.size().height
    x_min = int(w * cfg.WALL_CLICK_X_MIN_FRAC)
    x_max = int(w * cfg.WALL_CLICK_X_MAX_FRAC)
    y_min = int(h * cfg.WALL_CLICK_Y_MIN_FRAC)
    y_max = int(h * cfg.WALL_CLICK_Y_MAX_FRAC)

    for _ in range(cfg.WALL_UPGRADE_TRIES):
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        pyautogui.click(x, y)
        pyautogui.sleep(cfg.WALL_CLICK_SLEEP)

        # randomly choose between upgrading with gold or elixir
        if random.choice([True, False]):
            pyautogui.press(cfg.WALL_UPGRADE_KEY_GOLD)
        else:
            pyautogui.press(cfg.WALL_UPGRADE_KEY_ELIXIR)
        pyautogui.sleep(cfg.WALL_CLICK_SLEEP)

        # confirm / press upgrade confirm key (configurable)
        pyautogui.press(cfg.WALL_UPGRADE_CONFIRM_KEY)
        pyautogui.sleep(cfg.WALL_CLICK_SLEEP)

        # hold exit key to close upgrade menu
        pyautogui.keyDown(cfg.WALL_EXIT_KEY)
        pyautogui.sleep(cfg.WALL_CLICK_SLEEP)
        pyautogui.keyUp(cfg.WALL_EXIT_KEY)
        pyautogui.sleep(cfg.WALL_CLICK_SLEEP)

def align_screen():
    """
    Aligns the home screen using the configured zoom key and HOME_ALIGN_KEYS in config.py.
    """
    pyautogui.keyDown(cfg.ALIGN_ZOOM_KEY)
    pyautogui.sleep(cfg.ALIGN_ZOOM_DURATION)
    pyautogui.keyUp(cfg.ALIGN_ZOOM_KEY)
    for key, wait in cfg.HOME_ALIGN_KEYS:
        pyautogui.keyDown(key)
        pyautogui.sleep(wait)
        pyautogui.keyUp(key)

def upgrade_walls():
    align_screen()
    check_walls()