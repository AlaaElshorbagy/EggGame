#AlaaElshorbagy
#19Nov19

n=int(input('Enter a positive integer: '))
#FullList=list(range(1,n+1))
EvenList=list(range(2,n+1,2))
OListOfSplits=list()

j=len(EvenList)
i=1
while True:
 if j-i>=0:
        OListOfSplits.append(EvenList[j-i:j])
 else:
    if j!=0:
        OListOfSplits.append(EvenList[0:j])
    break
 j=j-i
 i=i+1

print('The number of trials in worst case scenario= ', len(OListOfSplits),'\n')

print('Drop the egg from the following floors (keep the order):')

for i in range(-1,-len(OListOfSplits)-1,-1):
    print(OListOfSplits[i][-1])

#print('\n',OListOfSplits)
