"""
如果Close<Open，表示为“BW-Solid”（即“实心蓝白蜡烛”）；
如果Close>Open，表示为“R-Hollow”（即“空心红蜡烛”）；
如果Open等于Close，则为“R-Cross”（即“十字红蜡烛”）。
如果Low比Open和Close低，称为“Lower Shadow”（即“有下影线”），
如果High比Open和Close高，称为“Upper Shadow”（即“有上影线”）。
"""
Open, High, Low, Close = input().split()
Close = float(Close)
Open = float(Open)
Low = float(Low)
High = float(High)
if Close < Open:
    if Low < Open and Low < Close:
        if High > Open and High > Close:
            print('BW-Solid with Lower Shadow and Upper Shadow')
        else:
            print('BW-Solid with Lower Shadow')
    elif High > Open and High > Close:
        print('BW-Solid with Upper Shadow')
    else:
        print('BW-Solid')
elif Close == Open:
    if Low < Open and Low < Close:
        if High > Open and High > Close:
            print('R-Cross with Lower Shadow and Upper Shadow')
        else:
            print('R-Cross with Lower Shadow')
    elif High > Open and High > Close:
        print('R-Cross with Upper Shadow')
    else:
        print('R-Cross')
else:
    if Low < Open and Low < Close:
        if High > Open and High > Close:
            print('R-Hollow with Lower Shadow and Upper Shadow')
        else:
            print('R-Hollow with Lower Shadow')
    elif High > Open and High > Close:
        print('R-Hollow with Upper Shadow')
    else:
        print('R-Hollow')