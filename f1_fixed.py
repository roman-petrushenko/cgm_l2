import matplotlib.pyplot as plt
f = open('DS3.txt', 'r')
a = list()
b = list()

while (True):
    
    c = f.readline().split(" ")
    if (c[0] == ""): 
        break
    else:
       a.append(int(c[0]))
       b.append(int(c[1].replace("\n", "")))
plt.figure(figsize = (960/100, 540/100))

plt.scatter(a,b)
plt.xlabel("X")
plt.ylabel("Y")

plt.savefig("fig1.png")
plt.show()
