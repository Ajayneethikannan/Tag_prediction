import os
   #  	word = ""
   #  	tag = ""
   #  	for ch in words:
			# if(ch!='_' and check==False):
			# 	word.join(ch)
			# elif(ch=='_'):
			# 	check=True
			# elif(check):
			# 	tag.join(ch)
   #  	print(words)
   #  	modify(words, word, tag)
    	#print(word+" "+tag+"\n")
       #	print(word)

train_dict = {}
files = os.listdir('Train-corpus/Cleaned_files/')
directory = 'Train-corpus/Cleaned_files/'
# print(len(files)) = 520
for filename in files:
	file = open(directory+filename)
	for line in file:
	    for words in line.split():
	    	if words in train_dict :
	    		train_dict[words]=train_dict[words]+1
	    	else :
	    		train_dict[words]=1
	file.close()

length=len(train_dict) # 255506
print(length)

write_file = open("frequency.txt", "w+")
write_file.write(str(train_dict))
write_file.close() 

#print(length)
# for i in train_dict:
# 	print(i+" "+str(train_dict[i]))
#for i in range(31):
#	file = open("cleanTrain" + str(i) + ".txt")
#	for words in file:
#		word = "" 
#		tag = ""
#		modify(words, word, tag)
#		print(word+" "+tag+"\n")