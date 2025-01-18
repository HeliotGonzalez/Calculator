characters = 0 
a = 1
b = 1
blank = ""
string = ""
power = 0

import sys
import keyboard 
import os
import requests 
import update as us
from guizero import App, Text, PushButton, Box
from playsound import playsound
try:
   import calculatorMod as mod 
   modded = 1
except:
   print("No mod")
   modded = 0
#operations
def one():
    global characters  
    global srv 
    global string    
    global equation
    num = 1
    if characters == 0:
       srv = num
       string = str(srv)
       characters = 1
       equation = str(srv)
    else:
       string = string + str(num) 
       equation = equation + str(num)
    number.value = string

def two():
    global characters
    global srv
    global string    
    global equation
    num = 2
    if characters == 0:     
       srv = num
       string = str(srv)
       characters = 1
       equation = str(srv)
       
    else:
       string = string + str(num) 
       equation = equation + str(num)
    number.value = string

def three():
    global characters
    global srv
    global string    
    global equation
    num = 3
    if characters == 0:     
       srv = num
       string = str(srv)
       characters = 1
       equation = str(srv)
       
    else:
       string = string + str(num) 
       equation = equation + str(num)
    number.value = string

def four():
    global characters
    global srv
    global string    
    global equation
    num = 4
    if characters == 0:     
       srv = num
       string = str(srv)
       characters = 1
       equation = str(srv)
       
    else:
       string = string + str(num) 
       equation = equation + str(num)
    number.value = string

def five():
    global characters
    global srv
    global string    
    global equation
    num = 5
    if characters == 0:     
       srv = num
       string = str(srv)
       characters = 1
       equation = str(srv)
       
    else:
       string = string + str(num) 
       equation = equation + str(num)
    number.value = string

def six():
    global characters
    global srv
    global string    
    global equation
    num = 6
    if characters == 0:     
       srv = num
       string = str(srv)
       characters = 1
       equation = str(srv)
       
    else:
       string = string + str(num) 
       equation = equation + str(num)
    number.value = string

def seven():
    global characters
    global srv
    global string    
    global equation
    num = 7
    if characters == 0:     
       srv = num
       string = str(srv)
       characters = 1
       equation = str(srv)
       
    else:
       string = string + str(num) 
       equation = equation + str(num)
    number.value = string

def eight():
    global characters
    global srv
    global string    
    global equation
    num = 8
    if characters == 0:     
       srv = num
       string = str(srv)
       characters = 1
       equation = str(srv)
       
    else:
       string = string + str(num) 
       equation = equation + str(num)
    number.value = string
    
def nine():
    global characters
    global srv
    global string    
    global equation
    num = 9
    if characters == 0:     
       srv = num
       string = str(srv)
       characters = 1
       equation = str(srv)
       
    else:
       string = string + str(num) 
       equation = equation + str(num)
    number.value = string

def zero():
    global characters
    global srv
    global string    
    global equation
    num = 0
    if characters == 0:     
       srv = num
       string = str(srv)
       characters = 1
       equation = str(srv)
       
    else:
       string = string + str(num) 
       equation = equation + str(num)
    number.value = string

def dot():
    global characters
    global srv
    global string    
    global equation
    num = "."
    if characters == 0:     
       srv = num
       string = str(srv)
       characters = 1
       equation = str(srv)
       
    else:
       string = string + str(num) 
       equation = equation + str(num)
    number.value = string
    

def ac():
    global string
    string = ""
    character = 0
    number.value = string
    
def delete():
    global string
    global equation
    string = string[:-1]
    equation = equation[:-1]
    number.value = string
    
def plus():
    global characters
    global srv
    global string
    global equation
    srv = "+"
    if characters == 0:
       number.value = "Number required on front"
    else:
       string = string + srv
       equation = equation + "+"
    number.value = string
    
def minus():
    global characters
    global srv
    global string   
    global equation
    srv = "-"
    if characters == 0:
       number.value = "Number required on front"
    else:
       string = string + srv
       equation = equation + "-"
    number.value = string
    
