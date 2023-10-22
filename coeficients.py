import numpy as np
import vector
import function

# Coef -> Func
to_func = lambda coef: lambda x: coef[0] * x + coef[1]

# Coef -> Num
slope = lambda coef1, coef2: (coef2[1] - coef1[1]) / (coef2[0] - coef1[0])

# Coef -> Point
intersection = lambda coef1, coef2: (slope(coef1, coef2), to_func(coef1)(slope(coef1, coef2)))