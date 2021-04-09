#!/usr/bin/python3
# text.py

import contractions
from word2number.w2n import word_to_num
from stop_words import get_stop_words


def clean_text(text):
    cleaned_text = contractions.fix(text.strip()).lower()
    words = [x for x in cleaned_text.split(' ') if x]

    current_number = []
    i = 0
    while i < len(words):
        try:
            try:
                float(words[i])
                current_number.append(words[i])
                words.pop(i)
            except ValueError:
                pass

            word_to_num(words[i])
            current_number.append(words[i])
            words.pop(i)
        except ValueError:
            if current_number:
                j = 0
                prod = 1
                while j < len(current_number):
                    try:
                        prod *= float(current_number[j])
                        current_number.pop(j)
                    except ValueError:
                        j += 1

                if current_number:
                    num = prod * word_to_num(' '.join(current_number))
                else:
                    num = prod
                words.insert(i, str(int(num) if type(num) == float and num.is_integer() else num))
                current_number.clear()
                i += 1

            if len(words[i]) <= 2 or words[i] in get_stop_words('en'):
                words.pop(i)
                continue

            i += 1
    else:
        if current_number:
            words.append(str(word_to_num(' '.join(current_number))))

    return ''.join(x for x in ' '.join(words) if x.isalnum() or x == ' ')
