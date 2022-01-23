def convert(number):
    return get_to_words(number, len(number))


def get_to_words(number, count):
    NUM_WORDS = ['TY', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

    NUM_EXCEPTION = ["", 'ONE', 'TWO', 'THIR', 'FOUR', 'FIF', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

    EXCEPTIONS = ['ELEVEN', 'TWELVE', 'TWENTY']

    TEEN = 'TEEN'

    TEN = 'TEN'

    HUNDRED = 'HUNDRED'

    THOUSAND = 'THOUSAND'

    LAKHS = 'LAKHS'

    # place valued ones
    if count == 1:
        return NUM_WORDS[eval(number)]

    # place valued tens
    elif count == 2:
        if number[0] == "0":
            return get_to_words(number[1:], count - 1)
        elif number[0] == "1":
            if number[1] == "0":
                return TEN
            elif number[1] == "1":
                return EXCEPTIONS[0]
            elif number[1] == "2":
                return EXCEPTIONS[1]
            else:
                return NUM_EXCEPTION[eval(number[1])] + TEEN
        elif number[0] == "2":
            if number[1] == "0":
                return EXCEPTIONS[2]
            else:
                return EXCEPTIONS[2] + " " + NUM_WORDS[eval(number[1])]
        else:
            if number[1] == "0":
                return NUM_EXCEPTION[eval(number[0])] + NUM_WORDS[eval(number[1])]
            else:
                return NUM_EXCEPTION[eval(number[0])] + NUM_WORDS[0] + " " + NUM_WORDS[eval(number[1])]

    # place valued hundreds
    elif count == 3:
        if [x for x in number[1:]] == ['0'] * (count - 1):
            return NUM_WORDS[eval(number[0])] + " " + HUNDRED
        elif number[0] == "0":
            return get_to_words(number[1:], count-1)
        return NUM_WORDS[eval(number[0])] + " " + HUNDRED + " AND " + get_to_words(number[1:], 2)

    # place valued thousands
    elif count == 4:
        if [x for x in number[1:]] == ['0'] * (count - 1):
            return NUM_WORDS[eval(number[0])] + " " + THOUSAND
        elif number[0] == "0":
            return get_to_words(number[1:], count-1)
        return NUM_WORDS[eval(number[0])] + " " + THOUSAND + " " + get_to_words(number[1:], 3)

    # place valued ten thousands
    elif count == 5:
        if [x for x in number[1:]] == ['0'] * (count - 1):
            return get_to_words(number[:2], 2) + " " + THOUSAND
        elif number[0] == "0":
            return get_to_words(number[1:], count-1)
        return get_to_words(number[:2], 2) + " " + THOUSAND + " " + get_to_words(number[2:], 3)

    # place valued lakhs
    elif count == 6:
        if [x for x in number[1:]] == ['0'] * (count - 1):
            return NUM_WORDS[eval(number[0])] + " " + LAKHS
        elif number[0] == "0":
            return get_to_words(number[1:], count-1)
        return NUM_WORDS[eval(number[0])] + " " + LAKHS + " " + get_to_words(number[1:], 5)

    # place valued ten lakhs
    elif count == 7:
        if [x for x in number[1:]] == ['0'] * (count - 1):
            return get_to_words(number[:2], 2) + " " + LAKHS
        elif number[0] == "0":
            return get_to_words(number[1:], count-1)
        return get_to_words(number[:2], 2) + " " + LAKHS + " " + get_to_words(number[2:], 5)

    # place valued crores
    elif count == 8:
        if [x for x in number[1:]] == ['0'] * (count - 1):
            return NUM_WORDS[eval(number[0])] + " CRORES "
        elif number[0] == "0":
            return get_to_words(number[1:], count-1)
        return NUM_WORDS[eval(number[0])] + " CRORES " + get_to_words(number[1:], 7)

    # place valued ten crores
    elif count == 9:
        if [x for x in number[1:]] == ['0'] * (count - 1):
            return get_to_words(number[:2], 2) + " CRORES "
        elif number[0] == "0":
            return get_to_words(number[1:], count-1)
        return get_to_words(number[:2], 2) + " CRORES " + get_to_words(number[2:], 7)


if __name__ == '__main__':
    print(convert('100000001'))
