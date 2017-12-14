#!/usr/bin/python
# -*- coding: UTF-8 -*-
from highcharts import Highchart

# A chart is the container that your data will be rendered in, it can (obviously) support multiple data series within it.
chart = Highchart()

# Adding a series requires at minimum an array of data points.
# You can also change the series type, the name, or other series options as kwargs.
data = range(1,20)
chart.add_data_set(data, series_type='line', name='Example Series')

# This will generate and save a .html file at the location you assign
chart.save_file()