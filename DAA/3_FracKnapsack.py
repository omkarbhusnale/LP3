# PR-3 Fraction Knapsack 

val = [[60,10],[100, 20],[120,30]]
W = 50

values = sorted(val, key=lambda x:x[0]/x[1], reverse=True)

profit=0

for item in val:
    if W >= item[1]:
        profit += item[0]
        W -= item[1]
    else:
        profit += (item[0]/item[1]) * W
        break
print("%.2f" % profit)