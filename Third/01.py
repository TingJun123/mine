# 如果已知英制长度的英尺foot和英寸inch的值，那么对应的米是(foot+inch/12)×0.3048。
# 现在，如果用户输入的是厘米数，那么对应英制
# 长度的英尺和英寸是多少呢？
# 别忘了1英尺等于12英寸。
n = float(input())
k = 0.01 * n / 0.3048
i = int(k)
j = int((k - i)*12)
print(i, j)
