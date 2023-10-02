import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Kalkulator Biner Desimal')
        self.setGeometry(100, 100, 300, 400)
        self.initUI()
    
    def binerConvert(self, number):
        result = 0
        number = str(number)
        pangkat = len(number) - 1
        for i in range(len(number)):
            result += int(number[i]) * 2 ** pangkat
            pangkat -= 1
        return result
    
    def decimalConvert(self, number):
        if number == 0:
            return "0"
        else:
            result = ""
            while number > 0:
                sisa = number % 2
                result = str(sisa) + result
                number //= 2
            return result
    
    def split_operators(self, input_str):  # Menggunakan self untuk metode instance
        operators_and_operands = []
        i = 0
        while i < len(input_str):
            if input_str[i] in ('+', '-', '*', '/'):
                operators_and_operands.append(input_str[i])
                i += 1
            elif input_str[i].isdigit():
                start = i
                while i < len(input_str) and input_str[i].isdigit():
                    i += 1
                operators_and_operands.append(input_str[start:i])
            else:
                i += 1
        return operators_and_operands
    

    def initUI(self):
        self.option = "desimal"
        self.label = QLabel("Mode: " +self.option, self)
        self.buttonDecimal = QPushButton("Desimal")
        self.buttonDecimal.clicked.connect(self.button_decimal)
        self.buttonBiner = QPushButton("Biner")
        self.buttonBiner.clicked.connect(self.button_biner)
        self.input_line = QLineEdit(self)
        self.input_line.setPlaceholderText("Masukkan Angka")
        self.input_line.setReadOnly(True)

        option = QHBoxLayout()
        buttons_layout = QVBoxLayout()
        button_rows = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', 'C', '+', '=']
        ]

        for row in button_rows:
            row_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text, self)
                button.clicked.connect(self.on_button_click)
                row_layout.addWidget(button)
            buttons_layout.addLayout(row_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.buttonBiner)
        main_layout.addWidget(self.buttonDecimal)
        main_layout.addWidget(self.input_line)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

    def button_biner(self):
        self.option = "biner"
        self.label.setText("Mode: biner")

    def button_decimal(self):
        self.option = "desimal"
        self.label.setText("Mode: desimal")

    def on_button_click(self):
        button = self.sender()
        if button:
            if button.text() == '=':
                if self.option == "desimal":
                    result = eval(self.input_line.text())
                    self.input_line.setText(str(result))
                elif self.option == "biner":
                    val = self.input_line.text()
                    a = self.split_operators(val)
                    for i in range(len(a)):
                        if a[i].isnumeric():
                            x = self.binerConvert(a[i])
                            a[i] = str(x)
                    result = eval(' '.join(a))
                    self.input_line.setText(str(self.decimalConvert(result)))
            elif button.text() == 'C':
                self.input_line.clear()
            else:
                current_text = self.input_line.text()
                new_text = current_text + button.text()
                self.input_line.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())
