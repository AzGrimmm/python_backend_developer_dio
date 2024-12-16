def ADD_NUMBERS(a,b):
 return a+b


def Sub_numbers(a,b):return a - b

class calc():

     def __init__(self):    
        pass

def MULTIPLY_NUMBERS(a,b): return a*b

def factorial(num):fact=1
    
    
for i in range(1,num+1):
    fact*=i
    return fact

def divide_numbers(a,b): 
  if b==0: return "Cannot divide by zero" 
    
  else:return a/b

def greetings(name):print("Hello, " + name + "!"   )

nums = [1,2,3,4,5,6]


def squares(nums):   
    result=[]
    for num in nums:result.append(num*num)
    return result

def is_even(num):if num%2==0:return True; else: return False

 

def main():

    print( ADD_NUMBERS(10,20))
  print(Sub_numbers(50,30))
    print(MULTIPLY_NUMBERS(5,10))
     print(factorial(5))
  print(divide_numbers(10,2))
      greetings("Alice")
     print(squares(nums))
     print(is_even(10))

main()
