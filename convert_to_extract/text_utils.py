from pyvi import ViTokenizer
import nltk


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
            else:
                sentences.append(item)

        return sentences

    except Exception:
        print(file_name)


# def get_all_sentences(file_system, file_reference):
#     sentences_origin_system = []
#     for item in file_system:
#         sentences_origin_system.append((item, split_sentences(item)))
#
#     sentences_system = []  # be token words
#     for filename, list_sent_origin in sentences_origin_system:
#         sent_in_clus = []
#         for item in list_sent_origin:
#             sent_in_clus.append(ViTokenizer.tokenize(item))
#         sentences_system.append((filename, sent_in_clus))
#
#
#     sentences_origin_reference = []
#     for item in file_reference:
#         with open(item, 'r') as file:
#             sentences_origin_reference.append(file.read())
#
#     sentences_reference = []
#     for item in sentences_origin_reference:
#         sentences_reference.append(ViTokenizer.tokenize(item))
#
#     return sentences_system, sentences_reference



def get_all_sentences(file_system, file_reference):
    sentences_origin_system = []
    for item in file_system:
        sentences_origin_system.append((item, split_sentences(item)))



    sentences_origin_reference = []
    for item in file_reference:
        with open(item, 'r') as file:
            sentences_origin_reference.append(file.read())
    sentences_reference = []
    for item in sentences_origin_reference:
        sentences_reference.append(item)

    return sentences_origin_system, sentences_reference

