# Python Program to Find HCF of numbers of a list

def find_hcf(list):
    def elementsOfSpecificCount(factors,lengthOfMainList):
        listWithSimilarCounts = []
        for i in range(0,len(factors)):
            if factors.count(factors[i])==lengthOfMainList:
                listWithSimilarCounts.append(factors[i])
        return listWithSimilarCounts

    def findFactors(number):
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        return factors

    lengthOfList = len(list)
    all_factors = []
    for i in range(0, lengthOfList):
        k = 0
        while k<len(findFactors(list[i])):
            all_factors.append(findFactors(list[i])[k])
            k=k+1
    temp = []
    temp = elementsOfSpecificCount(all_factors,lengthOfList)
    temp.sort()
    return temp[len(temp)-1]


l = [24, 54]
print(find_hcf(l))
