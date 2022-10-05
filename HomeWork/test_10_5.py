from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == "__main__":
    corpus = ["我 来到 北京 清华大学",  # 第一个文本切词后的结果，词之间以空格隔开
              "他 来到 了 网易 杭研 大厦",  # 第二个文本的切词结果
              "小明 硕士 毕业 与 中国 科学院",  # 第三个文本的切词结果
              "我 爱 北京 天安门"]  # 第四个文本的切词结果
    def cut(sentence):
        return sentence.split(" ")
    vectorizer = CountVectorizer(analyzer="word", tokenizer=cut)  # 将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i个文本下的词频
    transformer = TfidfTransformer()  # 统计每个词语的tf-idf权值
    X = vectorizer.fit_transform(corpus)
    tfidf = transformer.fit_transform(X)  # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    word = vectorizer.get_feature_names_out()  # 获取词袋模型中的所有词语

    weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i个文本中的tf-idf权重
    for i in range(len(weight)):  # 打印每个文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一个文本下的词语权重
        print("-------这里输出第", i, u"个文本的词语tf-idf权重------")
        for j in range(len(word)):
            print(word[j], weight[i][j])

    print("1.---------------------")
    print(word)
    print("2.---------------------")
    k = vectorizer.vocabulary_
    print(k)
    print("3.---------------------")
    print(X.toarray())
    print("4.---------------------")
    print(X)