from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout, QLabel, QGraphicsDropShadowEffect
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt
import sys

app = QApplication(sys.argv)

# Main window
window = QWidget()
window.setWindowTitle("Instagram-Style Glowing Button")
window.setGeometry(100, 100, 300, 200)

# Button
button = QPushButton()
button.setFixedSize(131, 51)
button.setCursor(Qt.PointingHandCursor)
button.setEnabled(True)  # Initially ashy/inactive

# Inner layout for icon + text
layout = QHBoxLayout(button)
layout.setContentsMargins(10, 5, 10, 5)
layout.setSpacing(10)

# Icon
icon_label = QLabel()
pixmap = QPixmap("user_icon.png")  # Replace with your SVG/PNG icon
pixmap = pixmap.scaled(27, 27, Qt.KeepAspectRatio, Qt.SmoothTransformation)
icon_label.setPixmap(pixmap)
layout.addWidget(icon_label)

# Text
text_label = QLabel("Log In")
text_label.setStyleSheet("color: white; font-weight: 600;")
layout.addWidget(text_label)
layout.addStretch()

# Button style (ashy + hover effect)
button.setStyleSheet("""
QPushButton {
    border-radius: 15px;
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:1,
        stop:0 #2e8eff, stop:0.3 #2e8eff
    );
    background-color: #2e8eff;  /* solid bright blue */
    color: white;
}

/* Hover effect */
QPushButton:hover {
    background-color: rgba(46, 142, 255, 0.9);  /* brighter on hover */
}
""")

# Glow effect
glow = QGraphicsDropShadowEffect()
glow.setBlurRadius(30)
glow.setColor(QColor(46, 142, 255, 200))
glow.setOffset(0)
button.setGraphicsEffect(glow)

# Layout in main window
window_layout = QHBoxLayout(window)
window_layout.addWidget(button)
window_layout.setAlignment(Qt.AlignCenter)

window.show()

# Optional: Activate the button after 2 seconds to see the glow
from PySide6.QtCore import QTimer
QTimer.singleShot(2000, lambda: button.setEnabled(True))

sys.exit(app.exec())