def times():
    global characters
    global srv
    global string    
    global equation
    srv = "×"
    if characters == 0:
       number.value = "Number required on front"
    else:
       string = string + srv
       equation = equation + "*"
    number.value =  string
    
def divide():
    global characters
    global srv
    global string 
    global equation
    srv = "÷"
    if characters == 0:
       number.value = "Number required on front"
    else:
       string = string + srv
       equation = equation + "/"
    number.value = string

def bracketOne():
    global characters
    global srv 
    global string    
    global equation
    num = "("
    if characters == 0:
       string = num
       characters = 1
       equation = num
    else:
       string = string + num 
       equation = equation + num
    number.value = string 

def bracketTwo():
    global characters
    global srv 
    global string    
    global equation
    num = ")"
    if characters == 0:
       string = num
       characters = 1
       equation = num
    else:
       string = string + num 
       equation = equation + num
    number.value = string 

def equals():
   global string
   global equation
   global characters
   try:
     result = eval(equation)
     characters = 1
     equation = str(result)
     string = str(result)
     number.value = string
   except:
     number.value = "Invalid Syntax"
     characters = 0

#letters
def a():
   global string
   global equation
   global characters
   num = "a"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def b():
   global string
   global equation
   global characters
   num = "b"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def c():
   global string
   global equation
   global characters
   num = "c"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def d():
   global string
   global equation
   global characters
   num = "d"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def e():
   global string
   global equation
   global characters
   num = "e"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def f():
   global string
   global equation
   global characters
   num = "f"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def g():
   global string
   global equation
   global characters
   num = "g"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def h():
   global string
   global equation
   global characters
   num = "h"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def i():
   global string
   global equation
   global characters
   num = "i"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string



def k():
   global string
   global equation
   global characters
   num = "k"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def l():
   global string
   global equation
   global characters
   num = "l"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def n():
   global string
   global equation
   global characters
   num = "n"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def o():
   global string
   global equation
   global characters
   num = "o"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def p():
   global string
   global equation
   global characters
   num = "p"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def q():
   global string
   global equation
   global characters
   num = "q"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def r():
   global string
   global equation
   global characters
   num = "r"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def s():
   global string
   global equation
   global characters
   num = "s"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def t():
   global string
   global equation
   global characters
   num = "t"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def u():
   global string
   global equation
   global characters
   num = "u"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string

def v():
   global string
   global equation
   global characters
   num = "v"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string      

def w():
   global string
   global equation
   global characters
   num = "w"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string  

def x():
   global string
   global equation
   global characters
   num = "x"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string    

def y():
   global string
   global equation
   global characters
   num = "y"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string  

def z():
   global string
   global equation
   global characters
   num = "z"
   if characters == 0:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = num
         equation = formula
         characters = 1
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window."
         formula = input("Assign the letter to a number or equasion: ")
         f.write(formula)
         f.close()
   else:
      try:
         f = open("vccData/"+num, "r")
         formula = f.read()
         string = string + num
         equation = equation + formula
      except:
         f = open("vccData/"+num, "x")
         number.value = "Please refer to terminal window"
         formula = input("Assign the letter to a number or equation: ")
         f.write(formula)
         f.close()
         characters = 0
   number.value = string    

