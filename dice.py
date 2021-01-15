import random as rn
import statistics as st
def dice():
    return rn.randint(1,6)
mydata=[]
for i in range(100):
    mydata.append(dice())
print(st.mean(mydata),st.stdev(mydata))
