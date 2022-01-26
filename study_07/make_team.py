#-*- coding:utf-8 -*-
import random
from datetime import datetime
from queue import Queue

def run():
    mates = ['한다운', '서다빈', '송민혜', '유치영', '신아현', '이루오', '형진석', '박세관', '정엘윤', '원유석']
    std_num = datetime.now().day%9+1

    today_mates = mates[std_num:] + mates[:std_num]
    mates_a = today_mates[:5]
    mates_b = today_mates[5:]

    random.shuffle(mates_a)
    random.shuffle(mates_b)

    for team in zip(['a','b'],[mates_a, mates_b]):
        print(f'{team[0]} Group')
        for i, name in list(enumerate(team[1])):
            print(f'{name}님 {i+1}번 면접자')
        print('='*30)

if __name__ == '__main__':
    run()
