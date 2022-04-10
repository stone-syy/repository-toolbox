import time
import numpy
import requests
import json, os, random, jieba
from wordcloud import WordCloud
from PIL import Image
from matplotlib import pyplot

#存储数据路径
comments_path = 'D:/comment.txt'


def get_jd(page=0):
    head = {
        'Referer':'https://item.jd.com/',
        'user-agent':'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 100.0.4896.75Safari / 537.36'
    }
    url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100031406046&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1" % page
    try:
        result = requests.get(url, params=head)
        result.raise_for_status()
        #print(result.text[20:-2])
    except:
        print("fail")
    # 截取json字符串
    json_str = result.text[20:-2]
    # 字符串转json对象
    json_obj = json.loads(json_str)
    # 提取json字符串
    comments = json_obj['comments']
    # print(comments)
    # if os.path.exists(comments_path):
        # os.remove(comments_path)
    # 遍历评论列表
    for json_comment in comments:
        # print(json_comment['content'])
        with open(comments_path, 'a+') as comments_file:
            comments_file.write(json_comment['content'] + '\n')


def multiple_capture():
    if os.path.exists(comments_path):
        os.remove(comments_path)
    for pages in range(30):
        get_jd(pages)
        print("正在爬取第{}页".format(pages))
        time.sleep(random.random() * 3)


def cut_data():
    with open(comments_path) as file:
        comment_content = file.read()
        word_list = jieba.cut(comment_content, cut_all=True)
        wl = " ".join(word_list)
        # print(wl)
        return wl


def create_word_cloud():
    # 生成词云
    color = numpy.array(Image.open("D:/Python/repository-toolbox/test.jpg"))
    # 设置词云的配置，如字体，背景色，大小等
    word_cloud = WordCloud(background_color="white", max_words=2000, mask=color,
                           scale=4, max_font_size=50, random_state=42,
                           font_path="C:/Windows/Fonts/simhei.ttf")
    # 生成词云
    word_cloud.generate(cut_data())
    pyplot.imshow(word_cloud, interpolation="bilinear")
    pyplot.axis("off")
    pyplot.figure()
    pyplot.show()


if __name__ == '__main__':
    multiple_capture()
    cut_data()
    create_word_cloud()



