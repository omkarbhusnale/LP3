# PR-5 NQueen problem

def queen(n):
  def backtrack(i):
    if i==n:
      result.append(list(row))
    for j in range(n):
      if j not in col and j-i not in dig and  j+i not in ofdig:
        col.add(j)
        dig.add(j-i)
        ofdig.add(j+i)
        row.append("_"*j+"Q"+"_"*(n-j-1))
        backtrack(i+1)

        col.remove(j)
        dig.remove(j-i)
        ofdig.remove(j+i)
        row.pop()
  
  result=[]
  row=[]
  col=set()
  dig=set()
  ofdig=set()
  backtrack(0)
  return result


pp=int(input("Enter a Num: "))
p=queen(pp)
for j in p[0]:
  for i in j:
    print(i,end=" ")
  print()
  