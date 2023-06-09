import math
import jieba
import bm25utils
import matplotlib.pyplot as plt

text = '''
自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，
所以它与语言学的研究有着密切的联系，但又有重要的区别。
自然语言处理并不是一般地研究自然语言，
而在于研制能有效地实现自然语言通信的计算机系统，
特别是其中的软件系统。因而它是计算机科学的一部分。
'''
class BM25(object):
    def __init__(self, docs):
        self.D = len(docs)    # 记录文档的平均长度
        self.avgdl = sum([len(doc)+0.0 for doc in docs]) / self.D
        self.docs = docs    # 列表的每一个元素是一个dict，dict存储着一个文档中每个词的出现次数
        self.f = []    # 存储每个词及出现了该词的文档数量，也是一个字典结构
        self.df = {}
        self.idf = {}       # 存储每个词的idf值
        self.k1 = 1.5       # 设置参数值
        self.b = 0.75
        self.init()

    def init(self):
        for doc in self.docs:
            tmp = {}             # 字典
            for word in doc:
                tmp[word] = tmp.get(word, 0) + 1 # 0表示当所查找的单词不存在时，返回默认值0，存储每个文档中每个词的出现次数
            self.f.append(tmp)
            for k in tmp.keys():
                self.df[k] = self.df.get(k, 0) + 1        # 计算每个词出现该词的文档数量
        for k, v in self.df.items():
            self.idf[k] = math.log(self.D-v+0.5)-math.log(v+0.5)
#计算每个语素的权重
    def sim(self, doc, index):    # 计算Query
        score = 0
        for word in doc:
            if word not in self.f[index]: # 如果该单词没有在该文档中出现过
                continue
            d = len(self.docs[index]) # d为第index个文档的长度
            score += (self.idf[word]*self.f[index][word]*(self.k1+1) / (self.f[index][word]+self.k1*(1-self.b+self.b*d/self.avgdl)))
        return score

    def simall(self, doc):   # 计算Query分别对每个文档的相关性
        scores = []
        for index in range(self.D):
            score = self.sim(doc, index)  # 计算Query对第index个文档的相关性
            scores.append(score)
        return scores

if __name__ == '__main__':
    sents = bm25utils.get_sentences(text)
    doc = []
    for sent in sents:
        words = list(jieba.cut(sent)) # 实现分词操作
        words = bm25utils.filter_stop(words)         # 过滤掉停用词
        doc.append(words)
    s = BM25(doc)  # 得到一个新的对象
    print(s.f)
    print(s.idf)
    print(s.D)
    num_list = s.simall(['日常', '重要', '方向', '研究', '语言'])
    print(num_list)
    name_list = ["doc1", 'doc2', 'doc3', 'doc4', 'doc5', 'doc6', 'doc7', 'doc8', 'doc9', 'doc10', 'doc11', 'doc12']
    plt.bar(range(len(num_list)), num_list, color=['r','g','b'],tick_label=name_list)
    plt.ylabel("Score(Q,doc)")

    plt.show()