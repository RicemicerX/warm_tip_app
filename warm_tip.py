# -*- coding: utf-8 -*-
"""
每0.2秒弹出一个新的温馨提示窗口
- 保留所有已弹出的窗口（不自动关闭）
- 最多弹出50个窗口
- 文字带黑色描边效果（防止与背景混淆）
"""
import tkinter as tk
import random

# === 参数设置 === #
WINDOW_W, WINDOW_H = 280, 80     # 每个窗口大小
INTERVAL_MS = 200                # 每0.2秒弹一次
MAX_WINDOWS = 50                 # 最多50个窗口
FONT = ('Microsoft YaHei', 18, 'bold')  # 粗体字体，增强可读性

TIPS = [
    '多喝水哦~', '保持微笑呀~', '每天都要元气满满',
    '记得吃水果', '保持好心情', '好好爱自己',
    '早点休息', '愿所有烦恼都消失',
    '今天过得开心嘛', '天冷了，多穿衣服'
]
BG_COLORS = [
    'lightpink', 'skyblue', 'lightgreen', 'lavender',
    'lightyellow', 'plum', 'coral', 'bisque',
    'aquamarine', 'mistyrose', 'honeydew',
    'lavenderblush', 'oldlace'
]

root = tk.Tk()
root.withdraw()
count = 0

def popup_once():
    global count
    if count >= MAX_WINDOWS:
        return
    count += 1
    tip = random.choice(TIPS)
    bg = random.choice(BG_COLORS)

    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    margin = 40
    x = random.randint(margin, max(margin, sw - WINDOW_W - margin))
    y = random.randint(margin, max(margin, sh - WINDOW_H - margin))

    win = tk.Toplevel(root)
    win.title('温馨提示')
    win.geometry(f'{WINDOW_W}x{WINDOW_H}+{x}+{y}')
    win.attributes('-topmost', True)
    win.configure(bg=bg)

    canvas = tk.Canvas(win, bg=bg, highlightthickness=0)
    canvas.pack(fill='both', expand=True)

    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        canvas.create_text(
            WINDOW_W // 2 + dx,
            WINDOW_H // 2 + dy,
            text=tip,
            font=FONT,
            fill='black'
        )

    canvas.create_text(
        WINDOW_W // 2,
        WINDOW_H // 2,
        text=tip,
        font=FONT,
        fill='white'
    )

    win.bind('<Button-1>', lambda e: win.destroy())
    root.after(INTERVAL_MS, popup_once)

popup_once()
root.mainloop()
