from itertools import permutations,chain
def generate_words(sequence):
    perms=chain.from_iterable(permutations(sequence,lenght) for lenght in range(1,len(sequence)+1))
    sorted_words=sorted([''.join(word) for word in set(perms)],key=len)
    return sorted_words


input_sequence=input("Введите слова: ")
result_words=generate_words(input_sequence)
for word in result_words:
    print(word)





