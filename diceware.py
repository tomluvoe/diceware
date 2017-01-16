import argparse
import secrets

def open_wordlist(filename):
    """ Open wordlist """
    wordlist = []
    with open(filename,'r') as wordfile:
        for line in wordfile:
            word = line.split()
            if len(word) == 2 and word[0].isdigit():
                wordlist.append(word)
    return wordlist

def create_numbers(length=6):
    """ Create numbers """
    numbers = []
    for i in range(length):
        numbers.append("")
        for j in range(5):
            numbers[i] += str(secrets.randbelow(6)+1)
    return numbers

def passphrase(numbers):
    """ Create passphrase """
    passphrase = ''
    for n in numbers:
        for w in wordlist:
            if w[0] == n:
                passphrase += w[1] + ' '
    return passphrase

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Diceware passphrases.')
    parser.add_argument('--file', default='diceware.wordlist.asc', help='Diceware word list')
    args = parser.parse_args()
    wordlist = open_wordlist(args.file)
    for i in range(10):
        numbers = create_numbers()
        print(passphrase(numbers))
