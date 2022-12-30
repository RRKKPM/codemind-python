p,c,b,m,co=map(int,input().split())
percent=int((p+c+b+m+co)/5)
if percent>=90:
    print("Grade A")
elif percent>=80:
    print("Grade B")
elif percent>=70:
    print("Grade C")
elif percent>=60:
    print("Grade D")
elif percent>=40:
    print("Grade E")
elif percent<40:
    print("Grade F")