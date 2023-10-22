import numpy as np
import function
import coeficients

# Vec -> HalfVec
vecDif = lambda origin, endpoint: endpoint-origin

# HalfVec -> Mat
halfReflection = lambda vec: np.eye(2) - 2*np.outer(vec, vec)

# Vec -> Mat
reflection = lambda origin, endpoint: halfReflection(vecDif(origin, endpoint))

# Vec -> Num
slope = lambda origin, endpoint: (endpoint[1] - origin[1]) / (endpoint[0] - origin[0])

# Vec -> Func
to_function = lambda origin, endpoint: (
    lambda x: slope(origin, endpoint) * (x - origin[0]) + origin[1]
)

# Vec - Coef
to_coef = lambda origin, endpoint: (slope(origin, endpoint), to_function(origin, endpoint)(0))