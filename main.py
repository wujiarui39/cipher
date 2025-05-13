print('this code is written by jiarui wu')
print('this is written by jingfan cai.')

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

def remove_nonletters(input_text):
    return ''.join(c for c in input_text if c.isalpha())

def cipher(text, shift_amount):
    shifted = ''
    for c in text:
        if c.islower():
            shifted += chr((ord(c) - ord('a') + shift_amount) % 26 + ord('a'))
        elif c.isupper():
            shifted += chr((ord(c) - ord('A') + shift_amount) % 26 + ord('A'))
    grouped = ' '.join(shifted[i:i+5] for i in range(0, len(shifted), 5))
    return grouped