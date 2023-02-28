import requests
import random
import string
from sys import argv
import os

flag = 0

def help():
    print("""
Usage: python pass_gen.py [MAXIMUM] [OPTIONS] [STRINGS] 

OPTIONS:
    -o              Output filename with extension

Try 'python pass_gen.py --help | -h for more info'""")

if len(argv) < 2:
    help()

if argv[1] == '--help' or argv[1] == '-h':
    help()
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
    if '-o' in argv:
        filename = argv[argv.index('-o') + 1]
    elif '-o' not in argv:
        filename = 'pass.txt'
    with open(filename, 'a') as f:
        f.write(passw + '\n')
    flag += 1
print('Passwords are stored in', os.getcwd()+'/'+filename)
