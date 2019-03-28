from rouge_vn import pyrouge_vn
import text_utils_vietnamese
import os
import shutil
import re
import time

DIR_PATH = '/home/hieupd/PycharmProjects/convert_to_extract/baomoi/documents'


class ConvertExtract(object):
    def __init__(self, alpha=0.5):
        self.alpha = alpha

    def convert_extract(self, list_documents, list_human, path_save):
        sentences_system, sentences_reference = \
            text_utils_vietnamese.get_all_sentences(list_documents, list_human)
        old_rouge = 0
        rouge = 0  # initial rouge score
        old_index = -1

        sentences = []  # arr sentence is choosed
        sentences_label = []
        arr_indexes = []
        all_sentences = []

        for filename, list_sents in sentences_system:
            all_sentences += list_sents
            # with each round with add new sentence
        while (0 == 0):
            i = 0

            for sent in all_sentences:
                tmp = ""
                tmp += ' '.join(sentences)
                tmp += ' ' + sent

                # Use rouge 1
                tmp_rouge_f1 = pyrouge_vn.rouge_1(tmp, sentences_reference, self.alpha)

                if tmp_rouge_f1 > rouge:  # if has change score
                    rouge = tmp_rouge_f1
                    old_index = i

                i += 1

            if rouge == old_rouge:
                break
            else:
                arr_indexes.append(old_index)
                old_rouge = rouge
                sentences.append(all_sentences[old_index])
                old_index = -1

        # for item in sentences_origin:
        #     with open(path_save, 'a') as file:
        #         file.write(item)

        for i in range(len(all_sentences)):
            if i in arr_indexes:
                sentences_label.append( '1' + ' ' + all_sentences[i])
            else:
                sentences_label.append('0' + ' ' + all_sentences[i])
        length = 0
        sentences_label_clus = []
        for clus, list_sentences in sentences_system:
            l = len(list_sentences)
            number_sents = len(list_sentences)
            sentences_label_clus.append((clus, sentences_label[length:number_sents + length]))
            length += l

        for path_file, data in sentences_label_clus:
            with open(path_save, 'w') as file:
                file.write('\n'.join(data))
                file.close()

        return rouge

if __name__ == "__main__":
    convert_extract = ConvertExtract()
    root = os.getcwd()
    ABSTRACT = root + '/baomoi/summaries/'
    OUTPUT_LABELS = root + '/baomoi/data_labels/'

    list_doc_filtered = open('baomoi/list_doc_fitlers').read().strip().split('\n')

    #list_doc_filtered = list_doc_filtered[:100]

    rouges = []

    c = 0
    for file in list_doc_filtered:
        c += 1
        if c in [100, 500, 1000, 1200, 2000]:
            print(c)

        path_raw = file.split('/')[-2:]
        path = '/'.join(path_raw)
        path_human = ABSTRACT + path
        #print(path)

        rouges.append(convert_extract.convert_extract([file], [path_human],
                                        OUTPUT_LABELS + path_raw[1]))


    count = []
    for i in rouges:
        if i > 0.45:
            count.append(i)

    # print(sum(rouges)/ len((rouges)))

    print(len(count))
    print(sum(count) / len((count)))