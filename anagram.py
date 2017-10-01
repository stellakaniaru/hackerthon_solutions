from collections import Counter

a = 'Anagram'
b = 'magrana'

word1 = input().strip().lower()
word2 = input().strip().lower()
dict_1 = Counter(word1)
dict_2 = Counter(word2)
comp = dict_1 == dict_2

if comp == True:
	print('Anagrams')
else:
	print('Not Anagrams')
