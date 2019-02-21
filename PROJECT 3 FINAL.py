Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
>>> revenue = [145, 760, 861, 917, 805, 810, 114, 976, 103, 143, 107, 154]
>>> expenses = [120, 569, 123, 120, 865, 840, 328, 582, 697, 166, 100, 380]
>>> np_revenue = np.array(revenue)
>>> np_expenses = np.array(expenses)
>>> profit = np_revenue - np_expenses
>>> profit
array([  25,  191,  738,  797,  -60,  -30, -214,  394, -594,  -23,    7,
       -226])
>>> fin_status = {
	'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
	'profit': [25 , 191 , 738 , 797,  -60 , -30, -214 , 394, -594 , -23, 7, -226]
}
>>> fin_status = pd.Series(profit, index=months, name='ABD_company')
>>> fin_status
Jan     25
Feb    191
Mar    738
Apr    797
May    -60
Jun    -30
Jul   -214
Aug    394
Sep   -594
Oct    -23
Nov      7
Dec   -226
Name: ABD_company, dtype: int32
>>> 
KeyboardInterrupt
>>> plt.plot(months, profit, color='r', linewidth=2)
[<matplotlib.lines.Line2D object at 0x010DEAF0>]
>>> plt.xlabel('months', fontsize=12)
Text(0.5, 0, 'months')
>>> plt.ylabel('profit', fontsize=12)
Text(0, 0.5, 'profit')
>>> plt.show(block=False)
>>> 
