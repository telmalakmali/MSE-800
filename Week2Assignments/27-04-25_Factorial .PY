#Activity2: Write a function to calculate factorial X 
#A=5
#def fac(A):
      # if A == 1 or A == 0:
      #      print("Return value for fac is", A)
      #      return A
      # else:
      #      fac_cal = A * fac(A - 1)
       #     print("Return value is", fac_cal)
       #     return fac_cal
#fac(A)

# 27th April
#Activity3: Develop a factorial project with at least one class. 

class Fac:
    def fac(A):
        if A == 1 or A == 0:
            print("Return value for fac is", A)
            return A
        else:
            fac_cal = A * Fac.fac(A - 1)  # Recursive call using class name
            print("Return value is", fac_cal)
            return fac_cal

Fac.fac(5)  # This will compute the factorial of 5