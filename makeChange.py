# Kristen Harrison, CS 325, HW3


# Takes as parameters an array of denomination values and change amount
# Returns the min number of coins and how many of each denomination
def makeChange(currency, changeAmount):
    A = changeAmount

    # store optimal solution, initialized at infinity
    minArray = [float('inf') for i in range(A+1)]

    # base case is zero if change amount is zero
    minArray[0] = 0

    # store coin denomination used last to reverse engineer how many of each
    coinUsed = [-1 for i in range(A+1)]

    # tabulate how many of each denomination
    denoms = [0 for i in range(len(currency))]


    # solve each subproblem
    for a in range(1, A+1):
        for i in range(len(currency)):
            # change amount is greater than coin value
            # and current solution > previous solution plus 1
            if a >= currency[i] and minArray[a] > 1 + minArray[a - currency[i]]:
                # update solution and record coin used
                minArray[a] = 1 + minArray[a - currency[i]]
                coinUsed[a] = i


    # check coin denomination used in last index
    solutionIndex = A
    #coinType = coinUsed[solutionIndex]

    # derive coins used and save to denoms
    while solutionIndex > 0:
        coinType = coinUsed[solutionIndex]
        # record coin used
        denoms[coinType] = denoms[coinType] + 1
        # update subproblem index and coin denomination
        solutionIndex = solutionIndex - currency[coinType]

    return minArray[A], denoms



file_in = open('amount.txt', 'r')
file_out = open('change.out', 'w')

for line in file_in:
    file_out.write(line)
    currency = list(map(int, line.split()))

    nextLine = file_in.readline().strip()
    file_out.write(nextLine + '\n')
    changeAmount = int(nextLine)

    total, denominations = makeChange(currency, changeAmount)
    coinsNeeded = ' '.join(str(x) for x in denominations) + '\n'
    file_out.write(coinsNeeded)
    file_out.write(str(total) + '\n')

file_in.close()
file_out.close()







