# with open("shortjokes.csv") as f:
#     content = f.readlines()
# content = [x.strip() for x in content]
# index = 0
# prePos = 0
# for i in content:
#     index = index + 1
#     prePos = (index/10)+2
#     if 'my' in i:
#         line = i[int(prePos):]
#         print(prePos)

with open("shortjokes.csv") as f:
    content = f.readlines()
    line = [x.strip() for x in content]
    line = line.split(',', 2)
    newLine = line[1].strip()
    newLine = re.sub(r'[^a-zA-Z\0\s]', '', newLine)
    newLine = newLine.lower()
    words = newLine.split()
    # increase counters
    for word in words:
        if word:
            if words.index(word) + 1 < len(words):
                two_words = (words[words.index(word) + 1])
                thetup = word + " " + two_words
                if word.isalpha():
                    print(thetup, 1)