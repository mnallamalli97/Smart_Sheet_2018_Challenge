import itertools  
from collections import defaultdict


def minimize(string):

    word_count = 0
    data_dict = {}
    word_first_char = -1
    result = string
    result_offset = 0
    i = 0

    #to ensure the last character is read, add an extra space at the end of the string so last char is read
    string += ' '

    #reading the string char by char 
    while i < len(string):
        #if the char is not an alphabet, store the chars into a word variable and add the word to the dictionary along with the index
        if not string[i].isalpha():
            if word_first_char != -1:
                word = string[word_first_char:i]
                if word not in data_dict:
                    data_dict[word] = word_count
                else:
                    #if there is a duplicate word, then add the $index as a replacement. 
                    result = result[:word_first_char-result_offset] + "$" + str(data_dict[word]) + result[i-result_offset:]
                    result_offset = result_offset + len(word)-1-len(str(data_dict[word]))
                word_count += 1
                word_first_char = -1
            #print("result", result)
        #if it is an alphabet, set the lower bound of the word to be the first index, and the last 
        else:
            if word_first_char == -1:
                word_first_char = i
        i = i+1

    return result




def main():
    print(minimize("you say yes, I say no you say stop and I say go go go"))



if  __name__ =='__main__':
    main()
