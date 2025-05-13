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
def decipher(text, shift_amount):
    text = text.replace(' ', '')
    unshifted = ''
    for c in text:
        if c.islower():
            unshifted += chr((ord(c) - ord('a') - shift_amount) % 26 + ord('a'))
        elif c.isupper():
            unshifted += chr((ord(c) - ord('A') - shift_amount) % 26 + ord('A'))
    return unshifted

if __name__ == '__main__':
    original_text = get_original_text()
    shift_amount = get_shift_amount()
    text_letter_only = remove_nonletters(original_text)
    cipher_text = cipher(text_letter_only, shift_amount)
    print(f'cipher_text={cipher_text}')
    decipher_text = decipher(cipher_text, shift_amount)
    print(f'decipher_text={decipher_text}')