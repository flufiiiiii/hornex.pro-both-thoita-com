from agent import GameAgent

agent = GameAgent()
agent.run()
print("=== 游戏代理报告 ===")
print(agent.generate_report())

# 示例用户修改
slot = (400, 850)
agent.apply_correction(slot, 'health', 5000)
print("修正后报告：")
print(agent.generate_report())
