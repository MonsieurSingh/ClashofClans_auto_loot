Clash of Clans auto attacker, looter and wall upgrader bot
===============================================

This is a bot for the popular mobile game Clash of Clans. It automates attacking and looting resources from other players' villages so you can max out your walls without spending hours playing the game.

Features
--------
- Automated attacking of enemy villages
- Time optimised attack strategy
- Automatic wall upgrading when storages are supposedly full
- Configurable army composition and spell usage

Limitations
-----------
- Ratios are only tested for town halls 13-16
- Needs over 8gb RAM to run Bluestacks smoothly and avoid misclicks during long sessions
- Only attacks the first base found in matchmaking (may not be optimal depending on your trophy range)
- Spells are randomly deployed in a straight line across the centre of the base (may not be optimal for all bases)

Requirements
------------
- Python 3
- pyautogui
- Bluestacks
- Valkyries (Max level recommended for your town hall)
- Any seige machine (Log Launcher preferred)
- All 4 heroes (If heroes are being upgraded, modify the `HERO_KEYS` array in `config.py` to remove the corresponding hero key)
- (Optional) Alternatively use Super Barbarians if you don't have maxed Valkyries
- If using a custom army composition (or during events where special troops are automatically added to the army), modify the `TROOP_SELECT_KEYS` and `SPELL_SELECT_KEYS` arrays in `config.py` accordingly
- Modify the `SURRENDER_WAIT` variable in `config.py` to either:
    - 25 seconds for 2 stars (to allow time for heroes to clean up)
    - 5-10 seconds for 1 star
    Note: These values are only tested for maxed valkyries and might not work at every town hall level (please do your own testing to find the optimal value)

Installation
------------
1. Clone the repository
2. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```
3. Configure the bot settings in `config.py`
4. Open Bluestacks
5. Import the keyboard mapping by clicking on the keyboard icon in the sidebar and selecting "Import layout from file". Choose the `keymap.cfg` file provided in this repository. (Make sure you've selected the coc profile, else it won't work)
6. Open Clash of Clans and use the army configuration by clicking on the following hyperlink:
    • [Super Barbarians](https://link.clashofclans.com/en?action=CopyArmy&army=h4p1e40_9-1p2e20_3-2p3e4_5-0p0e10_8u64x26-1x91-1x87-1x75s11x10)
    which should look like this:
   ![Army Configuration](images/army.png)
   • OR use the Valkyries. [Valkyries](https://link.clashofclans.com/en?action=CopyArmy&army=h4p3e40_9-1p9e17_20-2p2e4_5-0p1e14_8i1x135-1x4-1x57-1x81d1x9-1x98u40x12-1x91-1x87-1x75s11x10).
   Feel free to customise the army composition as long as you're able to 1-star most bases under 20 seconds after deployment.
7. Use the following base layouts:
    • [TH 15](https://link.clashofclans.com/en?action=OpenLayout&id=TH15%3AHV%3AAAAABQAAAALyqvTgqf3LVADJ1UxoSF49)
    • [TH 16](https://link.clashofclans.com/en?action=OpenLayout&id=TH16%3AHV%3AAAAABQAAAAL0Ea1Tjrx5cv7Sph99OYbe)
   Or set up your own base with similar wall placements to the following image:
   ![Base Layout](images/base_layout.png)
    Make sure the walls run diagonally and vertically across the centre of the base and all the other buildings are sufficiently spaced out to prevent accidentally upgrading 'non-wall' buildings.

Usage
-----
- Open Bluestacks and launch Clash of Clans
- Make the Bluestacks window full screen.
- Run the bot:
    ```
    python bot.py
    ```
- You have 5 seconds to switch to the Bluestacks window before the bot starts executing.
- To stop the bot, press `Ctrl + C` in the terminal or drag the mouse to the top-left corner of the screen.

Easy modifications possible (without breaking the bot entirely)
-------------
- The army composition: `TROOP_SELECT_KEYS` array in `config.py`.
- The spell deployment keys: `SPELL_SELECT_KEYS` array in `config.py`.
- Hero usage: `HERO_KEYS` array in `config.py`.
- The surrender wait time: `SURRENDER_WAIT` variable in `config.py`.
- Only keymaps for troop slot 1-9 are supported. (Custom modifications need to be made in the keymap settings in Bluestacks to support more slots)
- How often walls are upgraded: `UPGRADE_WALLS_EVERY` variable in `config.py`.