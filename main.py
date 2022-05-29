import math
import os
from collections import Counter


# Problem_1:
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))


# Problem_2:
def remove_duplicates(numbers):
    return list(set(numbers))


# Problem_3:
def divide_string(str1, str2=''):
    split_location1 = math.ceil(len(str1) / 2)
    split_location2 = math.ceil(len(str2) / 2)
    if str1 and str2:
        return (str1[:split_location1] +
                str2[:split_location2] +
                ' ' +
                str1[split_location1:len(str1)] +
                str2[split_location2:len(str2)])
    else:
        return str1[:split_location1] + ' ' + str1[split_location1:len(str1)]


# Problem_4:
def find_common_words():
    file_path = input("Please, Enter file path: ")
    if os.path.exists(file_path):
        words_file = open(file_path).read().split()
        words_counter = [key for key, value in Counter(words_file).most_common(20)]
        # print(words_counter)
        common_words_file = open('popular_words.txt', 'w')
        common_words_file.write('\n'.join(words_counter))
        common_words_file.close()
    else:
        print("File does not exist!!")


# Problem_5:
def remove_vowels(word):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in word if char not in vowels])


# Problem_6:
def find_char_location(word, letter):
    return [index for index, char in enumerate(word.lower()) if letter.lower() == char]


# Problem_1 trial
print(calculate_distance(1, 1, 2, 2))
# Problem_2 trial
print(remove_duplicates([1, 2, 1, 2, 4, 8, 2]))
# Problem_3 trial
print(divide_string('Ahmed', 'Nada'))
print(divide_string('Ramez'))
# problem_5 trial
print(remove_vowels('Juventus'))
# Problem_6 trial
print(find_char_location('Juventus is my favourite football team', 'e'))
# problem_4 trial
find_common_words()
