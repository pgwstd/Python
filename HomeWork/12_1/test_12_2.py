import jieba
excludes = {"却说", "西天", "取经", "不可", "妖怪"}
txt = open("西游记.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "悟空" or word == "齐天大圣":
        rword = "孙悟空"
    elif word == "八戒" or word == "悟能":
        rword = "猪八戒"
    elif word == "沙和尚" or word == "悟净":
        rword = "孙悟空"
    elif word == "贫僧" or word == "唐僧":
        rword = "唐三藏"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del (counts[word])
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(5):
    word, count = items[i]
    print("{0:<10}{1:5}".format(word, count))
