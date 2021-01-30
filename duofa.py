#!/usr/bin/env python3
import pyperclip
import os
import sys
import subprocess
from SMS.sms_gv import getSMS as sms
from dotenv import load_dotenv, find_dotenv

def main():
    load_dotenv(dotenv_path=os.path.join(sys.path[0], '.env'))
    if os.getenv('DUOFA_H'):
        duofa_h = os.getenv('DUOFA_H')
    else:
        duofa_h = None
    while True:
        try:
            textcode = sms()
            if textcode.isdigit():
                cmd = "echo -n %s | shasum -a 512256 | awk '{print $1}'" % textcode
                hash = subprocess.getoutput("echo -n %s | shasum -a 512256 | awk '{print $1}'" % textcode)
                if not duofa_h == None:
                    if not hash == duofa_h:
                        break
                    else:
                        del hash
                else:
                    break
            pass
        except IndexError:
            pass
        except KeyboardInterrupt:
            exit()
    pyperclip.copy(textcode)
    try:
        os.system('afplay /System/Library/Sounds/Hero.aiff')
    except:
        pass
    with open(os.path.join(sys.path[0], '.env'), 'w+') as file:
        file.write(f'DUOFA_H={hash}')
    print(f'Copied {len(textcode)} characters ({textcode}) to clipboard.')
    exit()


if __name__ == "__main__":
    main()
