import time
import os

# 设置计时器和休息时间（单位：秒）
pomodoro_time = 25 * 60  
short_break_time = 5 * 60  

while True:
    # 倒计时25分钟
    for remaining in range(pomodoro_time, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("Focus Time:",timer, end="\r")
        time.sleep(1)

    # 播放警报声
    print("Time's up!")
    os.system('say "Time is up!"')

    # 短暂休息
    for remaining in range(short_break_time, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("Break Time:",timer, end="\r")
        time.sleep(1)

    # 提示用户开始下一个番茄钟
    print("Take the next pomodoro?")
    answer = input("> ")
    if answer.lower() not in ("yes", "y"):
        break

print("Goodbye!")
