measurement1=float(input("Input the wall's height: "))
measurement2=float(input("Input the wall's width: "))
capacity=int(input("How many square meters each liter can paint? "))
print(f"The wall's area is {measurement1*measurement2}, and it needs {measurement1*measurement2/capacity:.3f} liters to cover it all.")