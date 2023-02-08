import copy
import math

T = int(input())

def charToBin(char):
    if(char == "A"):
        return 8
    elif(char == "B"):
        return 4
    elif(char == "C"):
        return 2
    elif(char == "D"):
        return 1



# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    activityString = input()
    currentArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    previousArray = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    ans = 0
    for char in activityString:
        binChar = charToBin(char)
        for currentBin in range(16):
            if(currentBin & binChar != 0 ):
                for previousBin in range(16):
                    if(previousBin & currentBin != 0):
                        currentArray[currentBin] += previousArray[previousBin]
        ans = sum(currentArray) % 1000000007
        previousArray = copy.deepcopy(currentArray)
        currentArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ansLine = "#" + str(test_case) + " " + str(ans)
    print(ansLine)

