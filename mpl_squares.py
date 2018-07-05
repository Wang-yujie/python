import json
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
    country_name = pop_dict['Country Name']
    population = pop_dict['Value']
    print(country_name + ": " + population)







##读取csv画双折线填充图##
# import csv
# from matplotlib import pyplot as plt
# from datetime import datetime
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     dates, highs, lows = [], [], []
#     for row in reader:
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
#         high = int(row[1])
#         highs.append(high)
#         low = int(row[3])
#         lows.append(low)
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates, highs, c='red')
# plt.plot(dates, lows, c='blue')
# plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)##折线间填充颜色
# plt.title("Daily high and low temperatures - 2014", fontsize=24)
# plt.xlabel('', fontsize=16)
# fig.autofmt_xdate() ## fig.autofmt_xdate() 来绘制斜的日期标签，以免它们彼此重叠
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
# plt.show()







##散点图##
# import matplotlib.pyplot as plt
# x_values = list(range(0,1001))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values,y_values,edgecolor='none',c=y_values,cmap=plt.cm.Reds,s=40) ##scatter(x,y,s)  c=(0, 0, 0.8)红绿蓝3颜色 cmap颜色渐变
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis='both',  which='major',labelsize=14)
# plt.savefig('scatter') ##以该名保存图片
# # plt.show()



##折线图#######
# import matplotlib.pyplot as plt
# squares = [1, 4, 9, 16, 25]
# input_value = [1,2,3,4,5]
# plt.plot(input_value, squares, linewidth=5)
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis='both', labelsize=14)
# plt.show()
