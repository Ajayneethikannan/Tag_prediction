from bs4 import BeautifulSoup
import os

access_directory = os.listdir("Train-corpus/")

write_directory = "Train-corpus/Cleaned_files/"

# print(access_directory)

i=0
for ele in access_directory:
	access_directory[i]="Train-corpus/"+ele+"/"
	i=i+1

os.mkdir(write_directory)

# print(access_directory)
# print('\n')
# print(write_directory)

for dirs in access_directory:
	files = os.listdir(dirs)
	for file in files:
		write_file = open(write_directory+file.split('.')[0]+".txt", "w+")
		filename = open(dirs+file)
		content = BeautifulSoup(filename, features="lxml")
		sent_arr = content.find_all("s")
		for sentence in sent_arr:
			for word in sentence.find_all("w"):
				text = word.get_text().strip()
				tag = word.get('c5')
				write_file.write(text + "_" + tag + " ")
		filename.close()
		write_file.close()


# index_arr = []
# for i in range(26):
#     index_arr.append(chr(65+i))
# for i in range(5):
#     index_arr.append(str(1+i))
# base = "A0"
# j = 0
# for index in index_arr:
#     write_file = open("cleanTrain" + str(j) + ".txt", "w+")
#     j = j+1
#     filename = base + index
#     file = open(filename + ".xml")
#     content = BeautifulSoup(file, features="lxml")
#     sent_arr = content.find_all("s")
#     for sentence in sent_arr:
#         for word in sentence.find_all("w"):
#             text = word.get_text().strip()
#             tag = word.get('pos')
#             write_file.write(text + "_" + tag + " ")
#     file.close()
#     write_file.close()