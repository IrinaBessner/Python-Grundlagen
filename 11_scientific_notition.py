x=1e3
print(x)

y=2.5e6
print(y)

z=3e-2
print(z)

w=4.7e-5
print(w)               # 4.7e-05 in der Konsole
print(f"{w:.6f}")       # 0.00047 -  highly recommended , formated
print(format(w, ".6f")) # 0.00047
print("%.6f" % w)       # 0.00047  - old style


