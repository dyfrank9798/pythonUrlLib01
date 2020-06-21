import wordcloud
from PIL import Image
import numpy as np
from matplotlib import colors

def genwordcloud_txt(txt, mkpic, fnpic):
    colorlist = ["black", "red", "#00ff00", "#0000ff"]
    colormap = colors.ListedColormap(colorlist)
    mk = np.array(Image.open(mkpic))
    wc = wordcloud.WordCloud(
             font_path = r"simsun.ttc",   # 汉字词云必须设置字体参数，宋体为simsun.ttc
                                          # 如果不行，就写字体的全路径名：r"c:\Windows\Fonts\simsun.ttc"
                                          # 微软雅黑为msyh.ttf，黑体为simhei.ttf
             background_color="white",    # 默认值是 "black"
             colormap = colormap,         # 自定义慈云文字颜色
             width = 600, height = 400,   # 默认值是 width = 400, height = 200
             max_words = 100,             # 默认值是 200，表示允许出现在词云图片中的单词个数上限
             prefer_horizontal = 0.7,     # 默认值是 0.9，表示水平排列的单词的比例
             collocations = False,        # 默认值是 True，表示词云是否统计搭配词（二元组），设为False则无重复关键词
             min_font_size = 10,          # 默认值为4，表示设置词云中的最小字体对应的像素数
             max_font_size = 100,         # 默认值为None，取图片高度像素值，表示设置词云中的最大字体对应的像素数
             mask = mk,                   # 设置词云的形状
             stopwords = {})
    t = wc.generate(txt)
    t.to_image().save(fnpic)

if __name__ == "__main__":
    mkpic = "舞女.jpg"                     # 词云形状，如果用numpy做蒙板的话，png图片就不行
    mkpic = "小熊.jpg"                     # 词云形状，如果用numpy做蒙板的话，png图片就不行
    fn = "testcn.txt"
    txt = open(fn).read()
    fn  = "词云14.jpg"
    genwordcloud_txt(txt, mkpic, fn)


