# Kristen Harrison, CS 325, HW 4


# activity class has attributes id, start, and finish times
class Activity:
    def __init__(self, id, start, finish):
        self.id = id
        self.start = start
        self.finish = finish


# receives an activity list and returns a maximal-size
# subset of mutually compatible activities
def selectActs(list):

    # add first greedy choice and track index
    solutionSet = []
    solutionSet.append(list[0])
    lastAdded = 0

    # iterate through rest of set
    for i in range(1, len(list)):
        # first activity found that is compatible with the last
        # added activity will have the latest start time of all
        # compatible activities because sort is descending by start time
        if list[i].finish <= list[lastAdded].start:
            solutionSet.append(list[i])
            lastAdded = i

    return solutionSet



# modified merge function sorts by start time descending
def merge(left, right):
    result = []

    # while both are not empty
    while (left and right):
        if (left[0].start >= right[0].start):
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    # copy elements left over in one of the lists
    while(left):
        result.append(left[0])
        left = left[1:]

    while(right):
        result.append(right[0])
        right = right[1:]

    return result;



def mergeSort(size, arr):
    if(size <= 1):
        return arr;

    left = arr[0:size//2]
    right = arr[size//2:]

    left = mergeSort(len(left), left)
    right = mergeSort(len(right), right)

    return merge(left, right);





file_in = open('act.txt', 'r')
set = 1

for line in file_in:
    nums = int(line)
    activityList = []

    # reads in each activity in the set, instantiates
    # an object for it, and adds it to the list
    for i in range(nums):
        nextLine = file_in.readline().strip()
        arr = list(map(int, nextLine.split()))
        if (len(arr) == 3):
            newAct = Activity(arr[0], arr[1], arr[2])
        activityList.append(newAct)

    # sort by start time in descending order
    #activityList.sort(key=lambda x: x.start, reverse=True)
    activityList = mergeSort(len(activityList), activityList)

    # format solution set
    solution = selectActs(activityList)
    solutionString = ""

    # read in activities in reverse order (low to high)
    for i in range(len(solution)-1, -1, -1):
        solutionString = solutionString + str(solution[i].id) + " "

    print("Set", set)
    print("Number of activities selected =", len(solution))
    print("Activities: ", solutionString, '\n')

    set = set+1

file_in.close()



