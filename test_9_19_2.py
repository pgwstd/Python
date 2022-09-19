{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "样本之一：﻿有些死亡发生在“隐秘的角落”。2021年9月11日，全美各地不堪重负的医院里，呼吸机上被“德尔塔”株击垮的重症患者，艰难地吸入最后一口氧气，然后呼吸停止。对于前者，美国政府举办盛大的悼念仪式，发动复仇的战争机器。对后者，美国政府无动于衷，无人担责，把他们统计成数字。美国正展开另一个巨大的、让他们追悔莫及的错误。据霍普金斯大学数据，截至北京时间12日早6时许，过去的24小时内，美国新增死亡病例3362例，超过“9·11”事件的遇难人数。据同网站数据，9月10日，全美新增死亡更是达到4409例。美国疫情，每天一个“9·11”（ a new 9/11 every day）。——这是著名小报《芝加哥太阳时报》9月10日的评论标题。\n",
      "样本的分词效果：﻿/死亡/发生/隐秘/角落/2021/年/月/11/日/全美/各地/不堪重负/医院/里/呼吸机/德尔塔/株/击垮/重症/患者/艰难/吸入/最后/一口/氧气/呼吸/停止/美国政府/举办/盛大/悼念/仪式/发动/复仇/战争/机器/美国政府/无动于衷/无人/担责/统计/成/数字/美国/正/展开/一个/巨大/追悔莫及/错误/霍普金斯大学/数据/北京/时间/12/日早/时许/过去/24/小时/美国/新增/死亡/病例/3362/例/超过/·/11/事件/遇难/人数/据同/网站/数据/月/10/日/全美/新增/死亡/更是/达到/4409/例/美国/疫情/每天/一个/·/11/ / /new/ /11/ / /day/这是/著名/小报/芝加哥/太阳/时报/月/10/日/评论/标题\n",
      "样本的topk10词为：[(' ', 5), ('11', 4), ('死亡', 3), ('月', 3), ('日', 3), ('美国', 3), ('全美', 2), ('美国政府', 2), ('一个', 2), ('数据', 2)]\n"
     ]
    }
   ],
   "source": [
    "import glob\n",
    "import random\n",
    "import jieba\n",
    "\n",
    "def getContent(path):\n",
    "    with open(path, encoding='utf-8', errors='ignore') as f:\n",
    "        content = ''\n",
    "        for line in f:\n",
    "           #去除空行\n",
    "            line = line.strip()\n",
    "            content += line\n",
    "        return content\n",
    "    \n",
    "def get_TF(words, topK=10):\n",
    "    tf_dic = {}\n",
    "    #遍历words中的每个词，如果这个词在tf_dic中出现过，则令其加一。\n",
    "    for w in words:\n",
    "        tf_dic[w] = tf_dic.get(w, 0) + 1\n",
    "        #将字典tf_dic排序后取出前topK.\n",
    "    return sorted(tf_dic.items(), key = lambda x: x[1], reverse=True)[:topK]\n",
    "\n",
    "def stop_words(path):\n",
    "    with open(path,encoding='utf-8') as f:\n",
    "        return [l.strip() for l in f]\n",
    "    \n",
    "#修改cut函数,path是你的停用词表所放的位置\n",
    "def cut(content,path):\n",
    "    split_words = [x for x in jieba.cut(content) if x not in stop_words('./data/stop_words.utf8')]\n",
    "    return split_words \n",
    "\n",
    "\n",
    "def main():\n",
    "    files=glob.glob('./data/news/10.txt')\n",
    "    corpus=[getContent(x) for x in files]\n",
    "    sample_inx=random.randint(0,len(corpus))\n",
    "    split_words=cut(corpus[sample_inx],'./data/stop_words.utf8')\n",
    "    print('样本之一：'+corpus[sample_inx])\n",
    "    print('样本的分词效果：'+'/'.join(split_words))\n",
    "    print('样本的topk10词为：'+str(get_TF(split_words)))\n",
    "    \n",
    "main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "metadata": {
    "collapsed": True
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "metadata": {
    "collapsed": True
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "metadata": {
    "collapsed": True
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
