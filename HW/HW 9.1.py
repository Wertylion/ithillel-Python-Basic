def popular_words (text, words):
    text1 = text.lower()
    text1 = text1.split()
    words1 = {}
    for word in words:
        words1[word] = text1.count(word)
    return words1


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

# text = "When I was One I had just begun When I was Two I was nearly new"
# words = ['i', 'was', 'three', 'near']
# text1 = text.lower()
# text1 = text1.split()
# words1 = {}
# for word in words:
#     words1[word] = text1.count(word)
# print(words1)






