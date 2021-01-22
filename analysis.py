import re
import json
import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

class Analysis():
    def __init__(self):

        # 去哪儿热门景点excel文件保存路径
        PLACE_EXCEL_PATH = 'qunar_place.xlsx'
        # 读取数据
        self.DF = pd.read_excel(PLACE_EXCEL_PATH)
        self.PLACE_EXCEL_PATH = PLACE_EXCEL_PATH

    #销量排行模块
    def analysis_sale(self):
        """
        分析销量
        :return:
        """
        df = self.DF.copy()
        # 1、生成一个名称和销量的透视表
        place_sale = df.pivot_table(index='景点名称', values='销量')
        # 2、根据销量排序
        place_sale.sort_values('销量', inplace=True, ascending=True)
        print(place_sale)
        # 3、生成柱状图
        place_sale_bar = (
            Bar()
                .add_xaxis(place_sale.index.tolist()[-20:])
                .add_yaxis("", list(map(int, np.ravel(place_sale.values)))[-20:])
                .reversal_axis()
                .set_series_opts(label_opts=opts.LabelOpts(position="right"))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="热门旅游景点门票销量TOP20"),
                yaxis_opts=opts.AxisOpts(name="景点名称"),
                xaxis_opts=opts.AxisOpts(name="销量")
            )
        )
        place_sale_bar.render('热门旅游景点门票销量TOP20.html')

    #销售额排行模块
    def analysis_amount(self):
        """
        分析销售额
        :return:
        """

        df = self.DF.copy()
        amount_list = []
        for index, row in df.iterrows():
            try:
                # 销售额
                amount = row['门票价格'] * row['销量']
            except Exception:
                amount = 0
            amount_list.append(amount)
        df['amount'] = amount_list
        # 生成一个名称和销售额的透视表
        place_amount = df.pivot_table(index='景点名称', values='amount')
        # 根据销售额排序
        place_amount.sort_values('amount', inplace=True, ascending=True)
        print(place_amount)
        # 生成柱状图
        place_amount_bar = (
            Bar()
                .add_xaxis(place_amount.index.tolist()[-20:])
                .add_yaxis("", list(map(int, np.ravel(place_amount.values)))[-20:])
                .reversal_axis()
                .set_series_opts(label_opts=opts.LabelOpts(position="right"))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="热门旅游景点门票销售额TOP20"),
                yaxis_opts=opts.AxisOpts(name="景点名称"),
                xaxis_opts=opts.AxisOpts(name="销售额")
            )
        )
        place_amount_bar.render('热门旅游景点门票销售额TOP20.html')

    #门票价格排行
    def diqu_mingcheng(self):

        df = self.DF.copy()
        # 1、生成一个名称和价格的透视表
        place_jiage = df.pivot_table(index='景点名称', values='门票价格')
        # 2、根据价格排序
        place_jiage.sort_values('门票价格', inplace=True, ascending=True)
        print(place_jiage)
        # 3、生成柱状图
        place_jiage_bar = (
            Bar()
                .add_xaxis(place_jiage.index.tolist()[-20:])
                .add_yaxis("", list(map(int, np.ravel(place_jiage.values)))[-20:])
                .reversal_axis()
                .set_series_opts(label_opts=opts.LabelOpts(position="right"))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="热门旅游景点门票价格TOP20"),
                yaxis_opts=opts.AxisOpts(name="景点名称"),
                xaxis_opts=opts.AxisOpts(name="门票价格")
            )
        )
        place_jiage_bar.render('热门旅游景点门票价格TOP20.html')

    #景点评分排行
    def jingqu_pingfen(self):
        """
        分析销量
        :return:
        """
        df = self.DF.copy()
        # 1、生成一个名称和评分的透视表
        place_pingfen = df.pivot_table(index='景点名称', values='评分')
        # 2、根据评分排序
        place_pingfen.sort_values('评分', inplace=True, ascending=True)
        print(place_pingfen)
        # 3、生成柱状图
        place_pingfen_bar = (
            Bar()
                .add_xaxis(place_pingfen.index.tolist()[-20:])
                .add_yaxis("", list(map(int, np.ravel(place_pingfen.values)))[-20:])
                .reversal_axis()
                .set_series_opts(label_opts=opts.LabelOpts(position="right"))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="热门旅游景点评分TOP20"),
                yaxis_opts=opts.AxisOpts(name="景点名称"),
                xaxis_opts=opts.AxisOpts(name="评分")
            )
        )
        place_pingfen_bar.render('热门旅游景点评分TOP20.html')

    #推荐模块
    def analysis_recommend(self):
        """
        排行榜，高评分、销量少、价格便宜
        :return:
        """
        df = self.DF.copy()
        recommend_list = []
        for index, row in df.iterrows():
            try:
                # 推荐系数算法
                recommend = (row['评分'] * 1000) / (row['门票价格'] * row['销量'])
            except ZeroDivisionError:
                recommend = 0
            recommend_list.append(recommend)
        df['recommend'] = recommend_list
        # 生成一个名称和推荐系数的透视表
        place_recommend = df.pivot_table(index='景点名称', values='recommend')
        # 根据推荐系数排序
        place_recommend.sort_values('recommend', inplace=True, ascending=True)
        print(place_recommend)
        # 生成柱状图
        place_recommend_bar = (
            Bar()
                .add_xaxis(place_recommend.index.tolist()[-20:])
                .add_yaxis("", list(map(int, np.ravel(place_recommend.values)))[-20:])
                .reversal_axis()
                .set_series_opts(label_opts=opts.LabelOpts(position="right"))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="热门旅游景点推荐TOP20"),
                yaxis_opts=opts.AxisOpts(name="景点名称"),
                xaxis_opts=opts.AxisOpts(name="推荐系数")
            )
        )
        place_recommend_bar.render('热门旅游景点推荐TOP20.html')

    #def analysis_point_sale():
    """
    生成热力图，使用百度地图api
    :return:
    """
    # 引入全局数据
    #global DF
    #df = DF.copy()
    #point_sale_list = []
    #for index, row in df.iterrows():
        # 构建坐标数据
        #lng, lat = row['point'].split(',')
        #count = row['sale']
        #point_sale = {'lng': float(lng), 'lat': float(lat), 'count': count}
        #point_sale_list.append(point_sale)
    #print(point_sale_list)
    #data = f'var points ={str(point_sale_list)};'
    # 替换模板中的坐标数据
    #with open(HOT_MAP_TEMPLATE_PATH, 'r', encoding="utf-8") as f1, open(PLACE_HOT_MAP_PATH, 'w',
                                                                        #encoding="utf-8") as f2:
        #s = f1.read()
        # 替换数据
        #s2 = s.replace('%data%', data)
        #f2.write(s2)
        #f1.close()
        #f2.close()


if __name__ == '__main__':
    analysis = Analysis()
    analysis.analysis_sale()
    analysis.analysis_amount()
    analysis.jingqu_pingfen()
    analysis.diqu_mingcheng()
    analysis.analysis_recommend()


