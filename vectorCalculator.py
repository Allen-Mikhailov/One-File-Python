import math

v1 = [100, 100]
v2 = [1, -1]

v1S = .5
v2S = 2

v1 = [v1[0]*v1S, v1[1]*v1S]
v2 = [v2[0]*v2S, v2[1]*v2S]

v3 = [v1[0] + v2[0], v1[1] + v2[1]]
print("x: ", v3[0], " y: ", v3[1])
print("Length: ", math.sqrt(v3[0]*v3[0] + v3[1]*v3[1]))
print("Angle: ", math.atan2(v3[1], v3[0])*180)