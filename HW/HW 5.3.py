# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

import string

text = "Should, I. subscribe? Yes!"

text = text.title()

for symbol in string.punctuation:
    text = text.replace(symbol, "")

text = text.replace(" ", "")

text = "#" + text
text = text[:140]

print(text)