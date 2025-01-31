def caesarShift(txt, shift) -> str:
    shifted_word = []
    for letter in txt:
        # Get the position of the letter
        new_pos = (ord(letter) - ord('a') + shift) % 26
        new_letter = chr(new_pos + ord('a'))
        shifted_word.append(new_letter)
    return ''.join(shifted_word)


if __name__ == "__main__":
    #This is the test code
    txt = input()
    shift = int(input())
    print(caesarShift(txt, shift))

    assert caesarShift('example', 1) == 'fybnqmf', 'failed test case 1'
    assert caesarShift('example', -1) == 'dwzlokd', 'failed test case 2'
    assert caesarShift('python', 2) == 'ravjqp', "failed test case 3"
    assert caesarShift('pecan', 4) == 'tiger', "failed test case 4"