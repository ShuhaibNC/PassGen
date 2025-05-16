# 🔐 Password Generator

A simple Python script that generates random passwords by combining real English adjectives, nouns, numbers, and special characters.

## 📦 Features

- Fetches real English words from public URLs
- Generates strong and readable passwords
- Saves all generated passwords to a file
- Customizable output file name

## 🚀 Usage

```bash
python pass_gen.py [MAXIMUM] [OPTIONS]
```

## Arguments:
- MAXIMUM: Number of passwords to generate (required)

## Options:
- -o filename.txt : Set custom output file name (default is pass.txt)
- --help or -h : Show help message and exit

## Example:
python pass_gen.py 10 -o secure.txt
(This generates 10 passwords and saves them in secure.txt)

## Output:
Passwords are saved in the current working directory.

## Example Passwords:
BraveTiger23!
LazySky47$
MightyWave88#

## Requirements:
- Python 3.10.0
- requests module

## Install Dependencies:
pip install requests

## Notes:
- Requires internet access to fetch word lists
- Be mindful of rate limits from the external word sources
