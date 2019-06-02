
lexicon = {
    'north': 'direction',
    'south': 'direction',
    'west': 'direction',
    'east': 'direction',
    'up': 'direction',
    'down': 'direction',
    'left': 'direction',
    'right': 'direction',
    'back': 'direction',
    'eat': 'verb',
    'kill': 'verb',
    'go': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'bear': 'noun',
    'princess': 'noun',
}

def scan(sentence):
    result = []
    words = sentence.split()

    for word in words:
        word_type = lexicon.get(word, 'error')
        if word_type == "error":
            value = convert_number(word)
            if value:
                word_type = 'number'
                result.append((word_type, value))
                continue
        result.append((word_type, word))

    return result

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
