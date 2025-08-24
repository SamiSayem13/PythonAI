import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Main Window")
    window.resize(600, 400)  # normal window size

    pixmap = QPixmap(r"C:\Users\Zeus\Desktop\PythonProject\Garbage_python_code\load.jpg")
    if pixmap.isNull():
        print("❌ Failed to load image")
        sys.exit(1)

    # Make it wide
    small_pixmap = pixmap.scaled(1280, 1980, aspectRatioMode=1)  # wide landscape

    label = QLabel()
    label.setPixmap(small_pixmap)

    layout = QVBoxLayout()
    layout.addWidget(label)
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec_())
