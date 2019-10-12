
import matplotlib.pyplot as plt

open_file = open("frequency.txt", "r").read()

dict1 = eval(open_file)

dict_word={} 
dict_tag={}


for key in dict1:
	words=key.split('_') 
	if(len(words) != 2):
		continue
	if words[0] in dict_word :
	    dict_word[words[0]]=dict_word[words[0]]+dict1[key]
	else :
	    dict_word[words[0]]=dict1[key]

	if words[1] in dict_tag :
	    dict_tag[words[1]]=dict_tag[words[1]]+dict1[key]
	else :
	    dict_tag[words[1]]=dict1[key]

sorted_words = sorted(dict_word.items(), key=lambda a : a[1])
sorted_tag = sorted(dict_tag.items(), key=lambda a : a[1])

sorted_words.reverse()
sorted_tag.reverse()

len_words = len(sorted_words)
len_tag = len(sorted_tag)

print(len_words) # 192632
print(len_tag) # 87

write_file = open("top10.txt", "w")

write_file.write("TOP 10 words based on frequency\n")
for i in range(0,10):
	write_file.write(str(sorted_words[i]))

write_file.write("\n\n\n")

write_file.write("TOP 10 tags based on frequency\n")
for i in range(0,10): # min(10,len_tag)
	write_file.write(str(sorted_tag[i]))

# print(len_tag)
# print(len_words)

# plt.bar(dict_tag.keys(), dict_tag.values())
# plt.show()

ten_words = []
ten_freqs_words = []

for i in range(0,10):
	ten_freqs_words.append(sorted_words[i][1])
	ten_words.append(sorted_words[i][0])

plt.bar(ten_words, ten_freqs_words)
plt.show()

ten_tags = []
ten_freqs_tags = []

for i in range(0,10):
	ten_freqs_tags.append(sorted_tag[i][1])
	ten_tags.append(sorted_tag[i][0])

plt.bar(ten_tags, ten_freqs_tags)
plt.show()


#---------------------------------------------------------- WEEK 4 ----------------------------------------------------------

words_prob = dict()
len_word_tag = len(dict1)
arr_tags = dict_tag.keys() 
for key,val in dict_word.items() :
	word_dict = dict()
	for tag in arr_tags:
		w_t = key + "_" + tag
		word_count = val
		try:
			word_tag_count = dict1[w_t]
		except KeyError:
			word_tag_count = 0
		word_dict[tag] = word_tag_count/word_count
	words_prob[key] = word_dict
	# print(word_dict)

# write_prob = open("word_probability.txt", "w")
# dict_size = len(words_prob)
# print(dict_size)

words_in_one_file = dict_size/500
index = 0
fno = 0
dic = dict()

prob_folder = "word_probability/"

prob_file = open(prob_folder+"words_prob" + str(fno), "w")
for key in words_prob:
    if(index > words_in_one_file):
        index = 0
        prob_file.write(str(dic))
        prob_file.close()
        fno = fno + 1
        prob_file = open(prob_folder+"words_prob" + str(fno), "w")
        dic = dict()
    dic[key] = words_prob[key]
    index = index + 1
prob_file.close()
if(len(dic) > 0):
    prob_file = open(prob_folder+"words_prob" + str(fno), "w")
    prob_file.write(str(dic))
    prob_file.close()


