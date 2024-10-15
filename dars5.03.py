# import sys
# from PyQt6.QtWidgets import QApplication, QWidget
#
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Eng sodda misol!")
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# sys.exit(app.exec())
# import sys
# from PyQt6.QtCore import Qt
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(100, 100, 1366,768)
#
#         label = QLabel("A simple label with ths text")
#
#         layout = QVBoxLayout()
#
#         layout.addWidget(label,alignment=Qt.AlignmentFlag.AlignCenter)
#
#         self.setLayout(layout)
#
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
#
# sys.exit(app.exec())
# import sys
# from PyQt6.QtWidgets import  QApplication,QWidget,QLabel,QVBoxLayout,QHBoxLayout,QScrollArea
#
# class ScrollableWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         layout = QVBoxLayout()
#
#         for i in range(1, 100):
#             label = QLabel(f"Label {i}")
#             layout.addWidget(label)
#
#         content_widget = QWidget()
#
#         content_widget.setLayout(layout)
#
#         scroll_area = QScrollArea()
#         scroll_area.setWidgetResizable(True)
#         scroll_area.setWidget(content_widget)
#
#         main_layout = QHBoxLayout()
#         main_layout.addWidget(scroll_area)
#
#         self.setLayout(main_layout)
#         self.setWindowTitle("ScrollableWidget")
#
# app = QApplication(sys.argv)
# window = ScrollableWidget()
# window.show()
# sys.exit(app.exec())
# import sys
# from PyQt6.QtCore import Qt
# from PyQt6.QtGui import QMouseEvent
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
#
#
# class EventHandlingWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.label = QLabel("Try clicking, dragging, or pressing keys.", self)
#         self.label.setStyleSheet("border: 1px solid black; padding: 10px;")
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.label)
#         self.setLayout(layout)
#
#         self.setWindowTitle("Event Handling Example")
#         self.setGeometry(100, 100, 400, 200)
#
#     def mousePressEvent(self, event):
#         if event.button() == Qt.MouseButton.LeftButton:
#             self.label.setText("Left mouse button clicked!")
#         elif event.button() == Qt.MouseButton.RightButton:
#             self.label.setText("Right mouse button clicked!")
#
#     def mouseMoveEvent(self, event):
#         position = event.pos()
#         self.label.setText(f"Dragging at {position.x()}, {position.y()}")
#
#     def keyPressEvent(self, event):
#         match event.key():
#             case Qt.Key.Key_A:
#                 self.label.setText("Key 'A' pressed!")
#                 self.label.setStyleSheet("color: red;")
#             case Qt.Key.Key_Escape:
#                 self.label.setText("Escape key pressed!")
#                 self.label.setStyleSheet("color: lightgray;")
#
#     def mouseReleaseEvent(self, event: QMouseEvent):
#         position = event.pos()
#         self.label.setText(f"Mouse button released! {position}")
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = EventHandlingWindow()
#     window.show()
#     sys.exit(app.exec())
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QComboBox, QSpinBox, QCheckBox, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
#
#
# class SimpleForm(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.first_name_label = QLabel("First name:")
#         self.first_name_input = QLineEdit(self)
#
#         self.last_name_label = QLabel("Last name:")
#         self.last_name_input = QLineEdit(self)
#
#         self.age_label = QLabel("Age:")
#         self.age_input = QSpinBox(self)
#         self.age_input.setRange(1, 150)
#
#         self.bio_label = QLabel("Biography:")
#         self.bio_input = QTextEdit(self)
#
#         self.gender_label = QLabel("Gender:")
#         self.gender_input = QComboBox(self)
#         self.gender_input.addItems(["Mujik", "Ayol"])
#
#         self.terms_checkbox = QCheckBox("I agree to the terms and conditions.")
#
#         self.submit_button = QPushButton("Submit")
#         self.submit_button.clicked.connect(self.submit_form)
#
#         layout = QVBoxLayout()
#
#         layout.addWidget(self.first_name_label)
#         layout.addWidget(self.first_name_input)
#
#         layout.addWidget(self.last_name_label)
#         layout.addWidget(self.last_name_input)
#
#         layout.addWidget(self.age_label)
#         layout.addWidget(self.age_input)
#
#         layout.addWidget(self.bio_label)
#         layout.addWidget(self.bio_input)
#
#         layout.addWidget(self.gender_label)
#         layout.addWidget(self.gender_input)
#
#         layout.addWidget(self.terms_checkbox)
#
#         layout.addWidget(self.submit_button)
#
#         self.setLayout(layout)
#         self.setWindowTitle("Simple User Input Form")
#
#     def submit_form(self):
#         first_name = self.first_name_input.text()
#         last_name = self.last_name_input.text()
#         age = self.age_input.value()
#         bio = self.bio_input.toPlainText()
#         gender = self.gender_input.currentText()
#         terms_accepted = self.terms_checkbox.isChecked()
#
#         if not terms_accepted:
#             QMessageBox.warning(self, "Terms Not Accepted", "Please accept the terms and conditions.")
#             return
#
#         QMessageBox.information(self, "Form Submitted", f"First Name: {first_name}\nLast Name: {last_name}\nAge: {age}\nGender: {gender}\nBio: {bio}")
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     form = SimpleForm()
#     form.show()
#     sys.exit(app.exec())
# import sys
# from PyQt6.QtCore import Qt
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea, QMessageBox
# from widgets import SimpleForm
#
#
# class ScrollableWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.records_layout = QVBoxLayout(self)
#         self.records_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
#
#         self.content_widget = QWidget()
#
#         self.content_widget.setLayout(self.records_layout)
#
#         scroll_area = QScrollArea()
#         scroll_area.setWidget(self.content_widget)
#         scroll_area.setWidgetResizable(True)
#
#         self.form = SimpleForm()
#         self.form.form_submitted.connect(self.update_records_list)
#
#         main_layout = QHBoxLayout()
#         main_layout.addWidget(self.form)
#         main_layout.addWidget(scroll_area)
#
#         self.setLayout(main_layout)
#         self.setWindowTitle("Scroll qilsa bo'ladigan oyna")
#
#     def update_records_list(self, name: str, surname: str, age: int, gender: str, bio: str):
#         if self.records_layout.count() + 1 <= 20:
#             count = self.records_layout.count() + 1
#             new_record = QLabel(f"{count}. Name: {name}, Surname: {surname}, Age: {age}, Gender: {gender}, Bio: {bio}")
#             new_record.setStyleSheet(f"background-color: {"gray" if count % 2 == 0 else "black"}; padding: 10px;")
#             self.records_layout.addWidget(new_record, alignment=Qt.AlignmentFlag.AlignTop)
#         else:
#             QMessageBox.warning(self, "Limit reached", "20tadan ortiq kiritish mumkin emas!")
#
#
#
#
# app = QApplication(sys.argv)
# window = ScrollableWindow()
# window.show()
# sys.exit(app.exec())
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
#
# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         layout = QVBoxLayout()
#
#         family_name = "VASTELORD"
#         first_name = "VASTO"
#         last_name = "LORDE"
#
#         label_family = QLabel(f"Familiya: {family_name}")
#         label_first = QLabel(f"Ism: {first_name}")
#         label_last = QLabel(f"Sharif: {last_name}")
#
#         layout.addWidget(label_family)
#         layout.addWidget(label_first)
#         layout.addWidget(label_last)
#
#         self.setLayout(layout)
#
#         self.setWindowTitle("Familiya, Ism, Sharif")
#         self.setGeometry(100, 100, 300, 200)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyApp()
#     window.show()
#     sys.exit(app.exec())
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
#
# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         layout = QVBoxLayout()
#
#         self.label = QLabel("Ma'lumotni tanlang")
#         layout.addWidget(self.label)
#
#         button_first = QPushButton("Ism")
#         button_first.clicked.connect(self.show_first_name)
#
#         button_second = QPushButton("Familiya")
#         button_second.clicked.connect(self.show_family_name)
#
#         button_third = QPushButton("Tug'ilgan sana")
#         button_third.clicked.connect(self.show_birth_date)
#
#         layout.addWidget(button_first)
#         layout.addWidget(button_second)
#         layout.addWidget(button_third)
#
#         self.setLayout(layout)
#
#         self.setWindowTitle("Ma'lumot ko'rsatish")
#         self.setGeometry(100, 100, 300, 200)
#
#     def show_first_name(self):
#         self.label.setText("Ism: VASTELORD")
#
#     def show_family_name(self):
#         self.label.setText("Familiya: LORD")
#
#     def show_birth_date(self):
#         self.label.setText("Tug'ilgan sana: #######")
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyApp()
#     window.show()
#     sys.exit(app.exec())
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
#
#
# class CalculatorApp(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         layout = QVBoxLayout()
#
#         self.line_edit1 = QLineEdit()
#         self.line_edit1.setPlaceholderText("Birinchi sonni kiriting")
#
#         self.line_edit2 = QLineEdit()
#         self.line_edit2.setPlaceholderText("Ikkinchi sonni kiriting")
#
#         self.label = QLabel("Natija: ")
#
#         self.create_buttons(layout)
#
#         layout.addWidget(self.line_edit1)
#         layout.addWidget(self.line_edit2)
#         layout.addWidget(self.label)
#
#         self.setLayout(layout)
#
#         self.setWindowTitle("Hisoblash Dasturi")
#         self.setGeometry(100, 100, 1300, 768)
#
#     def create_buttons(self, layout):
#         operations = {
#             "+": self.add,
#             "-": self.subtract,
#             "*": self.multiply,
#             "/": self.divide,
#             "%": self.modulus,
#             "**": self.power
#         }
#
#         for op, func in operations.items():
#             button = QPushButton(op)
#             button.clicked.connect(func)
#             layout.addWidget(button)
#
#     def add(self):
#         self.calculate(lambda x, y: x + y)
#
#     def subtract(self):
#         self.calculate(lambda x, y: x - y)
#
#     def multiply(self):
#         self.calculate(lambda x, y: x * y)
#
#     def divide(self):
#         self.calculate(lambda x, y: x / y if y != 0 else "Nolga bo'lish mumkin emas!")
#
#     def modulus(self):
#         self.calculate(lambda x, y: x % y)
#
#     def power(self):
#         self.calculate(lambda x, y: x ** y)
#
#     def calculate(self, operation):
#         try:
#             num1 = float(self.line_edit1.text())
#             num2 = float(self.line_edit2.text())
#             result = operation(num1, num2)
#             self.label.setText(f"Natija: {result}")
#         except ValueError:
#             self.label.setText("Iltimos, to'g'ri sonlarni kiriting.")
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = CalculatorApp()
#     window.show()
#     sys.exit(app.exec())
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
#
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# class PrimeChecker(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Tub Son Tekshiruvi")
#
#         self.layout = QVBoxLayout()
#
#         self.line_edit = QLineEdit(self)
#         self.line_edit.setPlaceholderText("Sonni kiriting")
#         self.layout.addWidget(self.line_edit)
#
#         self.check_button = QPushButton("Tekshirish", self)
#         self.check_button.clicked.connect(self.check_prime)
#         self.layout.addWidget(self.check_button)
#
#         self.result_label = QLabel("", self)
#         self.layout.addWidget(self.result_label)
#
#         self.setLayout(self.layout)
#
#     def check_prime(self):
#         try:
#             number = int(self.line_edit.text())
#             if is_prime(number):
#                 QMessageBox.information(self, "Natija", f"{number} - tub son.")
#             else:
#                 QMessageBox.information(self, "Natija", f"{number} - tub son emas.")
#         except ValueError:
#             QMessageBox.critical(self, "Xato", "Iltimos, butun son kiriting.")
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = PrimeChecker()
#     window.show()
#     sys.exit(app.exec())
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
#
# dictionary = {
#     "salom": "hello",
#     "dunyo": "world",
#     "kitob": "book",
#     "qalam": "pen",
#     "osh": "polov"
# }
#
# class Translator(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("So'z Tarjimon")
#
#         self.layout = QVBoxLayout()
#
#         self.line_edit = QLineEdit(self)
#         self.line_edit.setPlaceholderText("Tarjima qilinadigan so'zni kiriting")
#         self.layout.addWidget(self.line_edit)
#
#         self.translate_button = QPushButton("Tarjima", self)
#         self.translate_button.clicked.connect(self.translate_word)
#         self.layout.addWidget(self.translate_button)
#
#         self.result_label = QLabel("", self)
#         self.layout.addWidget(self.result_label)
#
#         self.setLayout(self.layout)
#
#     def translate_word(self):
#         word = self.line_edit.text().strip()
#         if word in dictionary:
#             translation = dictionary[word]
#             self.result_label.setText(f"{word} - {translation}")
#         else:
#             QMessageBox.critical(self, "Xato", "So'z mavjud emas. Dastur to'xtatilmoqda.")
#             QApplication.quit()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Translator()
#     window.show()
#     sys.exit(app.exec())
