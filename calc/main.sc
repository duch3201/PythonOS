import math
import sys
import os
from os import name

dozwolone_operacje = ["/", "-", "*", "+"]

def main():
    clear()
    try:
        operacja = input("enter operation: ")
        num1 = input("enter first num: ")
        num2 = input("enter second num: ")
        num1 = int(num1)
        num2 = int(num2)
        if operacja in dozwolone_operacje:
            pass
        else:
            print("nie dozwolona operacja")
            input("")
        if (num1 == 0 or num2 == 0):
            if(operacja == "/"):
                print("can't divide by 0!")
                input("")
        if operacja == "+":
            wynik = num1 + num2
        if operacja == "-":
            wynik = num1 - num2
        if operacja == "/":
            wynik = num1 // num2
        if operacja == "*":
            wynik = num1 * num2
        print("wynik to: ", wynik)

    except KeyboardInterrupt:
        clear()
        print("ctrl + c decided!")

def clear():
    if os.name in ('nt', 'dos'):
        command = 'cls'
        os.system(command)
    else:
        command = 'clear'
        os.system(command)


#def algorytm():
 #   try:
  #      A = input("wprowadź A: ")
   #     B = input("wprowadź B: ")
    #    h = input("wprowadź h: ")
     #   A = int(A)
      #  B = int(B)
       # h = int(h)
        #AB = A + B
        #hAB = AB * h
        #dhAB = hAB / 2
        #print("wynik to: " + str(dhAB))
    #except KeyboardInterrupt:
     #   print("ctrl + c wykryte")

#def main():
 #   try:
  #      opcja = input("wybierz opcje, kalk - kalkulator, algo - kalkulator trapezu: ")
   #     if opcja == "kalk":
    #        kalk()
     #   if opcja == "algo":
      #      algorytm()
    #except KeyboardInterrupt:
     #   print("ctrl + c wykryte")

main() 