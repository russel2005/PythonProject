import secrets


def generate_pass(num_words):
    with open('diceware.wordlist.asc', 'r') as file:
        lines = file.readlines()[2:7778]
        word_list = [lines.split()[1] for lines in lines]

    words = [secrets.choice(word_list) for i in range(num_words)]
    return ' '.join(words)

