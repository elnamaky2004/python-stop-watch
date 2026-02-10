import sys
from PyQt5.QtWidgets import (QApplication, QPushButton, QVBoxLayout, QWidget
                             , QHBoxLayout, QLabel)
from PyQt5.QtCore import QTimer, QTime,Qt
class timer_app(QWidget):
    def __init__(self):
        super().__init__()
        self.time =QTime(0,0,0,0)
        self.time_label=QLabel(self.time.toString("00:00:00.00"),self)
        self.start_button=QPushButton("Start",self)
        self.stop_button=QPushButton("Stop",self)
        self.reset_button=QPushButton("Reset",self)
        self.timer=QTimer(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setGeometry(100,100,300,200)
        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.time_label.setAlignment(Qt.AlignCenter)
        hbox=QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        #style
        self.time_label.setStyleSheet("font-size: 28px; font-weight: bold;")
        #buttons clicked
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        #timer config
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_time)
        #initial state
        self.stop_button.setEnabled(False)
    def start(self):
        if not self.timer.isActive():
            self.timer.start()
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
    def stop(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
    def reset(self):
        self.timer.stop()
        self.time=QTime(0,0,0,0)
        self.time_label.setText(self.time.toString("00:00:00.00"))
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
    def format_time(self):
        # mm:ss:zz
        minutes=self.time.minute()
        seconds=self.time.second()
        milliseconds=self.time.msec()
        return f"{minutes:02d}:{seconds:02d}:{milliseconds//10:02}"
    def update_time(self):
        self.time =self.time.addMSecs(10)
        self.time_label.setText(self.format_time())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer = timer_app()
    timer.show()
    sys.exit(app.exec_())