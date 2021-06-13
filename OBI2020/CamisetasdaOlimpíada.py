def rangeCheck(data, typeData):
    if typeData == 1:
        if data > 1000 or data < 0:
            print('N')
    if typeData == 0:
        if data > 1000 or data < 1:
            print('N')
    if typeData == 2:
        for x in data:
            if x > 2 or x < 1:
                print('N')
def main():
    premiados = int(input())
    rangeCheck(premiados, 0)

    tOne   =  map(int, input().split())

    peqProduzidas = int(input())
    rangeCheck(peqProduzidas, 1)

    grandProduzidas = int(input())
    rangeCheck(grandProduzidas, 1)

    tOne = list(map(int, tOne))
    rangeCheck(tOne, 2)

    repPeq = tOne.count(1)
    repGrand = tOne.count(2)
    if (peqProduzidas + grandProduzidas) != len(tOne):
        print('N')
        return 'N'
    if peqProduzidas != repPeq or grandProduzidas != repGrand:
        print('N')
        return 'N'
    else:
        print('S')
        return 'S'

main()
