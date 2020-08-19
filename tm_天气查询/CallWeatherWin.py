# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from WeatherWin import Ui_widget
import requests
import json

class MainWindow(QMainWindow ):
	def __init__(self, parent=None):    
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_widget()
		self.ui.setupUi(self)

	# 1.读取 城市编码 文件，并把文件返回为 字典 类型
	def read_city_txt(self):
		with open('city_code.txt', 'r', encoding='utf-8') as f:
			return json.load(f)

	# 2.形成 城市 和 编码的 映射关系
	def get_city_code(self, city, table):
		city_code = table[city]
		return city_code

    # 3.查询天气
	def queryWeather(self):
		print('* queryWeather  ')

		city_dict = self.read_city_txt()
		# print(city_dict)

        # 通过文本框传入想要搜索的城市名称:天津
		cityName = self.ui.weatherComboBox.currentText()

		# 获取城市的编码号
		cityCode = self.get_city_code(cityName, city_dict)

        # 获取天气的API
		url = f'http://wthrcdn.etouch.cn/weather_mini?citykey={cityCode}'

		print(cityCode)
		res = requests.get(url)
		res.encoding = 'utf-8'

		res_json = res.json()
		# print(res_json)  # 返回 字典 类型

        # 解析数据，数据格式化
		data = res_json['data']
		city = f"城市：{data['city']}\n"  # 字符串格式化的一种方式  f" {} " 通过字典传递值

		today = data['forecast'][0]
		date = f"日期：{today['date']}\n"  # \n 换行
		now = f"实时温度：{data['wendu']}度\n"
		temperature = f"温度：{today['high']} {today['low']}\n"
		fengxiang = f"风向：{today['fengxiang']}\n"
		type = f"天气：{today['type']}\n"
		tips = f"贴士：{data['ganmao']}\n"

		result = city + date + now + temperature + fengxiang + type + tips

		print(result)
		# 在文本框显示查询结果
		self.ui.resultText.setText(result)
				
	def clearResult(self):
		print('* clearResult  ')
		self.ui.resultText.clear()	
		
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	win = MainWindow()  
	win.show()  
	sys.exit(app.exec_())  
