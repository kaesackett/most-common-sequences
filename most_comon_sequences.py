"""
Outputs a list of the 100 most common three-word sequences in the text,
along with a count of how many times each occurred in the text. The program
ignores punctuation, line endings, and is case insensitive.

Not exactly the best code I've ever written. I literally wrote this in like an hour.

EXAMPLE USAGE
cat some-file.txt | ./most_common_sequences.py
            - or -
python3 most_common_sequences.py some-file.txt another-file.txt

EXAMPLE OUTPUT
Given Darwin's 'Origin of Species' (http://www.gutenberg.org/cache/epub/2009/pg2009.txt):
$ cat origin_of_species.txt | ./most_common_sequences.py | jq .
{
  "of the same": "272",
  "the same species": "118",
  "conditions of life": "107",
  "in the same": "97",
  "of natural selection": "95",
  "from each other": "89",
  [...]
}
"""

import collections
import nltk
import sys
import re

def normalize_text(input):
    """Normalize our input a little bit for processing to ensure
    that punctuation and line breaks are ignored, and the grouping
    is case insensitive."""

    # Remove all punctuation and split on whitespace
    input = re.sub(r'\W+', ' ', input)
    input = input.split()

    # Force lowercase
    clean_text = [word.lower() for word in input]

    return clean_text

def find_ngrams(input_list, n):
    """Given an array of words, returns a mapping of recurring phrases
    in a given text to the number of times each phrase appears."""

    ngrams = zip(*[input_list[i:] for i in range(n)])
    sequences = (' '.join(w) for w in ngrams)

    # collections.Counter's most_common method returns a list of the n most common elements and their counts
    # Check it yo: https://docs.python.org/2/library/collections.html#collections.Counter
    result = collections.Counter(sequences)

    # Only problem is, it's hideous - transform to JSON
    return magic_json(result.most_common(100))

def magic_json(list_of_iterables):
    """Transform a given a list of iterables (tuples, lists) into JSON.
    Exists for the sole purpose of improving readability of the output."""

    join = ""
    output = "{"
    for i in list_of_iterables:
        output += join + '"' + str(i[0]) + '":"' + str(i[1]) + '"'
        join = ","

    return output + "}"

if __name__=='__main__':
    files = sys.argv[1:]
    if not files:
        files = ["/dev/stdin"]

    for file in files:
        with open(file) as input:
            # Normalize the text
            normalized_text = normalize_text(input.read())

            # Analyze the text
            print(find_ngrams(normalized_text, 3))
