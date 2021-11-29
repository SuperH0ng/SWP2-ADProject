class Score :
    def __init__(self, score):
        self.presentScore = score
    
    def correct(self) :
        self.presentScore += 1
        # return score + 1