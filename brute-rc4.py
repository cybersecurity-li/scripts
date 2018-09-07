#!/usr/bin/env python3

import requests

def main():
    char, mask = None, None
    lowest_c = None
    mask_pos = 0
    mask_len = 8
    url  = 'http://REDACTED.com:1339/encrypt?content=Cookie%3A%20sessionid%3D'
    
    while mask_pos < mask_len:
        lowest = 9999999
        print('Starting Round')
        print('Position:', mask_pos)
        while char != '=':
            char = nx(char)
            mask = gen_mask(mask, mask_pos, mask_len, char)
            r = requests.get(url + mask)
            #print('[DEBUG]', url+mask)
            result = len(r.text)
            print(mask, ':', result)
            if result < lowest:
                lowest = result
                lowest_c = char
                print('New lowest:', lowest, lowest_c)
        print('=' * 20)
        print('Round finished')
        print('Round result:', lowest_c)
        print('=' * 20)
        mask = gen_mask(mask, mask_pos, mask_len, lowest_c)
        mask_pos += 1
        char = None
    print('Result:', mask)


def nx(last):
    table = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/', '=' ]
    if not last:
        return table[0]
    return table[table.index(last)+1]


def gen_mask(old, pos, le, char):
    mask = [''] * le
    for i in range(0, le):
        if i < pos:  mask[i] = old[i]
        if i == pos: mask[i] = char
    return ''.join(mask)

if __name__ == '__main__':
    main()
