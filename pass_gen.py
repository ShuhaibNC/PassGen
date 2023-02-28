import requests
import random
import string
from sys import argv
import os

flag = 0
try:
    if_num = int(argv[1])
except ValueError:
    if_num = 1
try:
    if if_num <= 0 or argv[1] == '--help' or argv[1] == '-h':
        print("""
pass_gen --help: To see this message
SYNTAX:
pass_gen [number of passwords to generate]
          """)
        exit()
except IndexError:
    print("""                                                                          pass_gen --help: To see this message
SYNTAX
    pass_gen [number of passwords to generate]                                                       """)
    exit()
while flag < int(argv[1]):
    print(f"[{flag+1}] Creating password...")
    adjresp = requests.get("https://gist.githubusercontent.com/hugsy/8910dc78d208e40de42deb29e62df913/raw/eec99c5597a73f6a9240cab26965a8609fa0f6ea/english-adjectives.txt")
    adj = random.choice(adjresp.text.split('\n'))
    nounresp = requests.get("https://raw.githubusercontent.com/hugsy/stuff/main/random-word/english-nouns.txt")
    noun = random.choice(nounresp.text.split("\n"))
    num = str(random.randrange(100))
    punct = random.choice(string.punctuation)
    passw = adj + noun + num + punct
    with open('pass.txt', 'a') as f:
        f.write(passw + '\n')
    flag += 1
os.system("echo -e Passwords are stored in $(pwd)/pass.txt")
