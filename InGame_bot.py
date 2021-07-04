import time
import pyautogui
from pynput.keyboard import Key, Listener
from pynput.keyboard._win32 import KeyCode
from os import system

pyautogui.FAILSAFE = False

fail_safe = False

retry = (901, 966)
restaurant = (301, 615)
DOC_DEFAULT = (605, 470)
confirm_loadout = (384, 358)
settings = (1758, 118)

LONE_WOLF = (467, 351)
NORMAL = (233, 429)

POS_TH_SCREEN = (678, 382)
COLOR_TH_SCREEN = (26, 33, 42)

PLAY_BUTTON_POS = (441, 402)

POS_OK_REMOVED = (931, 1011)
COLOR_REMOVED1 = (14, 14, 15)
COLOR_REMOVED2 = (14, 14, 14)
COLOR_REMOVED3 = (15, 15, 15)

POS_IN_MATCHMAKING = (1426, 493)
COLOR_IN_MATCHMAKING = (16, 21, 30)
POS_EXIT_MATCHMAKING = (951, 777)

POS_LVL = (1567, 101)
COLOR_LVL = (33, 36, 41)

DOC_IMG_PATH = "doc.png"

time.sleep(3)

start_time = time.time()


def get_time_d_str():
    d = time.gmtime(time.time() - start_time)

    return f"\nDays:{d.tm_mday - 1}\n{time.strftime('%H:%M:%S', d)}\n"


def on_press(key: KeyCode):
    global fail_safe

    if fail_safe is False:
        if key == Key.space:
            fail_safe = True

        elif str(key)[1].lower() == 'n':
            print(get_time_d_str())

        elif str(key)[1].lower() == 'b':
            # print("\n" * 13)
            system("cls")


        else:
            print(key)


def get_pos_by_img(img_path):
    coords = pyautogui.locateOnScreen(img_path)

    if coords is None:
        pos = DOC_DEFAULT
        print("Default doc")

    else:
        pos = coords[0] + int(coords[2] / 2), coords[1] + int(coords[3] / 2)
        print("Real doc")

    return pos


def clicker(position):
    pyautogui.moveTo(position)
    pyautogui.dragRel(1, 1)
    time.sleep(0.05)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.dragRel(1, 1)
    time.sleep(0.4)


def check_to_continue():
    global fail_safe

    if input("Do you want to continue? ").lower() == 'y':
        fail_safe = False


def main():
    global fail_safe

    print("Started")

    #doc_pos = get_pos_by_img(DOC_IMG_PATH)

    with Listener(on_press=on_press):
        while fail_safe is False:
            # check if in game
            img = pyautogui.screenshot().load()

            if img[POS_LVL] == COLOR_LVL:
                # pyautogui.hotkey("win", "alt", "g")
                # print("\Main Screen, check replays\n")
                print("\nMain Screen")
                print(get_time_d_str())
                print("Continuing\n")

                clicker(PLAY_BUTTON_POS)
                time.sleep(1.4)
                clicker(LONE_WOLF)
                clicker(NORMAL)
                time.sleep(1)

            if img[POS_TH_SCREEN] == COLOR_TH_SCREEN:
                # pyautogui.hotkey("win", "alt", "g")
                # print("\nTH Screen, check replays\n")
                print("\nTH Screen")
                print(get_time_d_str())
                print("Continuing\n")

                clicker(LONE_WOLF)
                clicker(NORMAL)
                time.sleep(1)

            if img[POS_OK_REMOVED] == COLOR_REMOVED1 or img[POS_OK_REMOVED] == COLOR_REMOVED2 or img[
                POS_OK_REMOVED] == COLOR_REMOVED3:
                # pyautogui.hotkey("win", "alt", "g")
                # print("\nRemoved Screen, check replays\n")
                print("\nRemoved Screen")
                print(get_time_d_str())
                print("Continuing\n")

                clicker(POS_OK_REMOVED)
                time.sleep(0.5)
                clicker(PLAY_BUTTON_POS)
                time.sleep(1)

            if img[POS_IN_MATCHMAKING] == COLOR_IN_MATCHMAKING:
                # pyautogui.hotkey("win", "alt", "g")
                # print("\nMatchmaking Screen, check replays\n")
                print("\nMatchmaking Screen")
                print(get_time_d_str())
                print("Continuing\n")

                clicker(POS_EXIT_MATCHMAKING)
                time.sleep(1.2)
                clicker(PLAY_BUTTON_POS)
                time.sleep(1)

            # click all the things

            clicker(retry)

            clicker(restaurant)

            clicker(DOC_DEFAULT)

            clicker(confirm_loadout)

            if fail_safe is True:
                check_to_continue()

    print(get_time_d_str())


if __name__ == '__main__':
    main()
