import random
import pyautogui
import config as cfg
import attack
import upgrade

" Clash of Clans Bot "
" Works by searching for attacks, deploying troops and surrendering after 1 star victory. Then repeats until storages are full. "
" Click locations are mapped to keyboard keys for easy configuration. "
" Using bluestacks as emulator. "

def check_storages_full():
    check_storages_full.counter += 1
    if check_storages_full.counter >= cfg.STORAGE_CHECK_LIMIT:
        return True
    return False

check_storages_full.counter = 0

pyautogui.FAILSAFE = True

def main():
    print(f"Starting in {cfg.START_DELAY_SECONDS} seconds. Switch to Bluestacks window.")
    pyautogui.sleep(cfg.START_DELAY_SECONDS)
    while True:
        attack.search_attack()
        attack.align_screen()
        attack.deploy_troops()
        attack.surrender()
        if check_storages_full.counter % cfg.UPGRADE_WALLS_EVERY == 0:
            upgrade.upgrade_walls()
        storages_full = check_storages_full()
        if storages_full:
            print("Storages are full. Stopping the bot.")
            break

if __name__ == "__main__":
    main()