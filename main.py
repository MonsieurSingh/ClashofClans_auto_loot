import pyautogui
import random

" Clash of Clans Bot "
" Works by searching for attacks, deploying troops and surrendering after 1 star victory. Then repeats until storages are full. "
" Click locations are mapped to keyboard keys for easy configuration. "
" Using bluestacks as emulator. "

def check_storages_full():
   # Storages are mathematically full after at most 90 attacks so count 90 iterations then return True
    check_storages_full.counter += 1
    if check_storages_full.counter >= 90:
        return True
    return False

check_storages_full.counter = 0

def search_attack():
    pyautogui.press('space')
    pyautogui.sleep(1)
    pyautogui.press('e')
    pyautogui.sleep(1)
    pyautogui.press('i')
    pyautogui.sleep(4)
    return

def align_screen():
    pyautogui.keyDown('s')
    pyautogui.sleep(1)
    pyautogui.keyUp('s')
    pyautogui.keyDown('d')
    pyautogui.sleep(1)
    pyautogui.keyUp('d')

def deploy_troops():
    # select troop 1
    pyautogui.press('1')
    pyautogui.sleep(1)
    # deploy troops by pressing 'G' 40 times with 1 second interval
    for _ in range(20):
        pyautogui.press('g')
        pyautogui.sleep(0.1)
    # select heroes by pressing keys 3-6 and deploy them by pressing 'Q'
    for hero_key in ['3', '4', '5', '6']:
        pyautogui.press(hero_key)
        pyautogui.sleep(0.25)
        pyautogui.press('q')
        pyautogui.sleep(0.25)
    # select battle machine by pressing '2' then press 'Q' to deploy it
    pyautogui.press('2')
    pyautogui.sleep(0.5)
    pyautogui.press('q')
    pyautogui.sleep(0.5)
    # select spell by pressing '7' then deloy them at random locations of the screen 11 times but around the middle of the screen not too close to the edges
    pyautogui.press('7')
    pyautogui.sleep(0.5)
    for _ in range(15):
        x = pyautogui.size().width // 4 + random.randint(0, pyautogui.size().width // 2)
        y = pyautogui.size().height // 4 + random.randint(0, pyautogui.size().height // 2)
        pyautogui.click(x, y)
        pyautogui.sleep(0.15)
    # press hero abilities by pressing the keys 3-6 again
    for hero_key in ['3', '4', '5', '6']:
        pyautogui.press(hero_key)
        pyautogui.sleep(0.5)
        pyautogui.press('q')
        pyautogui.sleep(0.5)
    return

def surrender():
    # wait 20 seconds and then surrender by pressing 'E' then 'O' to confirm then 'H' to back to home screen
    pyautogui.sleep(20)
    pyautogui.press('e')
    pyautogui.sleep(2)
    pyautogui.press('o')
    pyautogui.sleep(2)
    pyautogui.press('h')
    pyautogui.sleep(5)
    return

def main():
    # wait 5 seconds to allow user to switch to bluestacks window
    print("Starting in 5 seconds. Switch to Bluestacks window.")
    pyautogui.sleep(5)
    while True:
        search_attack()
        align_screen()
        deploy_troops()
        surrender()
        storages_full = check_storages_full()
        if storages_full:
            print("Storages are full. Stopping the bot.")
            break

if __name__ == "__main__":
    main()