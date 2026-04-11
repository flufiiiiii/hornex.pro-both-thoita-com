from perception import read_ground_coords, read_petal_info
from actions import move_towards, pick_loot, attack, merge_petals
from config import PETAL_SLOT_COORDS, LOOT_COORDS
import time

class GameAgent:
    def __init__(self):
        self.report_log = []
        self.petal_stats = {}

    def run(self):
        print("请切换至游戏窗口，5秒后开始自动操作...")
        time.sleep(5)
        # 示例循环（自动拾取、移动到某区域、花瓣学习、攻击）
        for loot in LOOT_COORDS:
            pick_loot(loot)
            self.report_log.append(f"Picked up loot at {loot}")

        # 自动学习花瓣信息
        for slot in PETAL_SLOT_COORDS:
            info = read_petal_info(slot)
            self.petal_stats[str(slot)] = info
            self.report_log.append(f"Petal at {slot}: {info}")

        # 示例区域移动：假设你要移动到(70,30)
        target_area = (70, 30)
        cur_pos = read_ground_coords()
        if cur_pos:
            while abs(cur_pos[0] - target_area[0]) > 2 or abs(cur_pos[1] - target_area[1]) > 2:
                move_towards(target_area, cur_pos)
                time.sleep(0.1)
                cur_pos = read_ground_coords()

        # 自动攻击示例
        for _ in range(5):
            attack()
            time.sleep(0.5)

    def generate_report(self):
        rep = "\n".join(self.report_log)
        rep += "\nPetal stats:\n"
        for slot, info in self.petal_stats.items():
            rep += f"{slot}: {info}\n"
        return rep

    def apply_correction(self, slot, prop, value):
        if str(slot) in self.petal_stats:
            self.petal_stats[str(slot)][prop] = value
            self.report_log.append(f"Correction: Petal {slot} {prop} -> {value}")