keyboard.add_hotkey('1', one)
keyboard.add_hotkey('2', two)
keyboard.add_hotkey('3', three)
keyboard.add_hotkey('4', four)
keyboard.add_hotkey('5', five)
keyboard.add_hotkey('6', six)
keyboard.add_hotkey('7', seven)
keyboard.add_hotkey('8', eight)
keyboard.add_hotkey('9', nine)
keyboard.add_hotkey('0', zero)
keyboard.add_hotkey('.', dot)
keyboard.add_hotkey('shift+=', plus)
keyboard.add_hotkey('m', minus)
keyboard.add_hotkey('shift+8', times)
keyboard.add_hotkey('shift+9', bracketOne)
keyboard.add_hotkey('shift+0', bracketTwo)
keyboard.add_hotkey('/', divide)
keyboard.add_hotkey('enter', equals)
keyboard.add_hotkey('backspace',delete)
keyboard.add_hotkey('a', a)
keyboard.add_hotkey('b', b)
keyboard.add_hotkey('c', c)
keyboard.add_hotkey('d', d)
keyboard.add_hotkey('e', e)
keyboard.add_hotkey('f', f)
keyboard.add_hotkey('g', g)
keyboard.add_hotkey('i', i)
keyboard.add_hotkey('k', k)
keyboard.add_hotkey('l', l)
keyboard.add_hotkey('n', n)
keyboard.add_hotkey('o', o)
keyboard.add_hotkey('p', p)
keyboard.add_hotkey('q', q)
keyboard.add_hotkey('r', r)
keyboard.add_hotkey('s', s)
keyboard.add_hotkey('t', t)
keyboard.add_hotkey('u', u)
keyboard.add_hotkey('v', v)
keyboard.add_hotkey('w', w)
keyboard.add_hotkey('x', x)
keyboard.add_hotkey('y', y)
keyboard.add_hotkey('z', z)

#Checks for updates.
v = open('update.txt','r')
vs = v.read()
os.remove("update.txt")
r = requests.get('https://raw.githubusercontent.com/thetiger21/Calculator/refs/heads/main/calculator/update.txt', auth=('user','pass'))
open('update.txt', 'wb').write(r.content)
vrs = open('update.txt','r')
version = vrs.read()
if vs == version:
   print("No update")
else:
   us.update()

#Checks if there are any mods.
if modded == 1:
   mod.shortcuts() 
   print("Custom keyboard shortcuts activated")
else:
   print("Custom keyboard shortcuts failed to load")

print("Welcome to Very Cool Calculator (VCC), version 1.0")
app = App(title="Calculator", height=400, width=500)
number =  Box(app)
command_box = Box(app, layout="grid", align="left", height=200, width=175)
number_box = Box(app, layout="grid", align="left", height=200, width=175)
operator_box = Box(app, layout="grid", align="right", height=200, width=175)
number = Text(number, text="0")
buttonAc = PushButton(command_box, text="AC",command=ac, grid=[0,0])
buttonDel = PushButton(command_box, text="DEL",command=delete, grid=[0,1])
buttonBracketOne = PushButton(command_box, text="(",command=bracketOne, grid=[1,0])
buttonBracketTwo = PushButton(command_box, text=")",command=bracketTwo, grid=[1,1])
button1 = PushButton(number_box, text="1",command=one, grid=[0,0])
button2 = PushButton(number_box, text="2", command=two, grid=[1,0])
button3  = PushButton(number_box, text="3", command=three, grid=[2,0])
button4  = PushButton(number_box, text="4", command=four, grid=[0,1])
button5  = PushButton(number_box, text="5", command=five, grid=[1,1])
button6  = PushButton(number_box, text="6", command=six, grid=[2,1])
button7  = PushButton(number_box, text="7", command=seven, grid=[0,2])
button8  = PushButton(number_box, text="8", command=eight, grid=[1,2])
button9  = PushButton(number_box, text="9", command=nine, grid=[2,2])
button0  = PushButton(number_box, text="0", command=zero, grid=[1,3])
buttonDot = PushButton(number_box, text=".", command=dot, grid=[2,3])
buttonPlus  = PushButton(operator_box, text="+", command=plus, grid=[0,0])
buttonMinus  = PushButton(operator_box, text="-", command=minus, grid=[1,0])
buttonPlus  = PushButton(operator_box, text="×", command=times, grid=[0,1])
buttonMinus  = PushButton(operator_box, text="÷", command=divide, grid=[1,1])
buttonequals  = PushButton(operator_box, text="=", command=equals, grid=[0,2])
app.display()

