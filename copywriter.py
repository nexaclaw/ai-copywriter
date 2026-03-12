#!/usr/bin/env python3
"""
AI Copywriter - 智能文案工厂
Nexa Claw (https://nexaclaw.cn/)
"""

import json
import sys
import random
import argparse
from typing import List, Dict

class AICopywriter:
    """智能文案生成器"""
    
    def __init__(self):
        self.brand = "Nexa Claw"
        self.website = "https://nexaclaw.cn/"
        
        # 标题模板库
        self.title_templates = {
            "爆款": [
                "震惊！{}，看完我沉默了...",
                "千万别{}，除非你想...",
                "为什么{}？背后的原因让人意外",
                "{}的正确打开方式，第3个绝了！",
                "我用{}个月做到了{}，方法很简单",
            ],
            "小红书": [
                "姐妹们！{}真的绝了✨",
                "终于找到了{}的正确姿势！",
                "{}测评｜踩雷预警❌ vs 真香警告✅",
                "收藏了！{}保姆级教程📖",
            ],
            "抖音": [
                "关于{}，很多人不知道的真相",
                "我用{}天验证了{}，结果惊人",
                "你知道吗？{}其实很简单",
            ]
        }
    
    def generate_titles(self, topic: str, style: str = "爆款", count: int = 5) -> List[str]:
        """生成爆款标题"""
        templates = self.title_templates.get(style, self.title_templates["爆款"])
        selected = random.sample(templates, min(count, len(templates)))
        
        titles = []
        for t in selected:
            if t.count("{}") > 1:
                titles.append(t.format(topic, topic))
            elif "{}" in t:
                titles.append(t.format(topic))
            else:
                titles.append(t)
        return titles
    
    def generate_xiaohongshu(self, topic: str) -> str:
        """生成小红书文案"""
        return f"""
姐妹们！今天分享{topic}✨

用了{random.randint(1,30)}天，真的爱了！

✅ 优点：
- 效果明显
- 操作简单  
- 性价比高

💡 使用tips：
1. 建议每天坚持
2. 配合其他方法效果更好

真的推荐！姐妹们冲！💖

#好物推荐 #种草 #分享
"""
    
    def generate_tags(self, topic: str, count: int = 10) -> List[str]:
        """生成热门标签"""
        tags = [topic, f"#{topic}", "#干货", "#分享", "#推荐"]
        return tags[:count]

def main():
    parser = argparse.ArgumentParser(description='AI Copywriter')
    parser.add_argument('topic', help='主题')
    parser.add_argument('--style', choices=['爆款', '小红书', '抖音'], default='爆款')
    parser.add_argument('--count', type=int, default=5)
    
    args = parser.parse_args()
    writer = AICopywriter()
    
    print(f"\n🎯 为 '{args.topic}' 生成内容...")
    
    titles = writer.generate_titles(args.topic, args.style, args.count)
    print(f"\n📝 {args.style}标题：")
    for i, t in enumerate(titles, 1):
        print(f"  {i}. {t}")
    
    if args.style == "小红书":
        print(f"\n📱 小红书文案：")
        print(writer.generate_xiaohongshu(args.topic))
    
    print(f"\n🏷️ 推荐标签：")
    print(f"  {' '.join(writer.generate_tags(args.topic))}")

if __name__ == '__main__':
    main()
