#!/usr/bin/env python
import sys

current_word = None
current_count = 0

# Read input from standard input
for line in sys.stdin:
    # Parse the input line
    word, count = line.strip().split('\t')
    count = int(count)

    # Check if the word has changed
    if current_word == word:
        current_count += count
    else:
        # Emit the count for the previous word
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# Emit the count for the last word
if current_word:
    print(f"{current_word}\t{current_count}")
