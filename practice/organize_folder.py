import shutil
import time
import os

dir = 'C:/Users/russe/Downloads'

actions = [
    (('.png', '.jgp', '.gif'), 'images'),
    (('.mp4', '.mov', '.avi'), 'videos'),
    (('.exe', '.rar', '.zip'), 'exe_zip'),
    (('.wav', '.mp3', '.flac'), 'audio'),
    (None, 'other')
]


def create_dir(dir):
    for _, dir_name in actions:
        if dir_name not in os.listdir(dir):
            os.mkdir(dir + '/' + dir_name)


