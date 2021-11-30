numberDic = {1: ["1", "일", "하나", "One", "一", "I"],
2: ["2", "이", "둘", "Two", "二" , "II"], 3: ["3", "삼", "셋", "Three", "三", "III"],
4: ["4", "사", "넷", "Four", "四", "IV"], 5:["5", "오", "다섯", "Five", "五", "V"],
6: ["6", "육", "여섯", "Six", "六", "VI"], 7: ["7", "칠", "일곱", "Seven", "七", "VII"],
8: ["8", "팔", "여덟", "Eight", "八", "VIII"], 9:["9", "구", "아홉", "Nine", "九", "IX"]}

import random
class RandomNumber :

    def __init__(self) :
        self.operand1 = random.randint(1,9)
        self.operand2 = random.randint(1,9)

        self.operand1Type = random.randint(0,5)
        self.operand2Type = random.randint(0,5)

        self.answerNum = self.operand1 * self.operand2

    def operands(self) :
        return [numberDic[self.operand1][self.operand1Type], numberDic[self.operand2][self.operand2Type]]

    def checkAnswer(self, num) : 
        return self.answerNum == num