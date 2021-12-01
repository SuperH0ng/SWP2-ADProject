class ScoreBoard :
    def __init__(self):
        self.numList = []
        with open("scoreBoard.txt", "r") as f :
            while True:
                c = f.readline()
                if c == '':
                    break
                c = c[:len(c)-1]
                self.numList.append(int(c))
    
    def updateBestScore(self, num) :
        self.numList.append(num)
        self.numList = sorted(self.numList, reverse=True)[:5]
        self.numList = list(map(lambda x : f"{x}\n", (n for n in self.numList)))

        with open("scoreBoard.txt", "w") as f :
            
            f.writelines(self.numList)

        # print(self.numList)

    def resetScoreBoard(self) :
        with open("scoreBoard.txt", "w") as f :
            
            f.writelines(["\n"])