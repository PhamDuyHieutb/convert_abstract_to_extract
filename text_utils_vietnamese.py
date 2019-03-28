from pyvi import ViTokenizer
import nltk
import re

SPECICAL_CHARACTER = {'(', ')', '[', ']', ',', '"', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


def text_process_vietnamese(sentences):
    new_sentences = []

    for item in sentences:
        tmp = re.sub('[<>@~:.;*]', '', item)
        tmp = re.sub('-', ' ', tmp)
        tmp = re.sub('[“”]', '"', tmp)
        text_tmp = []
        token_sent = ViTokenizer.tokenize(tmp).lower()
        for word in token_sent.split(' '):
            if len(word) != 1 or word in SPECICAL_CHARACTER:
                text_tmp.append(word)
        if len(text_tmp) > 5:
            new_sentences.append(' '.join(text_tmp).strip())

    return new_sentences


def split_sentences(file_name):
    try:
        with open(file_name, 'r') as file:
            text_system = file.read()

        sentence_token = nltk.data.load('tokenizers/punkt/english.pickle')
        tmp = sentence_token.tokenize(text_system)
        sentences = []
        for item in tmp:
            if "…" in item:
                b = item.split("…")
                for i in b:
                    sentences.append(i)
            elif '... ' in item:
                b = item.split('... ')
                for i in b:
                    sentences.append(i)
            else:
                sentences.append(item)
        preprocess_sents = text_process_vietnamese(sentences)

        return preprocess_sents

    except Exception:
        print(file_name)


def get_all_sentences(file_system, file_reference):
    sentences_origin_system = []
    for item in file_system:
        sentences_origin_system.append((item, split_sentences(item)))

    sentences_reference = []
    for item in file_reference:
        with open(item, 'r') as file:
            sentences_ref = text_process_vietnamese(nltk.sent_tokenize(file.read()))
            sentences_reference.append('. '.join(sentences_ref))

    return sentences_origin_system, sentences_reference