from dictogram import Dictogram
import random


def make_markov_model(data):
    markov_model = dict()

    for i in range(len(data) - 1):
        if data[i] in markov_model:
            markov_model[data[i]].update([data[i + 1]])
        else:
            markov_model[data[i]] = Dictogram([data[i + 1]])
    return markov_model


def make_higher_order_markov_model(order, data):
    markov_model = dict()

    for i in range(len(data) - order):
        window = tuple(data[i: i + order])

        if window in markov_model:
            markov_model[window].update([data[i + order]])
        else:
            markov_model[window] = Dictogram([data[i + order]])
    return markov_model


def generate_random_start(model):
    if 'END' in model:
        seed_word = 'END'
        while seed_word == 'END':
            seed_word = model['END'].return_weighted_random_word()
        return seed_word
    return random.choice(model.keys())


def generate_random_sentence(length, markov_model):
    current_word = generate_random_start(markov_model)
    sentence = [current_word]
    for i in range(length):
        current_dictogram = markov_model[current_word]
        rand_weighted_word = current_dictogram.return_weighted_random_word()
        current_word = rand_weighted_word
        sentence.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'

