"""
Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
"""

import collections

text = input("")

words = text.split()

counter = collections.Counter(words)

most_common, occurrences = counter.most_common()[0]

longest = max(words, key=len)

print(most_common, longest)