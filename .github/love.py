import tkinter as tk
import random
import threading
import time

# 情话列表
messages = [
    "想你了！", "注意休息", "发来一条想念", "晚安好梦", "吃饭了吗",
    "摸摸头~", "睡不着呢", "天天开心哦~", "我想你了！", "爱你呀",
    "想你一整天", "和我一起吃早餐吧", "今天也要加油呀！", "注意休息啊",
    "想你到爆！", "今天见面吗？", "想你！", "小心感冒哦", "见面吗？",
    "抱一抱", "想你~", "女神", "要喝热水哦", "好想你在我身边",
    "传递爱", "你在看我吗", "喝杯奶茶吧！", "下课一起走呀",
    "想你三秒钟", "抱一抱", "期待我们的下次见面", "给你所有爱",
    "想你想到睡不着", "想你在我身边", "多喝热水~", "今天开心吗？",
    "要开心哦", "希望你也想我", "你让我的世界更美好", "早点睡呀",
    "抱一抱", "早点睡呀", "每一天都想你", "别熬夜哦"
]

def dow():
    window = tk.Tk()
    # 获取屏幕宽高
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # 随机窗口位置与大小
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    win_width = random.randint(100, 200)
    win_height = random.randint(50, 100)
    window.title("亲爱的")
    window.geometry(f"{win_width}x{win_height}+{x}+{y}")
    # 随机选一条情话
    msg = random.choice(messages)
    tk.Label(
        window,
        text=msg,
        bg="pink",
        font=("黑体", 10),
        width=win_width,
        height=win_height
    ).pack()
    window.mainloop()

# 多线程生成多个窗口
threads = []
for i in range(200):  # 可调整窗口数量
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.05)  # 间隔启动避免卡顿
    threads[i].start()