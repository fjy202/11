import time
def isprime1(num):
    if num==2:
        return True
    elif num%2==0:
        return False
    else:
        for i in range(3,int((num-1)/2)+1):
            if num%i==0:
                return False
    return True
def isprime2(num):
    if num==2:
        return True
    elif num%2==0:
        return False
    else:
        # for i in a:
        #     if num%i==0:
        #         return False
        def key(b):
            if num%b==0:
                return False
            return True
        
        return True in list(map(key,a))
t0=time.time()
a=[2]
# for i in range(3,1000001):
#     if isprime2(i):
#         a.append(i)
# c=3
# while c<100001:
#     if isprime2(c):
#         a.append(c)
#     c+=1
def filter_prime(c):
    if isprime2(c):
        a.append(c)
list(map(filter_prime,range(3,100001)))
print(time.time()-t0)
print(a)
