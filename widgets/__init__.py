# from PyQt6.QtCore import pyqtSignal
# from PyQt6.QtWidgets import  QWidget, QLabel, QLineEdit, QTextEdit, QComboBox, QSpinBox, QCheckBox, QPushButton, QVBoxLayout, QMessageBox
#
#
# class SimpleForm(QWidget):
#     form_submitted = pyqtSignal(str, str, int, str, str)
#
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
#         self.form_submitted.emit(first_name, last_name, age, gender, bio)
