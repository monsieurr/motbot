import random
import os
import sys


# select a quote (line) in a particular file
def select_quote(file):
    lines = open(file, encoding='utf-8').read().splitlines()
    quote = random.choice(lines)
    print(quote.encode('utf-8').decode(sys.stdout.encoding))
    return quote.encode('utf-8').decode(sys.stdout.encoding)

# capitalize the chosen quote
def capitalize_first_letter(quote):
    return str(quote).capitalize()

# capitalize
def capitalize_quote(quote):
    return str(quote).upper()
