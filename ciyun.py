
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import  Image
import  numpy as  np
import imageio


import matplotlib.pyplot as plt
#词云生成工具
from wordcloud import WordCloud,ImageColorGenerator
#需要对中文进行处理
import matplotlib.font_manager as fm

mk = imageio.imread("12.png")
# 读入一部英文小说 txt 文件，这里以 简爱 作为例子
text = open('word.txt','r').read()

love_mask = np.array(Image.open("12.png"))
# 生成词云
wordcloud = WordCloud(font_path='C:\Windows\Fonts\simfang.ttf',
                      background_color="white", max_words=200
                      ,mask=mk,scale=50
                      ).generate(text)

# 显示词云图片
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

my_font=fm.FontProperties(fname='C:/Windows/Fonts/simkai.ttf')
#产生背景图片，基于彩色图像的颜色生成器
image_colors=ImageColorGenerator(love_mask)
#开始画图
plt.imshow(wordcloud.recolor(color_func=image_colors,),interpolation="bilinear")
#为云图去掉坐标轴
plt.axis("off")
#画云图，显示
plt.figure()
#为背景图去掉坐标轴
plt.axis("off")

plt.imshow(love_mask,cmap=plt.cm.gray)
# 保存图片
wordcloud.to_file('test.jpg')