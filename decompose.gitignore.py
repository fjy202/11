l=[]
a=input("number:")
ax=1
if a.isdigit()==False:
    print("Please try again.")
    exit()
else:
    a=int(a)
for x in range(1,int(a)):
    if a%x==0:
        print(a,"=",int(a/x),"*",x)
        l.append(x)
        #print(int(a / ax), "*",ax, "=", a)
    #ax=ax+1
l.append(a)
print(l)
