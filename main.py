import numpy as np
import math

def approx_eq(num1, num2, rel_tol=1e-5, abs_tol=1e-5):
    return math.isclose(num1, num2, rel_tol=rel_tol, abs_tol=abs_tol)

def vector_sine(v1, v2):
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    magnitude_v1 = math.sqrt(v1[0]**2 + v1[1]**2)
    magnitude_v2 = math.sqrt(v2[0]**2 + v2[1]**2)

    cos_theta = dot_product / (magnitude_v1 * magnitude_v2)
    sin_theta = 1 - cos_theta**2
    return sin_theta

def checkHit(angle, start):
    a = angle
    b = (start[1] - angle * start[0])

    A = (1 + a**2)
    B = (2*a*b)
    C = (b**2 - 1)
    
    discriminant = B**2 - 4*A*C

    if discriminant <= 0:
        raise "No possible"

    sol1 = (-B + np.sqrt(discriminant)) / (2 * A)
    sol2 = (-B - np.sqrt(discriminant)) / (2 * A)

    if approx_eq(sol1, start[0]) and approx_eq(a*sol1+b, start[1]):
        return sol2, a*sol2+b
    return sol1, a*sol1+b

def make_vector(angle, start):
    return [1, angle]

startHeight = 0.9 # [0, 1)
n = 1.33

firstHitX = -np.sqrt(1 - startHeight**2) # 4th quadrant
firstHitY = startHeight

firstInSine = vector_sine([firstHitX, firstHitY], [1, 0])
firstOutSine = firstInSine / n

if abs(firstOutSine) > 1:
    # Reflect
    print("Todo")

# Get in
firstOutAngle = math.asin(firstOutSine)
firstNormalAngle = math.asin(firstInSine)
firstAngle = firstOutAngle-firstNormalAngle
firstStart = (firstHitX, firstHitY)

arrayHit = [(firstHitX, firstHitY)]
angle = firstAngle
start = firstStart
i = 0
while(i < 10):
    i += 1
    hitX, hitY = checkHit(angle, start)
    arrayHit.append((hitX, hitY))

    inSine = vector_sine([firstHitX, firstHitY], make_vector(angle, start))
    outSine = inSine * n

    # if abs(outSine) <= 1:
    #     outAngle = math.asin(outSine)
    #     normalAngle = math.asin(inSine)
    #     angle = outAngle-normalAngle
    #     start = (hitX, hitY)
    #     break

    R = np.eye(2) - 2 * np.outer([firstHitX, firstHitY], [firstHitX, firstHitY])
    newVec = np.dot(R, [1, angle])
    newAngle = newVec[1] / newVec[0]

    angle = newAngle
    start = (hitX, hitY)

import matplotlib.pyplot as plt

firstLine = [(t, arrayHit[0][1]) for t in np.linspace(-2, arrayHit[0][0], 100)]
x_coords, y_coords = zip(*firstLine)
plt.plot(x_coords, y_coords, linestyle='-', color='blue', label='Input line')

x_coords, y_coords = zip(*arrayHit)
plt.scatter(x_coords, y_coords, color='red', marker='o', label='Hit points')
plt.plot(x_coords, y_coords, linestyle='-', color='blue', label='Bounce lines')

# lastLine = [(t, arrayHit[0][1]) for t in np.linspace(-2, arrayHit[0][0], 100)]
# x_coords, y_coords = zip(*firstLine)
# plt.plot(x_coords, y_coords, linestyle='-', color='blue', label='Input line')

theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
plt.plot(x, y, label='Unit Circle', color='black')

plt.gca().set_aspect('equal', adjustable='box')
plt.title('Rainbow')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.show()