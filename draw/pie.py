import os
import pandas as pd
from pyecharts import Pie, Bar, TreeMap, Scatter

def create_gender(df):
    '''
    性别
    '''
    df = df.copy()
    df.loc[df.gender == 0, 'gender'] = '未知'
    df.loc[df.gender == 1, 'gender'] = '男性'
    df.loc[df.gender == 2, 'gender'] = '女性'
    #  性别统计
    gender_message = df.groupby(['gender'])
    gender_com = gender_message['gender'].agg(['count'])
    gender_com.reset_index(inplace=True)

    # 生成饼图
    attr = gender_com['gender']
    v1 = gender_com['count']
    pie = Pie('大V性别分布情况', title_pos='center', title_top=0)
    pie.add('', attr, v1, radius=[40,75], label_text_color=None, is_label_show=True, legend_orient='vertical', legend_pos='left', legend_top='%10')
    pie.render("大V性别分布情况.html")


def create_likes(df):
    """
    点赞数
    """
    df = df.sort_values('likes', ascending=False)
    attr = df['name'][0:10]
    v1 = ['{}'.format(float('%0.1f'%(float(i)/10000))) for i in df['likes'][0:10]]

    # 生成柱状图
    bar = Bar('大V点赞数TOP10(万)', title_pos='center', title_top='18', width=800, height=400)
    bar.add('', attr, v1, is_convert=True, xaxis_min=0, yaxis_label_textsize=12, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=True, is_legend_show=False, label_pos='right',is_yaxis_inverse=True, is_splitline_show=False)
    bar.render("大V点赞数TOP10.html")


def create_fans(df):
    """
    粉丝数
    """
    df = df.sort_values('fans', ascending=False)
    attr = df['name'][0:10]
    v1 = ["{}".format(float('%.1f' % (float(i) / 10000))) for i in df['fans'][0:10]]

    # 生成柱状图
    bar = Bar("抖音大V粉丝数TOP10(万)", title_pos='center', title_top='18', width=800, height=400)
    bar.add("", attr, v1, is_convert=True, xaxis_min=0, yaxis_label_textsize=12, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=True, is_legend_show=False, label_pos='right', is_yaxis_inverse=True, is_splitline_show=False)
    bar.render("抖音大V粉丝数TOP10.html")


def create_type_likes(df):
    """
    类型点赞数
    """
    dom = []
    print(df)
    likes_type_message = df.groupby(['type'])
    likes_type_com = likes_type_message['likes'].agg(['sum'])  # 统计
    likes_type_com.reset_index(inplace=True)
    for name, num in zip(likes_type_com['type'], likes_type_com['sum']):
        data = {}
        data['name'] = name
        data['value'] = num
        dom.append(data)
    # 生成矩形树图
    treemap = TreeMap('各类型抖音大V点赞数汇总图', title_pos='center', title_top='5', width=800, height=400)
    treemap.add('各类型抖音大V点赞数汇总图', dom, is_label_show=True, label_pos='inside', is_legend_show=False)
    treemap.render('各类型抖音大V点赞数汇总图.html')


def create_scatter(df):
    """
    三维度散点图
    """
    # 生成数据列表
    data = [list(i) for i in zip(df['videos'], df['fans'], df['likes'])]
    print(data)
    # 生成散点图
    x_lst = [v[0] for v in data]
    y_lst = [v[1] for v in data]
    extra_data = [v[2] for v in data]
    sc = Scatter("抖音大V视频数粉丝数点赞数三维度", title_pos='center', title_top='5', width=800, height=400)
    sc.add("", x_lst, y_lst, extra_data=extra_data, is_visualmap=True, visual_dimension=2, visual_orient="horizontal", visual_type="size", visual_range=[0, 500000000], visual_text_color="#000", visual_range_size=[5, 30])
    sc.render('抖音大V视频数粉丝数点赞数三维度.html')



