#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
current_user = None
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, user, count = line.split('\t', 2)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word and current_user == user:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s\t%s' % (current_word, user, current_count)
        current_count = count
	current_user = user
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s\t%s' % (current_word, current_user, current_count)
