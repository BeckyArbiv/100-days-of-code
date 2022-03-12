import time
from playsound import playsound
import tkinter as tk

def get_user_input():
    sec_input = input("Duration: ")
    return sec_input

def count_down(t):
    t = convert_to_format(t)
    while t > 0:
        min, sec = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(timer, end="\r")
        t -= 1
        time.sleep(1)

def convert_to_format(t):
    if ':' in t:
        time_list = t.split(':')
        int_list = list(map(int, time_list))
        min = int_list[0]*60
        time = min + int_list[1]
        print(f'Timer is set for {time} seconds')
        return time
    else:
        assert int(t), "input incorrect format"
        return int(t)

def sound_alarm():
    playsound('Day_2/mixkit-facility-alarm-sound-999.wav')
    print('Timer is up!')


def main():
    t = get_user_input()
    count_down(t)
    sound_alarm()


if __name__ == '__main__':
    main()