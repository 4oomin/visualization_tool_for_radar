import os
from Pkg.config import *
from Pkg.data import *
from Pkg.window import *

if __name__ == "__main__":
    #RAD ver
    cfg = Config("RAD6")

    #Input 파일 읽기
    files = os.listdir(".\\Input")
    #data = Data(cfg, files[0])

    #gui 실행
    app = QApplication(sys.argv)
    gui = Window(cfg,files)
    gui.show()
    app.exec_()
    pass