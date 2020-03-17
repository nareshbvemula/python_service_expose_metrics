a = [1,2,3,4,5]
b = [2,8,9,7]
c = [2,10,5,9]

x = []
z = set()
def fun(k):
    for j in k:
        x.append(j)

fun(a)
fun(b)
fun(c)

for k in x:
    if x.count(k) > 2:
        z.add(k)


for m in range(0,len(a)):
    if a[m] == b[m]:
        z.add(m)
print(x)
print(z)

# 4 - ppl cross a bridge
# 1 torch light
# 1st person - 1 sec to cross
# 2nd person - 2 sec to cross
# 3rd person - 5 sec
# 4th person - 10 sec to cross

# At a time only 2 person can cross the bridge

# how many sec all 4 can cross a bridge

10 + 1 + 5 + 1 + 2

