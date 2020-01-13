import jieba

# 结巴分词
a = ['你好，我要做词云展示', '你在哪怎么弄项目篇章哈哈哈嘉宾']
c = "".join(a)
print(c)

b = jieba.lcut(c)  # 切分的是字符串

print(b)