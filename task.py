# amstrong number
# n=153
# find len of the number
# separate the digits
#1pow len of number--->1pow3+5pow3+3pow3
# sum
# check condition


# 153 --> 1+125+27=153

#automorphic number


n=int(input("Enter a number: "))
d=len(str(n))
a=n//100
b=(n//10)%10
c=n%10
a**=d
b**=d   
c**=d
sum=a+b+c
print(sum)
if(sum==n):
    print(n,"amstrong number")
else:
    print(n,"not amstrong number")



n=25
a=n*n
if a%100==n:
    print(n,"automorphic number")   
else:
    print(n,"not automorphic number")