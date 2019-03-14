import os
import nltk


print(' '.join(nltk.word_tokenize("He said 'Gilliam' - also told the informant someone should kill the FBI sniper who killed the wife of white supremacist Randy weaver during an 11-day standoff in 1992 at Ruby Ridge, Idaho, along with civil rights lawyer Morris Dees of the Montgomery-based Southern Poverty Law Center.")))


#
# DIR_OLD = '/home/hieupd/PycharmProjects/convert_to_extract/Human/'
# DIR_NEW = '/home/hieupd/PycharmProjects/convert_to_extract/Human_New/'
# list_filename = os.listdir(DIR_OLD)
#
# for filename in list_filename:
#     number = filename.split(".")[0].split('_')[1]
#     if os.path.isdir(DIR_NEW + 'cluster_' + number):
#         os.rename(DIR_OLD + filename, DIR_NEW + 'cluster_' + number + '/' + filename)
#     else:
#         os.mkdir(DIR_NEW + 'cluster_' + number)
#         os.rename(DIR_OLD + filename, DIR_NEW + 'cluster_' + number + '/' + filename)
#
