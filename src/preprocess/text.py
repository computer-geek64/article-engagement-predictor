#!/usr/bin/python3
# text.py

import contractions
from word2number.w2n import word_to_num


def clean_text(text):
    cleaned_text = contractions.fix(text.strip()).lower()
    words = [x for x in cleaned_text.split(' ') if x]

    current_number = []
    i = 0
    while i < len(words):
        try:
            word_to_num(words[i])
            current_number.append(words[i])
            words.pop(i)
        except ValueError:
            if current_number:
                j = 0
                prod = 1
                while j < len(current_number):
                    try:
                        float(current_number[j])
                        prod *= int(current_number[j]) if current_number[j].isdecimal() else float(current_number[j])
                        current_number.pop(j)
                    except ValueError:
                        j += 1
                words.insert(i, str(prod * word_to_num(' '.join(current_number))))
                current_number.clear()
                i += 1

            i += 1
    else:
        if current_number:
            words.append(str(word_to_num(' '.join(current_number))))

    return ' '.join(words)
