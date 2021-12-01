import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QSizePolicy
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from PyQt5.QtGui import QFont

from randomNumber import RandomNumber
from score import Score

class Gugudan(QWidget) :

    def __init__(self, parent=None):
        super().__init__(parent)

        

        #현재 점수 layout
        self.currentScore = QLabel(f"점수 : 0")
        self.currentScore.setFont(QFont("명조", 15))
        # self.currentScore.setStyleSheet("Color : rgb(255,255,255) ")
        # self.currentScore.setReadOnly(True)

        #남은 시간 layout
        self.leftTime = QLabel(f"남은 시간 : 60")
        self.leftTime.setFont(QFont("명조", 15))
        # self.leftTime.setStyleSheet("Color : green")
        # self.leftTime.setReadOnly(True)


        #구구단 문제 layout
        self.gugudanQuiz = QLineEdit(f"숫자 X num")
        self.gugudanQuiz.setReadOnly(True)
        self.gugudanQuiz.setAlignment(Qt.AlignCenter)
        #사이즈 픽셀로 설정
        self.gugudanQuiz.setFixedSize(280, 130)
        self.gugudanQuiz.setFont(QFont("명조", 20))
        # self.gugudanQuiz.setSizePolicy(0, QSizePolicy.Expanding)
        # font = self.gugudanQuiz.font()
        # font.setFamily('Courier New')
        # self.gugudanQuiz.setFont(font)

        #정답 :
        self.resultText = QLabel("정답 : ")
        self.resultText.setFont(QFont("명조", 20))
        #정답 입력창 layout
        self.enterResult = QLineEdit("1")
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

        #메인보드
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(gugudanLayout, 0, 0)
        mainLayout.addLayout(scoreBoardLayout, 0, 1)
        
        self.setLayout(mainLayout)
        self.setWindowTitle('업그레이드 구구단')

        #타이머
        self.timer = QTimer(self)
        self.timer.start(100)
        self.timer.timeout.connect(self.updateTime)

        # self.startGame()

        #게임 상태
        self.onGame = False

    #게임 시작
    def startGame(self):
        self.onGame = True

        #초기 점수
        self.score = 0

        #초기 남은 시간 설정
        self.time = 60.1

        self.gameScore = Score()
        self.newQuiz()

    #새로운 구구단 생성
    def newQuiz(self) :
        self.gugudan = RandomNumber()
        self.gugudanQuiz.setText(f"{self.gugudan.operands()[0]} X {self.gugudan.operands()[1]}")

    #점수 갱신
    def updateScore(self) :
        self.currentScore.setText(f"점수 : {self.score}")
        

    #남은 시간 갱신
    def updateTime(self) :
        if self.onGame :
            self.time = round(self.time - 0.1, 1)
            if self.time == 0 :
                self.onGame = False
                self.gameOver()
            self.leftTime.setText(f"남은 시간 : {self.time}")
            

    #버튼 입력 (enter, spacebar)
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.submit()
        # elif e.key() == Qt.Key_Space:
        #     self.pause()
        # elif e.key() == Qt.Key_N:
        #     self.showNormal()

    #정답 제출
    def submit(self) :
        
        # self.close()
        self.ipt = self.enterResult.text()
        self.enterResult.clear()
        self.enterResult.setText("")
        if self.onGame :
            if self.gugudan.checkAnswer(int(self.ipt)):
                self.score = self.gameScore.correct(self.score)
                self.updateScore()
                self.newQuiz()
            else :
                pass
    
    #잠시 대기
    def pause(self) :
        self.close()

    def gameOver(self) :
        pass
            
            

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    game = Gugudan()
    game.setGeometry(300,300, 300,500)
    game.show()
    sys.exit(app.exec_())