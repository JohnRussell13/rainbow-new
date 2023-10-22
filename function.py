import numpy as np
import vector
import coeficients

# Func -> Vec
to_vector = lambda func: (np.array([0, func(0)]), np.array([1, func(1)]))

# Func -> Coef
to_coef = lambda func: (func(0), func(1)-func(0))