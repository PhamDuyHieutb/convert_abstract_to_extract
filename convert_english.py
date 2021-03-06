from rouge_vn import pyrouge_vn
import text_utils_english
import os
import shutil
import re

DIR_PATH = '/home/hieupd/PycharmProjects/convert_to_extract/english'


class ConvertExtract(object):
    def __init__(self, alpha=0.5):
        self.alpha = alpha

    def convert_extract(self, list_documents, list_human, path_save):
        pass


    def convert_extract_with_indexes(self, list_documents, list_human, path_save):
        sentences_system, docs_reference = \
            text_utils_english.get_all_sentences(list_documents, list_human)

        old_rouge = 0
        rouge = 0  # initial rouge score
        old_index = -1

        sentences_selected = []  # arr sentence is choosed
        sentences_label = []
        arr_indexes = []
        all_sentences = []

        # add all list sentences of system to all_sentences in a cluster
        for filename, list_sents in sentences_system:
            all_sentences += list_sents

        # with each round with add new sentence
        while (0 == 0):
            i = 0

            for sent in all_sentences: # SELECT sentence which has best rouge, return index of this sentence
                tmp = ""
                for s in sentences_selected:
                    tmp += s

                tmp += sent

                # Use rouge 1
                tmp_rouge_f1 = pyrouge_vn.rouge_1(tmp, docs_reference, self.alpha)

                if tmp_rouge_f1 > rouge:  # if has change score
                    rouge = tmp_rouge_f1
                    old_index = i

                i += 1

            if rouge == old_rouge:
                break
            else:
                arr_indexes.append(old_index)
                old_rouge = rouge
                sentences_selected.append(all_sentences[old_index])
                old_index = -1


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

        os.mkdir(path_save)
        for path_file, data in sentences_label_clus:
            with open(path_save + '/' + path_file.split('/')[-1], 'w') as file:
                file.write('\n'.join(data))


if __name__ == "__main__":
    convert_extract = ConvertExtract()

    list_clusters = []
    dir_documents = DIR_PATH + '/DUC2007'
    for clus in os.listdir(dir_documents):
        list_clusters.append(dir_documents + '/' + clus)

    list_human_refs = []
    for clus in os.listdir(DIR_PATH + '/Human'):
        list_human_refs.append(DIR_PATH + '/Human/' + clus)

    for i in range(len(list_clusters)):
        list_docs_in_clus = []
        list_human_ref = []
        name_cluster = list_clusters[i]

        for filename in os.listdir(name_cluster):
            list_docs_in_clus.append(name_cluster + '/' + filename)
        name_clus = name_cluster.split('/')[-1]

        for ref in os.listdir(list_human_refs[i]):
            list_human_ref.append(list_human_refs[i] + '/' + ref)
        convert_extract.convert_extract(list_docs_in_clus, list_human_ref,
                                        DIR_PATH + "/convert_to_extract_indexes/" + name_clus)