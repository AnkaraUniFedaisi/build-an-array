import numpy as np
#build ana array of the average of weights each weekend
#the weight scheme:
daily_weight = 185 - np.arange(5 * 7) / 5
print(daily_weight)

#print(daily_weight[[5, 6]])
#print(daily_weight[[12, 13]])
#print(daily_weight[[19, 20]])
#print(daily_weight[[26, 27]])
#print(daily_weight[[33, 34]])

n = 5
data = list()
sum = 0
while n + 1 in range(daily_weight.size):
    sum = daily_weight[n] + daily_weight[n + 1]
    data.append(sum / 2)
    n += 7

#print(data)
array = np.array(data)
print(array)
