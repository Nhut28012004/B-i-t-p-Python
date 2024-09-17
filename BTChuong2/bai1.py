import math

try:
    r=float(input(" Mời bạn nhập bán kính "))
    cv=2*math.pi*r
    dt=r**2
    print(" Chu vi =",cv)
    print(" Diện tích =",dt)
except:
    print("Sai rồi !")  
    