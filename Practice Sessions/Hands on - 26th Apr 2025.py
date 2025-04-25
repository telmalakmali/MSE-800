#Activity1:Write a code to use round function to calculate the area of a rectangle land try to usboth Jupyter Notebook and Py
#Option 1
X = round(4.567)
print("Value is",X)

#Option 2 -- check this 
x = 14.122
y = 12.19
def area(x,y):
    area_land = x * y
    int_area = int(area_land)
    print("Retun value", area_land)
    print("Retun value as integer", int_area)
    return area_land
area (x,y)
    

#Activity2: Write a function to calculate factorial X
A=5
def fac(A):
       if A == 1 or A == 0:
            print("Return value for fac is", A)
            return A
       else:
            fac_cal = A * fac(A - 1)
            print("Return value is", fac_cal)
            return fac_cal
fac(A)