def create_avg_likes(df):
    """
    平均点赞数
    """
    df = df[df['videos'] > 0]
    df.eval('result = likes/(videos*10000)', inplace=True)
    df['result'] = df['result'].round(decimals=1)
    df = df.sort_values('result', ascending=False)
    attr = df['name'][0:10]
    v1 = df['result'][0:10]

    # 生成柱状图
    bar = Bar("抖音大V平均视频点赞数TOP10(万)", title_pos='center', title_top='18', width=800, height=400)
    bar.add("", attr, v1, is_convert=True, xaxis_min=0, yaxis_label_textsize=12, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=True, is_legend_show=False, label_pos='right', is_yaxis_inverse=True, is_splitline_show=False)
    bar.render("抖音大V平均视频点赞数TOP10.html")



def create_avg_fans(df):
    """
    平均粉丝数
    """
    df = df[df['videos'] > 0]
    df.eval('result = fans/(videos*10000)', inplace=True)
    df['result'] = df['result'].round(decimals=1)
    df = df.sort_values('result', ascending=False)
    attr = df['name'][0:10]
    v1 = df['result'][0:10]

    # 生成柱状图
    bar = Bar("抖音大V平均视频粉丝数TOP10(万)", title_pos='center', title_top='18', width=800, height=400)
    bar.add("", attr, v1, is_convert=True, xaxis_min=0, yaxis_label_textsize=12, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=True, is_legend_show=False, label_pos='right', is_yaxis_inverse=True, is_splitline_show=False)
    bar.render("抖音大V平均视频粉丝数TOP10.html")


# 读取文件
def read_csv(file_path):
    data_info = pd.read_csv(file_path, engine='python', encoding='utf-8')
    return data_info


# 保存
def save_csv(music_info, file_path, head=None):
    data = pd.DataFrame(music_info, columns=head)
    # index=False去掉DataFrame默认的index列
    data.to_csv(file_path, encoding="utf-8", index=False)


# 根据文件名获取文件数据, 返回文件head，文件数据data
def getFileData(file_name):
    if file_name == 'gender':
        return ['gender', 'link'], [{'gender': 1, 'link': 'http://www.baidu.com'}, {'gender': 0, 'link': 'http://www.baidu.com'}]
    elif file_name == 'likes':
        return ['name', 'likes'], [{'name': '浙有正能力', 'likes': 50000},
                                   {'name': '活的刘二斗', 'likes': 40000},
                                   {'name': '人民日报', 'likes': 30000},
                                   ]
    elif file_name == 'fans':
        return ['name', 'fans'], [{'name': '迪丽热巴', 'fans': 53000},
                                  {'name': '陈赫', 'fans': 43000},
                                  {'name': '活的刘二斗', 'fans': 32000},
                                  ]
    elif file_name == 'type_likes':
        return ['type', 'likes'], [{'type': '蓝v', 'likes': 53000},
                                  {'type': '帅哥', 'likes': 43000},
                                  {'type': '美妞', 'likes': 32000},
                                  ]
    elif file_name == 'scatter':
        return ['videos', 'fans', 'likes'], [{'videos': 100, 'likes': 53000, 'fans': 10000},
                                             {'videos': 300, 'likes': 43000, 'fans': 100},
                                             {'videos': 10, 'likes': 32000, 'fans': 1000},
                                            ]


# 获取文件, 返回文件数据
def getFile(file_name):
    current_path = os.getcwd() + "/data/"
    if not os.path.exists(current_path):
        os.makedirs(current_path)
    file_path = '{0}/{1}.csv'.format(current_path, file_name)
    if os.path.exists(file_path) != True:
        head, data_info = getFileData(file_name)
        save_csv(data_info, file_path, head=head)
    data_info = read_csv(file_path)
    return data_info


if __name__ == '__main__':
    #data_info = getFile('gender')
    # create_gender(data_info)

    # data_info = getFile('likes')
    # create_likes(data_info)

    # data_info = getFile('fans')
    # create_fans(data_info)

    # data_info = getFile('type_likes')
    # create_type_likes(data_info)

    data_info = getFile('scatter')
    create_scatter(data_info)