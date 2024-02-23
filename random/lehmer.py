import matplotlib.pyplot as plt
x = 123
 
for i in range(1, 127):
    g_x = i * x % 127
    counter = 1
    while x != g_x:
        counter += 1
        g_x = i * g_x % 127
    if counter == 126:
        print(i, counter)

xPoints = []
yPoints = []
#101
g_x = 101 * x % 127
while x != g_x:
    last_x = g_x
    xPoints.append(last_x)
    g_x = 101 * g_x % 127
    yPoints.append(g_x)

plt.scatter(xPoints, yPoints)
plt.show()

xPoints = []
yPoints = []
zPoints = []

a = 66
m = 401
x = 123
g_x = a * x % m
last_x = g_x

while x != g_x:
    last_last_x = last_x
    last_x = g_x
    xPoints.append(last_last_x)
    g_x = a * g_x % m
    yPoints.append(last_x)
    zPoints.append(g_x)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(xPoints, yPoints, zPoints)
plt.show()

