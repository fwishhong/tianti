import random
import time
import os

class Player:
    def __init__(self):
        self.health = 100
        self.energy = 100
        self.items = []
        self.skills = []
        
class Game:
    def __init__(self):
        self.player = Player()
        self.game_over = False
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_slow(self, text):
        """逐字打印文本，创造打字机效果"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.03)
        print()
        
    def print_status(self):
        """显示玩家状态"""
        print("\n=== 状态 ===")
        print(f"生命值: {self.player.health}")
        print(f"体力值: {self.player.energy}")
        print(f"物品: {', '.join(self.player.items)}")
        print(f"技能: {', '.join(self.player.skills)}")
        print("===========\n")
        
    def make_choice(self, choices):
        """处理玩家选择"""
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice}")
        
        while True:
            try:
                choice = int(input("\n请选择 (输入数字): "))
                if 1 <= choice <= len(choices):
                    return choice
                else:
                    print("无效的选择，请重试。")
            except ValueError:
                print("请输入有效的数字。")
                
    def climb_challenge(self):
        """天梯攀登挑战"""
        self.print_slow("你面临一段特别危险的攀爬...")
        success_chance = random.randint(1, 100)
        
        if self.player.energy < 30:
            success_chance -= 30
        
        if "灵活技巧" in self.player.skills:
            success_chance += 20
            
        if success_chance > 50:
            self.print_slow("你成功通过了这段危险的路程！")
            self.player.energy -= 20
            return True
        else:
            self.print_slow("你失足了！受到了伤害...")
            self.player.health -= 30
            self.player.energy -= 30
            return False
            
    def village_scene(self):
        """村庄场景"""
        self.clear_screen()
        self.print_slow("\n你站在部落中，远处的天梯若隐若现...")
        
        choices = [
            "与村民交谈",
            "寻找草药",
            "训练身手",
            "开始登天梯",
            "查看状态"
        ]
        
        choice = self.make_choice(choices)
        
        if choice == 1:
            self.talk_to_villagers()
        elif choice == 2:
            self.search_herbs()
        elif choice == 3:
            self.training()
        elif choice == 4:
            self.start_climbing()
        elif choice == 5:
            self.print_status()
            
    def talk_to_villagers(self):
        """与村民交谈"""
        self.clear_screen()
        self.print_slow("\n村民们围在你身边，讲述着关于天梯的传说...")
        
        villager_stories = [
            "听说天梯顶端有能治百病的仙丹...",
            "已经有很多人在天梯上失去了生命...",
            "传说我们的祖先就是从天上下来的...",
            "天梯上的机关非常危险，要小心啊..."
        ]
        
        self.print_slow(random.choice(villager_stories))
        input("\n按回车键继续...")
        
    def search_herbs(self):
        """寻找草药"""
        self.clear_screen()
        self.print_slow("\n你在山脚下寻找草药...")
        
        if random.random() > 0.5:
            self.print_slow("你找到了一些有用的草药！")
            self.player.items.append("草药")
            self.player.health += 10
        else:
            self.print_slow("你没有找到什么特别的东西...")
            
        input("\n按回车键继续...")
        
    def training(self):
        """训练场景"""
        self.clear_screen()
        self.print_slow("\n你开始训练自己的身手...")
        
        if "灵活技巧" not in self.player.skills and random.random() > 0.7:
            self.print_slow("经过勤奋的训练，你掌握了新的技巧！")
            self.player.skills.append("灵活技巧")
        else:
            self.print_slow("你感觉身手更加敏捷了...")
            
        self.player.energy -= 10
        input("\n按回车键继续...")
        
    def start_climbing(self):
        """开始爬天梯"""
        self.clear_screen()
        self.print_slow("\n你站在天梯脚下，开始了充满未知的攀登之旅...")
        
        stages = [
            "钢刺机关",
            "旋转门",
            "激光迷宫",
            "最终之门"
        ]
        
        for stage in stages:
            self.print_slow(f"\n=== {stage} ===")
            if not self.climb_challenge():
                if self.player.health <= 0:
                    self.game_over = True
                    self.print_slow("\n你的生命耗尽了...")
                    return
                    
            if self.player.energy <= 0:
                self.print_slow("\n你的体力耗尽了，不得不返回村子...")
                return
                
        # 到达终点
        self.reach_top()
        
    def reach_top(self):
        """到达天梯顶端"""
        self.clear_screen()
        self.print_slow("\n你终于到达了天梯的顶端，推开了那扇神秘的石门...")
        self.print_slow("\n然而，门后空无一物。你明白了天梯的真相...")
        
        choices = [
            "告诉村民真相",
            "隐瞒真相",
            "寻找其他出路"
        ]
        
        choice = self.make_choice(choices)
        
        if choice == 1:
            self.ending_truth()
        elif choice == 2:
            self.ending_hide()
        else:
            self.ending_search()
            
        self.game_over = True
        
    def ending_truth(self):
        """真相结局"""
        self.print_slow("\n你选择告诉村民真相。")
        self.print_slow("虽然遭到了怀疑和排斥，但你相信这是正确的选择...")
        self.print_slow("也许有一天，人们会明白你的用意。")
        
    def ending_hide(self):
        """隐瞒结局"""
        self.print_slow("\n你选择隐瞒真相。")
        self.print_slow("你告诉村民们天梯上的机关太过危险...")
        self.print_slow("人们依然生活在希望中，但你的内心永远背负着这个秘密。")
        
    def ending_search(self):
        """探索结局"""
        self.print_slow("\n你决定寻找其他出路。")
        self.print_slow("也许答案不在天上，而在人间...")
        self.print_slow("你开始带领村民探索新的生存方式。")
        
    def run(self):
        """运行游戏主循环"""
        self.clear_screen()
        self.print_slow("欢迎来到《天梯》")
        self.print_slow("\n在这个被云海环绕的深山峡谷中，你的村落世代守护着一座通天的巨大阶梯...")
        self.print_slow("作为一个十六岁的少年，你即将面临攀登天梯的挑战。")
        
        while not self.game_over:
            self.village_scene()
            
        self.print_slow("\n=== 游戏结束 ===")

if __name__ == "__main__":
    game = Game()
    game.run()
