n=int(input())
i=n
rev=0
while i!=0:
    rev=rev*10+(i%10)
    i=i//10   
if n==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
    