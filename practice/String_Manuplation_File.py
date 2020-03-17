import os
import re
BASE_DIR = "C:\\VMWare\\"
f1 = "P0_TestCases.txt"
f2 = "P0_TestCases_back.txt"
#f2 = input("Enter file Name:")

re_Char = re.compile('\w')
re_Spec = re.compile('_')

m = ('a','b','c','d','e','f','g','h','i','j','F')
#m = (re.compile('[A-Z][a-z]'))
n = ('1','2','3','4','5','6','7','8','9','0')
sp = ('$', '#')

pattern1 = '\s+'
pattern2 = '_'
#print(BASE_DIR)
#os.chdir(BASE_DIR)
#cmd = "{} {} {}".format('cp', f1, f2)
#os.system(cmd)
#f3= BASE_DIR + f2

s = "aBc deF g12 3h4 i_j $_# 1_2 3_A"
s1 = s.title()
re_a = s.split(" ")
z = ""
c = 0
for i in range(0, len(re_a)):
    print ( re_a [ i ] )
    if re_a[i].startswith(m) and re_a[i].endswith(m) and re_a[i].isalpha():
        z = z+re_a[i].title()
    elif re_a[i].startswith(n) and re_a[i].endswith(n) and re_a[i].isalnum():
        z = z + re_a [ i ]+'_'
    elif re_a[i].startswith(m) and re_a[i].endswith(n) and re_a[i].isalnum():
        z = z+re_a[i].title()+'_'
    elif re_a[i].startswith(m) and re_a[i].endswith(m):
        z = z+re_a[i].replace('_', '').title()
    elif re_a[i].startswith(n) and re_a[i].endswith(m) and re_a[i].isalnum():
        z = z+re_a[i].title()
    elif re_a[i].startswith(sp) and re_a[i].endswith(sp) :
        z = z+'_'+re_a[i]
    elif re_a[i].startswith(n):
        z = z+'_'+re_a[i]
    else:
        z = z + re_a [ i ]
print(z)
print("AbcDefG12_3h4_Ij_$_#_1_2")