import os
import re
import codecs

stop_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'stopwords.txt')
# 连接两个文件名地址
stop = set()
fr = codecs.open(stop_path, 'r', 'utf-8-sig')
for word in fr:
    stop.add(word.strip())
fr.close()
re_zh = re.compile('([\u4E00-\u9FA5]+)')

def filter_stop(words):
# 过滤掉停用词
    return list(filter(lambda x: x not in stop, words))

def get_sentences(doc):
# 用来得到文档
    line_break = re.compile('[\r\n]')
    delimiter = re.compile('[，。？！；]')
# 划分文档
    sentences = []
    for line in line_break.split(doc):
        line = line.strip()
        if not line:
            continue
        for sent in delimiter.split(line):
            sent = sent.strip()
            if not sent:
                continue
            sentences.append(sent)
    return sentences