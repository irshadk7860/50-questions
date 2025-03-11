
# return statement is used in  function return statement is return something and with the use of return statement we can reuse very easily
# check the number is even or odd
def my_fun(m):
    if m%2==0:
        return 'even'
    else:
        return 'odd'   



# check the number is positive ,negative or zero

def checker(n):
    if n==0:
        return 'zero number'
    
    elif n>0:
        return 'positive'
    
    else:
        return 'negative'


# check the number is prime 

def isprime(n):
    count=0
    i=1
    while i<=n:
        if n%i==0:
            count=count+1
        i=i+1
    if count==2:
        return 'prime number '
    else:
        return 'not a prime number'
        
        

# reverse a string 
def rvstr(n):
    return n[::-1]
    # for i in range(len(n)-1,-1,-1):
    #     return 
    
    
# check the string is palindrome nor not 

def ispalindrome(s):
    if s==s[::-1]:
        return 'palindrome'
    else:
        return "not a palindrome"
    
    
   
# reverse a number:

def isreverse(n):
    rem=0
    rev=0
    while n!=0:
      rem =n%10
      rev= rem +(rev*10)
      n = n//10
    return rev
 
# sum of digits 
def smdigit(n):
    sum=0
    while n>0:
        sum = sum+(n%10)
        n=n//10
        
    return sum 
        
# mximum digit from list

def ismax(a):
    max=a[0]
    for i in a:
       if i > max:
        max=i
    return max
        
# sorting a list 

def sortlist(a):
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            if a[i]> a[j]:
                a[i],a[j]=a[j],a[i]
                
    return a
    

# factorial of a number:
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f


# fabnocci series 
def fabnocci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=' ')
        a,b=a+b,a


# remove duplicate from list
def duplicate(data):
    noduplicate=[]
    for element in data:
        if element not in noduplicate:
            noduplicate.append(element)
    return noduplicate
    
    
    
# count the number vowels in number

def vowel(w):
    count=0
    lst=['a','e','i','o','u']
    
    for char in w :
        if char in lst:
            count=count+1      
    return count
     

# occurence of words 
def occur(st):
    str_char={}
    for char in st:
        if char in str_char:
            str_char[char]+=1
        else:
            str_char[char]=1
    return str_char
        
     
# CHECK TWO STRING IS ANARGAM OR NOT 

def anargam(m,n):
    if sorted(m)==sorted(n):
        return 'anargam'
    else:
        return 'not anargam'   
    
# REVERSE THE WORDS IN STRING 
def rvword(m):
    w=m.split(" ")
    # print(w[-1::-1])
    z= w[-1::-1]
    s=" ".join(z)
    return s

# check the leap year 

def leap(m):
    if m%4==0:
        return 'leap year'
    
    else:
        return "not a leap year"

# without using** we can find power 
def power(n,po):
    p=1
    for i in range(po):
        p=p*n
    return p

# convert binaryy to decimal

def binary(d):
    binary = bin(d)
    return binary


# find second larrgest in list 
def seclarge(n):
    n.sort(reverse=True)
    second=n[1]
    return second

# larggest number of words in string 
def lorge(st):
    w=st.split(" ")
    print(w)
    maximum= max(w,key=len)
    return maximum


# recursion factorial

def factorial(n):
    if(n==0 or  n==1):
        return 1
    else:
        return n * factorial(n-1)

# remove the space from string 
def space(st):
    w=st.split(" ")
    out="".join(w)
    return out

# common from list
def common(n,m):
    c=[]
    for i in n:
        if i in m:
            c.append(i)
            
    return c


if __name__=='__main__':
    
    print(isprime(66))
    
    print(checker(78))
    
    print(my_fun(90))
    
    print(rvstr('khan'))
    
    print(ispalindrome("mom"))
    
    print(isreverse(86))
    print(smdigit(876))
    
    print(ismax([2,4,6,7,33,22]))
    
    print(sortlist([23,45,22,78,33]))
    
    print(fact(6))
    
    fabnocci(20)
    
    print()
    
    
    print(duplicate([1,2,3,2,4,2,6,5,7,1,2,4]))
    
    print(vowel("hello"))
    
    print(anargam("abc","cba"))
    
    print(rvword("my name is khan hai"))
    
    print(leap(2023))
    
    print(occur("hello"))
    
    print(power(2,3))
    
    print(binary(4))
    
    print(seclarge([1,3,4,5,6]))
    
    print(lorge("well you have any issue in progrmming language"))
    
    print(factorial(6))
    
    print(space("well you are doing well and performance is good "))
    
    
    print(common([1,2,3,4,5],[3,2,1,8,8]))