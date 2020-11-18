import numpy as np
import time
import matplotlib.pyplot as plt

#bleble

#1
#a
def kwadraty1(x):
    t11 = time.time()
    lista1 = []
    for y in range(0,int(x)):
        z = y**2
        lista1.append(z)
    t12 = time.time()
    print(t12-t11)
kwadraty1(1000000)

#b
def kwadraty2(a):
    t21 = time.time()
    lista2 = [b**2 for b in range(0,a)]
    t22 = time.time()
    print(t22-t21)
kwadraty2(1000000)

#c
def kwadraty3(h):
    t31 = time.time()
    lista3 = np.arange(h)**2
    t32 = time.time()
    print(t32-t31)
kwadraty3(1000000)

#2
tablica = np.ones((4,4), dtype=bool)
print(tablica)

#3
a = np.arange(10)
b = np.ones(10)
a2 = a.reshape(2,5)
b2 = b.reshape(2,5)
c = np.append(a2, b2, axis=1)
print(c)

#4
wektor = np.random.random(20)
for a in wektor:
    if 0.5<a<0.9:
        print(a)

#5
plik = np.loadtxt('dih_sample.dat')
tabela = np.array(plik)
print(np.shape(tabela))
nor = np.array(tabela-min(tabela))/(max(tabela)-min(tabela))
print(np.shape(nor))
save = open('save_dane.dat', 'w')
save.write(str(nor))
save.close()

#6
a = float(input())
x = np.linspace(-10.,0.)
y = (a*x/-3)
z = np.linspace(0.,10.)
t = z**2/3
plt.plot(x, y, color='b', label='f(x)=-ax/3 dla xϵ[-10, 0)')
plt.plot(z, t, color= 'g', label='f(x)=x^2/3 dla xϵ[0, 10]')
plt.legend(loc='upper left')
labels = plt.xticks()
plt.xticks(np.arange(-10,10, step = 2))
plt.xlabel('x', fontsize=8)
plt.ylabel('f(x)', fontsize=8)
plt.show()
