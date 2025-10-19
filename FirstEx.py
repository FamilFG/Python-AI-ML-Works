# 1 exercise
# def reverse_list(lst):
#     if len(lst)<=1:
#         return lst
    
#     return reverse_list(lst[1:]) + [lst[0]]

# lst = [1,2,3,4,5]
# print(reverse_list(lst))

#2 exercise
# grades = {
#     "Alice": [85, 90, 78],
#     "Bob": [72, 88, 91],
#     "Charlie": [90, 92, 85]
# }

# avg = {}  

# for name in grades: 
#     scores = grades[name]               
#     average = sum(scores) / 3
#     avg[name] = round(average,2)                 

# print(avg)

# list = []
# for names in avg:
#     list.append(int(avg[names]))
# print(max(list))


#3 exercise
# listof = {}
# lst = [5,1,7,8]
# def count_elements(lst):
#     for i in range(0,len(lst)):
#         listof[f'{i}'] = lst[i]

# count_elements(lst)
# print(listof)

#6 exercise
# def prime_factors(n):
#     factors = []
#     d = 2

#     while n > 1:
#         while n % d == 0:
#             factors.append(d)
#             n //= d
#         d += 1

#     return factors


#7 exericse
# def remove_duplicates_preserve_order(lst):
#     seen_objects = set()
#     result = []
#     for item in lst:
#         if item not in seen_objects:
#             seen_objects.add(item)
#             result.append(item)
#     return result


# nums = [3, 1, 2, 3, 2, 4, 1, 5]
# print(remove_duplicates_preserve_order(nums))


#5 exercise

# def is_palindrome(word):
#     word = list(word)
#     if len(word)<=1:
#          return word
    
#     return is_palindrome(word[1:]) + [word[0]]

# thestring = "faaf"
# print(is_palindrome(thestring)==list(thestring))

#4 exercise


def word_statistics(text):

    for ch in [".", "!", "?", ","]:
        text = text.replace(ch, "")
    words = text.lower().split()
    #turn the sentence to words

    word_freq = {}
    for i in words:
        word_freq[i] = word_freq.get(i, 0) + 1
        #counting word frequencies

    un_words = []
    for j in word_freq:
        un_words.append(j)
    un_words = tuple(un_words)
    unwordscount = len(un_words)
    #tuple with unique words
    
    sortedlist = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
    top3 = []
    for i in range(3):
        top3.append(sortedlist[i][0])


    print(unwordscount, word_freq, top3)


    




text = "Data is the new oil. Data drives the world. Oil is limited."
word_statistics(text)