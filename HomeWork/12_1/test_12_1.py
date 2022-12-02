import jieba

excludes = {"一个", "那里", "怎么", "我们", "不知",  "妖精", "菩萨", "师父", "和尚"}
txt = open("西游记.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "行者" or word == "大圣":
        rword = "孙悟空"
    elif word == "八戒" or word == "天蓬元帅":
        rword = "猪八戒"
    elif word == "悟净" or word == "沙僧":
        rword = "沙悟净"
    elif word == "贫僧" or word == "三藏":
        rword = "唐僧"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del (counts[word])
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(4):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
