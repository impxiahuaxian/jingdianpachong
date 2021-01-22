import os
import time
import random

import requests
import pandas as pd


class GetInfo():
    def __init__(self):
        # 去哪儿热门景点excel文件保存路径
        self.PLACE_EXCEL_PATH = 'qunar_place.xlsx'


    def spider_place(self, keyword, page):
        """
        爬取景点

        :param keyword: 搜索关键字
        :param page: 分页参数
        :return:
        """
        url = f'http://piao.qunar.com/ticket/list.json?keyword={keyword}&region=&from=mpl_search_suggest&page={page}'
        headers = {
            'Accept': 'application / json, text / javascript, * / *; q = 0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'piao.qunar.com',
            'Referer': 'https://piao.qunar.com/ticket/list_%E7%83%AD%E9%97%A8%E6%99%AF%E7%82%B9.html?from=mpl_search_suggest_h',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
    
        response = requests.get(url, headers=headers)
        # 提取景点信息
        place_list = self.get_place_info(response.json())
        print(place_list)
        # 保存景点信息
        self.save_excel(place_list)


    def get_place_info(self, response_json):
        """
        解析json，获取想要字段
        :param response_json:
        :return:
        """
        sight_list = response_json['data']['sightList']
        place_list = []
        for sight in sight_list:
            goods = {'景点id': sight['sightId'],  # 景点id
                     '景点名称': sight['sightName'],  # 景点名称
                     '景点星级': sight.get('star', '无'),  # 景点星级，使用get方法防止触发KeyError
                     '评分': sight.get('score', 0),  # 评分
                     '门票价格': sight.get('qunarPrice', 0),  # 门票价格
                     '销量': sight.get('saleCount', 0),  # 销量
                     '所在地区': sight['districts'],  # 省 市 县
                     '坐标': sight['point'],  # 坐标
                     '简介': sight.get('intro', ''),  # 简介
                     }
            place_list.append(goods)
        return place_list


    def save_excel(self, place_list):
        """
        将json数据生成excel文件
        :param place_list: 景点数据
        :return:
        """
        if os.path.exists(self.PLACE_EXCEL_PATH):
            df = pd.read_excel(self.PLACE_EXCEL_PATH)
            df = df.append(place_list)
        else:
            df = pd.DataFrame(place_list)
        writer = pd.ExcelWriter(self.PLACE_EXCEL_PATH)
        df.to_excel(excel_writer=writer,
                    columns=['景点id', '景点名称', '景点星级', '评分', '门票价格', '销量', '所在地区', '坐标', '简介'], index=False,
                    encoding='utf-8', sheet_name='去哪儿热门景点')
        writer.save()
        writer.close()


    def patch_spider_place(self, keyword):
        """
        批量爬取淘去哪儿景点
        :param keyword: 搜索关键字
        :return:
        """
        # 写入数据前先清空之前的数据
        if os.path.exists(self.PLACE_EXCEL_PATH):
            os.remove(self.PLACE_EXCEL_PATH)
        # 批量爬取
        for i in range(1, 8):
            print(f'正在爬取 {keyword} 第{i}页')
            self.spider_place(keyword, i)
            # 设置一个时间间隔
            time.sleep(random.randint(2, 5))
        print('爬取完成！')


if __name__ == '__main__':
    getinfo = GetInfo()
    getinfo.patch_spider_place('热门景点')





