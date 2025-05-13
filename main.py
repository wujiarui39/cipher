print('this code is written by jiarui wu')
this is written by jingfan cai.

import argparse
import string

def get_original_text():
    with open('input.txt', 'r', encoding='utf-8') as f:
        return f.read()
def get_shift_amount():
    parser = argparse.ArgumentParser()
    parser.add_argument('--shift', type=int, default=1)
    args = parser.parse_args()
    return args.shift
