import math

x1 = int(input("Please enter the x-coordinate of the first point:"))
y1 = int(input("Please enter the y-coordinate of the first point:"))

x2 = int(input("Please enter the x-coordinate of the second point:"))
y2 = int(input("Please enter the y-coordinate of the second point:"))

d1 = pow(x1-x2, 2)
d2 = pow(y1-y2, 2)

d = d1 +d2
print("Distance: ", math.sqrt(d))