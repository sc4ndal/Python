import operator

trainDic, trainList1,trainList2 = {},[],[]
trainDic = {'Thomas':'토마스','Edward':'에드워드','henry':'헨리','Gothen':'고든','James':'제임스'}
# trainList1 = sorted(reverse=True)(trainDic.items(),key= operator.itemgetter(0))
# trainList1 = list(sort(trainDic.items(),key=operator.itemgetter(0),reverse=True))
trainList2 = sorted(trainDic.items(),key= operator.itemgetter(0))
# print(trainList1)
print(trainList2)