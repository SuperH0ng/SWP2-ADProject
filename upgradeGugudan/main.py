import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QSizePolicy
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from PyQt5.QtGui import QFont

from randomNumber import RandomNumber
from score import Score
from scoreBoard import ScoreBoard

class Gugudan(QWidget) :

    def __init__(self, parent=None):
        super().__init__(parent)

        #현재 점수 layout
        self.currentScore = QLabel(f"점수 : 0")
        self.currentScore.setFont(QFont("명조", 15))

        #남은 시간 layout
        self.timeLimit = 5
        self.leftTime = QLabel(f"남은 시간 : {self.timeLimit}")
        self.leftTime.setFont(QFont("명조", 15))

        #구구단 문제 layout
        self.gugudanQuiz = QLineEdit(f"업그레이드 구구단")
        self.gugudanQuiz.setReadOnly(True)
        self.gugudanQuiz.setAlignment(Qt.AlignCenter)
        #사이즈 픽셀로 설정
        self.gugudanQuiz.setFixedSize(280, 130)
        self.gugudanQuiz.setFont(QFont("명조", 20))

        #정답 :
        self.resultText = QLabel("정답 : ")
        self.resultText.setFont(QFont("명조", 20))

        #정답 입력창 layout
        self.enterResult = QLineEdit("")
        self.enterResult.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        self.enterResult.setMaxLength(2)
        self.enterResult.setFont(QFont("명조", 20))

        #새 게임
        self.newGameButton = QToolButton()
        self.newGameButton.setText('새 게임')
        self.newGameButton.clicked.connect(self.startGame)
        self.newGameButton.setFont(QFont("명조", 15))
        self.newGameButton.setFixedSize(80, 40)

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
        self.bestScore.setFont(QFont("명조", 20))
        self.bestScore.setStyleSheet("Color : blue")

        #scoreBoard 초기화 버튼
        self.resetBtn = QToolButton()
        self.resetBtn.setText('ScoreBoard\n 초기화')
        self.resetBtn.clicked.connect(self.reset)

        #점수 목록 layout
        self.scores = QTextEdit("")
        self.scores.setFixedSize(220, 190)
        self.scores.setReadOnly(True)
        self.scores.setAlignment(Qt.AlignLeft)
        self.scores.setFont(QFont("명조", 23))

        #스코어보드
        scoreBoardLayout = QGridLayout()
        scoreBoardLayout.addWidget(self.bestScore, 0, 0)
        scoreBoardLayout.addWidget(self.scores, 1, 0, 2, 0)
        scoreBoardLayout.addWidget(self.resetBtn, 0, 1)

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

        #스코어보드
        self.bestScores = ScoreBoard()
        self.updateScoreBoard()

        #게임 상태
        self.onGame = False
        self.gameStop = False

    #게임 시작
    def startGame(self):
        self.onGame = True
        self.gameStop = False
        self.enterResult.setReadOnly(False)

        #초기 점수
        self.score = 0
        self.updateScore()

        #초기 남은 시간 설정
        self.time = self.timeLimit + 0.1
        self.updateTime()

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
        #게임이 진행 중이고, pause를 누르지 않았을 때
        if self.onGame and not self.gameStop:
            self.time = round(self.time - 0.1, 1)
            if self.time == 0 :
                self.onGame = False
                self.gameOver()
            self.leftTime.setText(f"남은 시간 : {self.time}")
            
    #버튼 입력 (enter, escape)
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.submit()
        elif e.key() == Qt.Key_Escape:
            self.pause()

    #정답 제출
    def submit(self) :
        if not self.gameStop :
            self.ipt = self.enterResult.text()
            self.enterResult.clear()
            self.enterResult.setText("")
            if self.onGame :
                try :
                    if self.gugudan.checkAnswer(int(self.ipt)):
                        self.score += 1
                        self.updateScore()
                        self.newQuiz()
                except :
                    pass

    #잠시 대기
    def pause(self) :
        if self.gameStop :
            self.enterResult.setReadOnly(False)
            self.gameStop = False
        else :
            self.enterResult.setReadOnly(True)
            self.gameStop = True

    #게임 종료
    def gameOver(self) :
        self.enterResult.setReadOnly(True)
        self.enterResult.clear()
        self.bestScores.updateBestScore(int(self.currentScore.text()[5:]))
        self.updateScoreBoard()

    #스코어보드 갱신
    def updateScoreBoard(self) :
        x = ""
        for i in range(len(self.bestScores.numList)) :
            if i != 4 :
                x += f"{i+1}등\t {self.bestScores.numList[i]}점\n"
            else :
                x += f"{i+1}등\t {self.bestScores.numList[i]}점"
        self.scores.setText(x)

    #점수 초기화
    def reset(self):
        self.bestScores = ScoreBoard()
        self.bestScores.resetScoreBoard()
        # self.bestScores.numList = []
        self.updateScoreBoard()

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    game = Gugudan()
    # game.setGeometry(300,300, 300,500)
    game.show()
    sys.exit(app.exec_())