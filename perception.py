import pyautogui
import easyocr
from config import GROUND_COORD_REGION, MINIMAP_REGION, INFO_PANEL_REGION

reader = easyocr.Reader(['en'])

def read_ground_coords():
    img = pyautogui.screenshot(region=GROUND_COORD_REGION)
    res = reader.readtext(img)
    for _, text, _ in res:
        if "," in text:
            try:
                x, y = map(int, text.split(","))
                return (x, y)
            except:
                pass
    return None

def capture_map():
    img = pyautogui.screenshot(region=MINIMAP_REGION)
    return img

def read_petal_info(petal_slot):
    pyautogui.moveTo(*petal_slot)
    pyautogui.click()
    img = pyautogui.screenshot(region=INFO_PANEL_REGION)
    res = reader.readtext(img)
    info = {}
    for _, text, _ in res:
        if "Health" in text:
            info['health'] = int(text.split()[-1])
        if "Body Damage" in text:
            info['body_damage'] = int(text.split()[-1])
        # 可扩展其它属性
    return info
