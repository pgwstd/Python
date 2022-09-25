import jieba
# 加载系统词典
jieba.set_dictionary('./data/dict.txt.big')

print('自定义词典内容:')
with open('./data/user_dict.utf8', 'r', encoding="utf-8") as f:
         for l in f:
             print(l)
sent = 'jieba分词非常好用，可以自定义金融词典!'
seg_list = jieba.cut(sent)
print('加载词典前:','/'.join(seg_list))

jieba.load_userdict('./data/user_dict.utf8')
seg_list = jieba.cut(sent)
print('加载词典后:','/'.join(seg_list))