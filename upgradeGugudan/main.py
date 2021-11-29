import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QSizePolicy
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from PyQt5.QtGui import QFont

from randomNumber import RandomNumber
from score import Score


class Gugudan(QWidget) :

    def __init__(self, parent=None):
        super().__init__(parent)

        #초기 점수
        self.priScore = 0

        #초기 남은 시간 설정
        self.time = 60

        #피연산자
        self.operand1 = 0
        self.operand2 = 0

        #현재 점수 layout
        self.currentScore = QLabel(f"점수 : {self.priScore}")
        self.currentScore.setFont(QFont("명조", 15))
        # self.currentScore.setStyleSheet("Color : rgb(255,255,255) ")
        # self.currentScore.setReadOnly(True)

        #남은 시간 layout
        self.leftTime = QLabel(f"남은 시간 : {self.time}")
        self.leftTime.setFont(QFont("명조", 15))
        # self.leftTime.setStyleSheet("Color : green")
        # self.leftTime.setReadOnly(True)


        #구구단 문제 layout
        self.gugudanQuiz = QLineEdit(f"{self.operand1} X {self.operand2}")
        self.gugudanQuiz.setReadOnly(True)
        self.gugudanQuiz.setAlignment(Qt.AlignCenter)
        self.gugudanQuiz.setFont(QFont("명조", 20))
        # self.gugudanQuiz.setSizePolicy(0, QSizePolicy.Expanding)
        # font = self.gugudanQuiz.font()
        # font.setFamily('Courier New')
        # self.gugudanQuiz.setFont(font)

        #정답 :
        self.resultText = QLabel("정답 : ")
        self.resultText.setFont(QFont("명조", 20))
        #정답 입력창 layout
        self.enterResult = QLineEdit()
        self.enterResult.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        self.enterResult.setMaxLength(2)
        self.enterResult.setFont(QFont("명조", 20))
        #새 게임
        self.newGameButton = QToolButton()
        self.newGameButton.setText('새 게임')
        self.newGameButton.clicked.connect(self.startGame)


        #게임창
        gugudanLayout = QGridLayout()
        gugudanLayout.addWidget(self.currentScore, 0, 0)
        gugudanLayout.addWidget(self.leftTime, 0, 2)
        gugudanLayout.addWidget(self.gugudanQuiz, 1, 0, 3, 3)
        gugudanLayout.addWidget(self.resultText, 4, 0)
        gugudanLayout.addWidget(self.enterResult, 4, 1)
        gugudanLayout.addWidget(self.newGameButton, 4, 2, alignment=Qt.AlignRight)

        
        #BEST SCORE text layout
        self.bestScore = QLabel("최고 점수")
        self.bestScoreFont = self.bestScore.font()
        self.bestScoreFont.setPointSize = 20
        self.bestScore.setFont(self.bestScoreFont)


        #점수 목록 layout
        self.scores = QTextEdit("")
        self.scores.setReadOnly(True)
        self.scores.setAlignment(Qt.AlignLeft)

        # self.scores

        #스코어보드
        scoreBoardLayout = QGridLayout()
        scoreBoardLayout.addWidget(self.bestScore, 0, 0)
        scoreBoardLayout.addWidget(self.scores, 1, 0)

        # scoreBoardLayout = QGridLayout()

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(gugudanLayout, 0, 0)
        mainLayout.addLayout(scoreBoardLayout, 0, 1)
        
        self.setLayout(mainLayout)

        self.setWindowTitle('업그레이드 구구단')


    
    def startGame(self):
        self.score = Score()
        self.gugudan = RandomNumber()
        
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Enter:
            self.submit()
        elif e.key() == Qt.Key_Space:
            self.pause()
        # elif e.key() == Qt.Key_N:
        #     self.showNormal()

    def submit(self) :
        ipt = self.enterResult.text()

        self.enterResult.clear()

        if self.gugudan.checkAnswer(ipt) :
            self.gugudan = RandomNumber()
            self.score.correct()
            self.currentScore.setText(f"점수 : {self.score}")
        else :
            pass

            
            

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    game = Gugudan()
    game.setGeometry(300,300, 300,500)
    game.show()
    sys.exit(app.exec_())