def rangeCheck(data, typeData):
    if typeData == 0:
        if data > 1000 or data < 1:
            print('N')
    if typeData == 1:
        if data > 1000 or data < 0:
            print('N')
    if typeData == 2:
        for x in data:
            if x > 2 or x < 1:
                print('N')
def main():
    premiados = int(input())
    rangeCheck(premiados, 0)

    camisas   =  map(int, input().split())

    peqProduzidas = int(input())
    rangeCheck(peqProduzidas, 1)

    grandProduzidas = int(input())
    rangeCheck(grandProduzidas, 1)

    camisas = list(map(int, tOne))
    rangeCheck(tOne, 2)

    repPeq = camisas.count(1)
    repGrand = camisas.count(2)
    if (peqProduzidas + grandProduzidas) != len(camisas):
        print('N')
    if peqProduzidas != repPeq or grandProduzidas != repGrand:
        print('N')
    else:
        print('S')
main()
