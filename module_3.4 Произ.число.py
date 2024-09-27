def single_root_words(root_word, *other_words):    # Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words
    same_words = []       #Создайте внутри функции пустой список same_words
    words = list(other_words) # list - упорядоченная и изменяемая коллекция элементов

    for i in range(len(words)):  #При помощи цикла for переберите предполагаемо подходящие слова (range — создаёт последовательность), len - Определение длины строки
        if root_word.lower() in words[i].lower() or words[i].lower() in root_word.lower():
            same_words.append(words[i]) 
    return (same_words)  # return() завершает вызов функции




result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)