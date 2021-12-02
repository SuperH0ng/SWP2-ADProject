numberDic = {
1: ["1", "일", "하나", "One", "一", "I", "0001b"],
2: ["2", "이", "둘", "Two", "二" , "II", "0010b"],
3: ["3", "삼", "셋", "Three", "三", "III", "0011b"],
4: ["4", "사", "넷", "Four", "四", "IV", "0100b"],
5: ["5", "오", "다섯", "Five", "五", "V", "0101b"],
6: ["6", "육", "여섯", "Six", "六", "VI", "0110b"],
7: ["7", "칠", "일곱", "Seven", "七", "VII", "0111b"],
8: ["8", "팔", "여덟", "Eight", "八", "VIII", "1000b"],
9: ["9", "구", "아홉", "Nine", "九", "IX", "1001b"]
}


import random
class RandomNumber :

    def __init__(self) :
        #랜덤 피연산자 생성
        self.operand1 = random.randint(1,9)
        self.operand2 = random.randint(1,9)
        self.answerNum = self.operand1 * self.operand2

        #랜덤 피연산자 타입 
        self.operand1Type = random.randint(0,6)
        self.operand2Type = random.randint(0,6)

    def operands(self) :
        return [numberDic[self.operand1][self.operand1Type], numberDic[self.operand2][self.operand2Type]]
        # return [numberDic[9][5], numberDic[6][4]]

    #
    def checkAnswer(self, num) : 
        return self.answerNum == num