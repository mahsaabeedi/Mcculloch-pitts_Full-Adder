
x1=int(input("please insert x1:"))
x2=int(input("please insert x2:"))
teta1=-2
teta2=14
teta3=4
teta4=2
if -x2>=teta1:
    out1=1
else:
    out1=0
if x2>=teta1:
    out2=1
else:
    out2=0
if 4*x1-x2>=teta1:
    out3=1
else:
    out3=0
if -4*x1+x2<=teta2:
    out4=1
else:
    out4=0
if out1+out2+out3+out4>=teta3:
     print("correct")
else:
    print("error")
    









