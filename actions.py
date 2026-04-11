import pyautogui
import random
import time

def move_towards(target_coords, current_coords):
    dx = target_coords[0] - current_coords[0]
    dy = target_coords[1] - current_coords[1]
    if dx > 0: pyautogui.keyDown('d'); time.sleep(0.05); pyautogui.keyUp('d')
    elif dx < 0: pyautogui.keyDown('a'); time.sleep(0.05); pyautogui.keyUp('a')
    if dy > 0: pyautogui.keyDown('s'); time.sleep(0.05); pyautogui.keyUp('s')
    elif dy < 0: pyautogui.keyDown('w'); time.sleep(0.05); pyautogui.keyUp('w')

def pick_loot(loot_coord):
    pyautogui.moveTo(*loot_coord)
    pyautogui.click()

def attack():
    pyautogui.keyDown('space')
    time.sleep(0.08)
    pyautogui.keyUp('space')

def merge_petals(slot1, slot2):
    pyautogui.moveTo(*slot1)
    pyautogui.dragTo(*slot2, duration=0.5, button='left')
