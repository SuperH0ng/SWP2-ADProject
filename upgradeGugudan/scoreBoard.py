# # scoreList = [4,3,2,1,0]

# # def updateScoreBoard(score) :
# #     scoreList.append(score)
# #     scoreList = scoreList

# class ScoreBoard :
#     def __init__(self) :
        
f = open("scoreBoard.txt", "w+")

numList = [10]

while True:
    c = f.readline()
    if c == '':
        break
    c = c[:len(c)-1]
    numList.append(int(c))

numList = sorted(numList, reverse=True)[:5]
numList = list(map(lambda x : f"{x}\n", (n for n in numList)))

f.writelines(numList)
f.close()

print(numList)