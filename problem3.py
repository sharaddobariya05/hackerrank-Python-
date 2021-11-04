# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())
   
#def power(a, b):
 #   return a**b
    
#def power(a, b, m):
  #  p = a**b
   # q = p % m
    #return q
# here we have issue of method overloading as python do not suppoet method overloading.
#from multipledispatch import dispatch
#passing one parameter
#@dispatch(int,int)
def power(a, b):
    return a**b
#passing one parameter
#@dispatch(int,int, int)    
def power1(a, b, m):
    p = a**b
    q = p % m
    return q

print(power(a, b))
print(power1(a, b, m))
