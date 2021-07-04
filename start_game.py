import os
import time
import pyautogui

R6S_LOCATION = "steam://rungameid/359550"
IN_GAME_BOT_LOCATION = "InGame_bot.py"

TIME_START_GAME = 60
TIME_AFTER_CLICK = 45

NOTHING_POS = (910, 95)

START_GAME_POS = (225, 345)
START_TH_POS = (255, 867)
LONE_WOLF_POS = (468, 360)
NORMAL_POS = (195, 433)


def clicker(position):
    pyautogui.moveTo(position)
    pyautogui.dragRel(1, 1)
    time.sleep(0.05)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.dragRel(1, 1)
    time.sleep(0.4)


def lunch_game():
    print("Lunching game")

    os.system("start " + R6S_LOCATION)

    print(f"Waiting {TIME_START_GAME} seconds")
    time.sleep(TIME_START_GAME)
    print(f"Done waiting {TIME_START_GAME} seconds\nClicking")

    clicker(NOTHING_POS)

    for i in range(10):
        clicker(NOTHING_POS)
        time.sleep(0.3)

    print(f"Done clicking\nWaiting {TIME_AFTER_CLICK} seconds")
    time.sleep(TIME_AFTER_CLICK)
    print(f"Done waiting {TIME_AFTER_CLICK} seconds")


def enter_TH():
    clicker(START_GAME_POS)
    time.sleep(2)
    clicker(START_TH_POS)
    time.sleep(1.5)
    clicker(LONE_WOLF_POS)
    time.sleep(1)
    clicker(NORMAL_POS)
    time.sleep(1)


def main():
    print("START GAME\n")
    lunch_game()
    print("Lunched game\n\nEntering")
    enter_TH()
    print("Entered game")
    print("Starting to play\n\n\n")

    os.system("py " + IN_GAME_BOT_LOCATION)


if __name__ == '__main__':
    main()
