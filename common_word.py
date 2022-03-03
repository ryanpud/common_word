#opens file
fname = input("Enter a File Name: ")
fhan = open(fname)
word_list = list()
word_dict = dict()


#this splits the file into individual lines then appends each line into word_list
for lines in fhan:
    lines.rstrip()
    lines = lines.split()
    for words in lines:
        word_list.append(words)

#this counts each word in the specific file to determine the total count
for each_word in word_list:
    if each_word in word_dict:
        word_dict[each_word] = word_dict[each_word] + 1
    else:
        word_dict[each_word] = 1

#this finds the biggest number and pastes the number
final_word = None
final_number = None
for each_word, word_dict in word_dict.items():
    if final_number is None or word_dict > final_number:
        final_number = word_dict
        final_word = each_word
print(final_word, final_number)
        