# Kristen Harrison, CS 325, HW3
import random
import time


def makeChange(currency, changeAmount):
    A = changeAmount

    # store optimal solution
    minArray = [float('inf') for i in range(A+1)]
    minArray[0] = 0

      # solve each subproblem
    for a in range(1, A+1):
        for i in range(len(currency)):
            # change amount is greater than coin value
            # and current solution > previous solution plus 1
            if a >= currency[i] and minArray[a] > 1 + minArray[a - currency[i]]:
                minArray[a] = 1 + minArray[a - currency[i]]

    return minArray




# generates a coin system starting at 1
# and increasing until array is size numCoins
def generateCurrency(numCoins):
    arr = []
    arr.append(1)
    for i in range(numCoins - 1):
        arr.append(arr[i] + random.randint(1, 10))
    return arr;


def runMakeChange(numCoins, amount):
    currency = generateCurrency(numCoins)

    # time sorting in ms
    start = time.time()
    resultArray = makeChange(currency, amount)
    finish = time.time()
    elapsed = (finish - start) * 1000
    #print(resultArray)
    print("currency:", numCoins, "amount:", amount, "time:", elapsed)
    #return elapsed

'''
runMakeChange(1000, 100)
runMakeChange(1000, 200)
runMakeChange(1000, 300)
runMakeChange(1000, 400)
runMakeChange(1000, 500)
runMakeChange(1000, 600)
print('\n')
runMakeChange(300, 300)
runMakeChange(600, 300)
runMakeChange(900, 300)
runMakeChange(1200, 300)
runMakeChange(1500, 300)
runMakeChange(1800, 300)
print('\n')
'''
runMakeChange(300, 10000)
runMakeChange(600, 20000)
runMakeChange(900, 30000)
runMakeChange(1200, 40000)
runMakeChange(1500, 50000)
runMakeChange(1800, 60000)






'''
def avgSort(size):
    avgElapsed = (runSort(size) + runSort(size) + runSort(size))/3
    print(size, avgElapsed, "\n")
    return
'''



