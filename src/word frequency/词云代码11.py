import wordcloud

def genwordcloud_eng_simple(txt, fnpic):
    wc = wordcloud.WordCloud(
             font_path = r"simsun.ttc",   # 汉字词云必须设置字体参数，宋体为simsun.ttc
                                          # 如果不行，就写字体的全路径名：r"c:\Windows\Fonts\simsun.ttc"
                                          # 微软雅黑为msyh.ttf，黑体为simhei.ttf
             background_color="white",    # 默认值是 "black"
             width = 600, height = 400,   # 默认值是 width = 400, height = 200
             max_words = 20,              # 默认值是 200，表示允许出现在词云图片中的单词个数上限
             prefer_horizontal = 0.9,     # 默认值是 0.9，表示水平排列的单词的比例
             collocations = False,        # 默认值是 True，表示词云是否统计搭配词（二元组），设为False则无重复关键词
             min_font_size = 4,           # 默认值为4，表示设置词云中的最小字体对应的像素数
             max_font_size = None,        # 默认值为None，取图片高度像素值，表示设置词云中的最大字体对应的像素数
             stopwords = {})
    t = wc.generate(txt)
    t.to_image().save(fnpic)

if __name__ == "__main__":
    fn = "testcn.txt"
    txt = open(fn,encoding="gbk").read()
    fn  = "词云12.jpg"
    genwordcloud_eng_simple(txt, fn)


