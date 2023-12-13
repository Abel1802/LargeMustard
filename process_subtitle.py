import os
import re
import numpy as np


def extract_text_from_subtitle(subtitle):
    # 使用正则表达式匹配时间戳和文本
    pattern = re.compile(r'\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+\n(.+?)\n', re.DOTALL)
    
    # 使用findall方法获取所有匹配的结果
    matches = pattern.findall(subtitle)
    
    # 返回匹配的文本结果
    return matches


def deal_with_a_file():
    f = open("raw_data/Friends.S01.en.BlueRay.AllEpisodes/friends_s01e01_720p_bluray_x264-sujaidr.srt", 'r')
    raw_text = f.read()
    print(raw_text)
    matches = extract_text_from_subtitle(raw_text)
    print(matches)
    print(len(matches))
    

def main():
    deal_with_a_file()


if __name__ == "__main__":
    main()