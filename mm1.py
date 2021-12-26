import math
x = [1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972,
1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]
y = [12.20, 11.90, 11.15, 11.90, 11.50, 11.50, 11.00, 11.40, 11.00, 11.07,
11.08, 11.06, 10.97, 10.54, 10.82, 10.94, 11.12, 10.93, 10.78, 10.75, 10.71]
length=len(x)
sumx=0
sumy=0
#finding xmean and ymean
for i in range(length):
    sumx=sumx+x[i]
    sumy=sumy+y[i]
xmean=sumx/length
ymean=sumy/length
print("xmean is :")
print(xmean)
print("ymean is :")
print(ymean)
xi=[]
yi=[]
xii=0
yii=0
for i in range(length):
    xii=x[i]-xmean
    yii=y[i]-ymean
    xi.append(xii)
    yi.append(yii)
print("xi-xmean is : ")
print(xi)
print("yi-ymean is : ")
print(yi)
xiii=0
xisquare=[]
for i in range(length):
    xiii=xi[i]*xi[i]
    xisquare.append(xiii)
print("xi-xmean square is:")
print(xisquare)
denominator=0
for i in range(length):
    denominator=denominator+xisquare[i]
print(denominator)
yiii=0
yisquare=[]
for i in range(length):
    yiii=xi[i]*yi[i]
    yisquare.append(yiii)
print("xi-xmean*yi-ymean is :")
print(yisquare)
yiiis=0
yiisquare=[]
for i in range(length):
    yiiis=yi[i]*yi[i]
    yiisquare.append(yiiis)
print("yi-ymean square is :")
print(yiisquare)
yiisquares=0
for i in range(length):
    yiisquares=yiisquares+yiisquare[i]
print("summation of yi-ymean is:")
print(yiisquares)
numerator=0
for i in range(length):
    numerator=numerator+yisquare[i]    
print(numerator)
b1=numerator/denominator
print("B1 is ")
print(b1)
b1x=b1*xmean
b0=ymean-b1x
print("B0 is :")
print(b0)
a=denominator/length
sigmax=math.sqrt(a)
b=yiisquares/length
sigmay=math.sqrt(b)
sigmaxy=sigmax*sigmay
rsdenominator=length*sigmaxy
r=numerator/rsdenominator
rsquare=r*r
print("R^2 is : ")
print(rsquare)
print("Prediction:")
c=float(input("enter the year for prediction"))
if(c%4==0 and c!=2020):
    b1c=b1*c
    prediction=b1c+b0
    print("predction is")
    print(prediction)
elif(c==2021):
    b1c=b1*2020
    prediction=b1c+b0
    print("predction is")
    print(prediction)
elif(c==2020):
    print("THE OLYMPICS WERE SHIFTED TO 2021 SO TRY FOR 2021")
else:
    print("Sorry olympic were not held this year ")
