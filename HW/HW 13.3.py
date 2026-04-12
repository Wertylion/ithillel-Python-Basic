def song_words(songtext):
    with open(songtext, 'r', encoding='utf-8') as file:
        text = file.read()

    badwords = ["devil","Fuckkkkkk"]
    for bad in badwords:
        text = text.replace(bad,"*")

    words = text.split()
    words7plus = []


    for word in words:
        if len(word) > 7:
            words7plus.append(word)

    return words7plus

result = song_words('songtext.txt')

with open('result.txt', 'w', encoding='utf-8') as file:
    for word in result:
        file.write(word + '\n')
count = len(result)
print(count)

