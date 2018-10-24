#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd

print pd.__version__

series1 = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
print series1

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento', 'Haha'])
population = pd.Series([852469, 1015785, 485199])

city_population_frame = pd.DataFrame({'City name': city_names, 'Population': population})
print city_population_frame

describe = city_population_frame.describe()
print describe

head = city_population_frame.head()
print head

# california_housing_dataframe = pd.read_csv("https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv", sep=",")
# california_housing_dataframe.describe()
# print california_housing_dataframe

hist_population = city_population_frame.hist("Population")
print hist_population

print "访问数据\n"
cities = pd.DataFrame({"city": city_names, "population": population})
# print cities
row_city = cities["city"]
print type(row_city)
print row_city

item_city = row_city[1]
print type(item_city)
print item_city

item_line = cities[0:1]
print type(item_line)
print item_line

print "操作数据\n"

temp = cities["population"]
temp = temp / 1000
print temp

# print cities

temp = cities["population"] > 1000 & cities["city"].apply(lambda city: city.startswith('San'))
print temp

cities["new row"] = temp
print  cities

print "索引"

print city_names.index
print population.index
print cities.index

temp = cities.reindex([2, 0, 1])
print temp
print cities

print "随机重排序"
import numpy as np

temp = cities.reindex(np.random.permutation(cities.index))
print temp

print "练习二"
