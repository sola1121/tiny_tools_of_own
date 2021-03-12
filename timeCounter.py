#!/usr/bin/env python3

# 命令行倒计时, 时间到了将会播放同目录下的音乐文件

import os
import sys
import time
import random
import datetime
import subprocess


CUR_DIR = os.path.dirname(sys.argv[0])

GRE_date = datetime.datetime(2021, 12, 26, 0, 0, 0)


def choice_music() -> str:
    """在该文件所在目录中寻找声音文件, 并返回其路径的列表
       用作计时结束后播放
    """
    all_items = os.listdir(CUR_DIR)
    wav_musics = list()
    for music in all_items:
        if music.endswith((".wav",".mp3")):
            wav_musics.append(music)
    if len(wav_musics) <= 0:
        music_path = str()
    else:
        music_path = os.path.join(CUR_DIR, random.choice(wav_musics))
    return music_path


def aim_date() -> datetime.datetime:
    """输入小时数, 并加上当前日期时间, 然后返回
       作为计时到点的结束日期时间
    """
    while True:
        try:
            hours = int(input("规定倒计时(时): "))
        except ValueError:
            print("ERROR! 输入有误.")
            continue
        if hours > 4:
            print("当前设定小时数大于4小时, 不建议这样过长计时, 是否继续? (y/n)")
            is_ok = input()
            if is_ok.lower().strip() != 'y':
                continue
        elif hours < 0:
            print("当前设定小时数小于0小时, 请重新输入.")
            continue
        task_Htime = datetime.timedelta(hours=hours)
        break
    return datetime.datetime.now() + task_Htime


if __name__ == "__main__":

    lost_date =  GRE_date - datetime.datetime.now()
    print("\n剩余天数 - ", lost_date.days)

    try:
        end_date = aim_date()
        while (differ_date := end_date - datetime.datetime.now()):
            if differ_date.total_seconds() <= .0:
                break
            time.sleep(1)
            print("任务倒计时 ▶ %.0f:%02.0f" % (differ_date.total_seconds()//60, differ_date.total_seconds()%60), end='\r')
        print("时间到, Good Job 🎶️")
        music_path = choice_music()
        if music_path:
            print(music_path)
            subprocess.Popen(["/usr/bin/celluloid", music_path])
        else:
            print('\a'*2, end='')
    except KeyboardInterrupt:
        print(" - 中断程序 ")
    finally:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        for _ in range(0, 3, 1):
            time.sleep(1)
