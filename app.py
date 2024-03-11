# barnemi benvisid ke list az adad ra gerefteh va tamami adad moshabeh ra hazf konad va az on add tanha yek add baghi bemand.
a=[1,2,3,4,4,4,4,5,6,3,2,1,21,58,8]

emptyList=[]

for i in a:
    if i not in emptyList:
        emptyList.append(1)
        
print();

# برنامه ای بنویسید  که * * * * * * * * * 
#   * * * * * * * *
#    * * * * * * * 
#     * * * * * *
#      * * * * *
#       * * * *
#        * * *
#         * *
#          *
n=9
 
for i in range(n , 8 , -1):
  print("",end="")
  for j in range(i):
    print("*",end="")
    print()
    
    
#برنامه ای بنویسید که لیستی از اعداد را از ورودی دریافت و تمامی اعدادی را که بر صفر تقسیم میشوند را نمایش دهد
m=[]


for i in range (2):
    x= int(input("Please enter number"))
    m.append(x)
       
try:
    for i in m:
        print(1/8)
except ZeroDivisionError:
    print("salam")
except:
    print("error khodemon")    
    
    # yek add az vproodi begir va tedad argham an ra beshmared
num=str(input('please enter a number:'))
count=0
for i in num:
    count+=1
    print(count)