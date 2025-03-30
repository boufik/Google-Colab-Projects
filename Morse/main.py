# RULES
# 1. The length of a dot (dit = .) is one unit
# 2. A dash (dah = -) is three units
# 3. The space between parts of the same letter is one unit (= dit)
# 4. The space between letters is three units (= dah)
# 5. The space between words is seven units.
# dit = .
# dah = -

# 1. LIBRARY
import winsound
import time
freq = 1000
dit = 500
dah = 3 * dit

# 2. AUXILIARY FUNCTIONS
def translate(initial_words):
    print(f"\n{50 * "~"}\n\tMessage = {initial_words}\n")
    words = initial_words
    words = words.lower()
    words = words.split()
    STR = ""
    for counter, word in enumerate(words):
        for letter in word:
            print(f"{letter} = ", end="")
            expr = d[letter]
            LEN = len(expr)
            for i, symbol in enumerate(expr):
                STR += symbol
                duration = dit if symbol == "." else dah
                winsound.Beep(freq, duration)
                print(symbol, end="")
                if i != LEN - 1:        # Not the last symbol ---> Pause sound for 1 dit (rule 3)
                    time.sleep(dit/ 1000)
            # Current letter's process is OK - New letter incoming ---> Pause sound for 3 dits (rule 4)
            STR += " "
            print()
            time.sleep(3 * dit / 1000)
        # Current word's process is OK - New word incoming ---> Pause sound for 7 dits (rule 5)
        if counter != len(words) - 1:
            time.sleep(7 * dit / 1000)
            STR += 4 * " "
            print("\n")
    print(f"\n{initial_words} = {STR}")
    print(f"{50 * "~"}")

# 3. GLOBAL VARIABLES
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
keys = [elem for elem in alphabet]
values1 = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
values2 = [".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"]
values = values1 + values2
d = dict(zip(keys, values))


# 4. MAIN FUNCTION
initial_words = "Hey Thomas"
translate(initial_words)
