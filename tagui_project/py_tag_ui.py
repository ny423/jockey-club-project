import time
from random import randint
import os

url_link = 'https://campaigns.hkjc.com/goracing/ch/'

os.system(rf'cmd /c "pip install -r requirements.txt"')


import tagui as t
from get_html_values import get_video_names
def show_more_videos():
    t.click('wpb_raw_code wpb_content_element wpb_raw_html more')


def click_and_close_video(vnum: int, freq: int = 1):
    for j in range(freq):
        print(f"{time.strftime('%H:%M:%S', time.localtime())}: clicking '{video_list[vnum]}' *{j + 1}")
        t.click(f'(//*[@class = "clickPopupItem"])[{vnum + 1}]')
        t.wait(0.5)
        t.click('video_close')
        t.wait(0.5)
    t.click(f'(//*[@class = "ex-close"])[{vnum + 1}]')
    t.wait(0.5)


def get_video_views(video_list: list) -> list:
    views = []
    for j in range(len(video_list)):
        views.append(t.read(f'(//*[@class = "viewcount"])[{j + 1}]'))
    return views


def semi_auto_mode():
    while True:
        print('video list:')
        view_list = get_video_views(video_list)
        for i in range(len(video_list)):
            print(f"video {i}: {video_list[i]}, views: {view_list[i]}")
        video_num = int(input('input the video num you want to play, enter -1 to terminate the program: '))
        if video_num <= -1:
            break
        frequency = int(input('input the repeating frequency: '))
        while frequency < 0:
            frequency = int(input('invalid value, please re-input the repeating frequency: '))
        click_and_close_video(video_num, frequency)

    print('program terminated')
    t.close()

def auto_mode():
    while True:
        view_list = get_video_views(video_list)
        videos = [(i, video_list[i], int(view_list[i][:-6])) for i in range(len(video_list))]
        videos.sort(key=lambda x: x[2])
        print(f'video with least views: {videos[0]}')
        click_and_close_video(videos[0][0], randint(5, 50))

def user_input_mode():
    f = open(file="input.txt", mode="r", encoding='utf8')
    lines = f.readlines()
    print(lines)
    # assert(lines[1].isnumeric())
    video_name = lines[0].replace('\n', '')
    freq = int(lines[1])
    for i in range(len(video_list)):
        if video_list[i] == video_name:
            click_and_close_video(i, freq)
            break


if __name__ == '__main__':

    t.init(visual_automation=True, chrome_browser=True)
    t.url(url_link)

    print('initializing...')
    for _ in range(5):  # show all videos
        print('clicking 更多...')
        show_more_videos()

    video_list = get_video_names()  # get all video names

    # auto_mode()

    # semi_auto_mode()

    user_input_mode()
