from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_BenThomasFinal):
    def __init__(self):
        """
        Sets up visibility and the three button functions
        """
        super().__init__()
        self.setupUi(self)

        self.button_calculate.clicked.connect(lambda: self.calculate())
        self.button_clear.clicked.connect(lambda: self.clear())
        self.button_enter.clicked.connect(lambda: self.enter())
        self.label_num1.setVisible(False)
        self.label_num2.setVisible(False)
        self.label_num3.setVisible(False)
        self.label_num4.setVisible(False)
        self.input_num1.setVisible(False)
        self.input_num2.setVisible(False)
        self.input_num3.setVisible(False)
        self.input_num4.setVisible(False)
        self.button_clear.setVisible(False)
        self.button_calculate.setVisible(False)

    def visibility_check(self, num: int):
        """
        Sets the visibility of certain labels and input boxes based on user input
        :param num: number 2-4 to set visibility
        :return:
        """
        if self.button_root.isChecked() is True or self.button_power.isChecked() is True:
            self.label_num1.setVisible(True)
            self.label_num2.setVisible(True)
            self.input_num1.setVisible(True)
            self.input_num2.setVisible(True)
            self.label_num1.setText(f'Base')
            self.label_num2.setText(f'Exponent/Root')
            if num > 2:
                self.main_label.setText(f'Power and Root functions cannot have more than 2 inputs')
            return
        else:
            self.label_num1.setText(f'Enter number 1:')
            self.label_num2.setText(f'Enter number 2:')
        if num < 2 or num > 4:
            self.main_label.setText(f'Enter an integer 2-4')
        if num == 4:
            self.label_num1.setVisible(True)
            self.label_num2.setVisible(True)
            self.label_num3.setVisible(True)
            self.label_num4.setVisible(True)
            self.input_num1.setVisible(True)
            self.input_num2.setVisible(True)
            self.input_num3.setVisible(True)
            self.input_num4.setVisible(True)
        elif num == 3:
            self.label_num1.setVisible(True)
            self.label_num2.setVisible(True)
            self.label_num3.setVisible(True)
            self.input_num1.setVisible(True)
            self.input_num2.setVisible(True)
            self.input_num3.setVisible(True)
        elif num == 2:
            self.label_num1.setVisible(True)
            self.label_num2.setVisible(True)
            self.input_num1.setVisible(True)
            self.input_num2.setVisible(True)

    def add(self, nums: list):
        """
        adds numbers in a list, if they exist
        :param nums: list of given numbers
        :return:
        """
        total = 0
        for num in nums:
            if num is nums[0]:
                total = num
            else:
                total += num
        self.main_label.setText(f'{total}')

    def subtract(self, nums: list):
        """
        subtracts numbers in a list, if they exist
        :param nums: list of given numbers
        :return:
        """
        total = 0
        for num in nums:
            if num is nums[0]:
                total = num
            else:
                total -= num
        self.main_label.setText(f'{total}')

    def multiply(self, nums: list):
        """
        multiplies numbers in a list, if they exist
        :param nums: list of given numbers
        :return:
        """
        total = 0
        for num in nums:
            if num is nums[0]:
                total = num
            else:
                total *= num
        self.main_label.setText(f'{total}')

    def divide(self, nums: list):
        """
        divides numbers in a list, if they exist
        :param nums: list of given numbers
        :return:
        """
        total = 0
        for num in nums:
            if num is nums[0]:
                total = num
            else:
                total /= num
        self.main_label.setText(f'{total}')

    def power(self, nums: list):
        """
        takes the first number of a list as the base, and the second as an exponent
        :param nums: list of given numbers
        :return:
        """
        self.main_label.setText(f'{nums[0]**nums[1]}')

    def root(self, nums: list):
        """
        takes the first number of a list as the base, and the second as a root
        :param nums: list of given numbers
        :return:
        """
        self.main_label.setText(f'{nums[0]**(1/nums[1])}')

    def number_test(self, num: str) -> list:
        """
        tests input to see if it is valid
        :param num: user input number
        :return:
        """
        try:
            num = float(num)
        except ValueError:
            pass
            return [0, 0]
        else:
            return [num, 1]

    def enter(self):
        """
        button to set off the visibility check
        :return:
        """
        try:
            amt = int(self.input_amt.text())
        except ValueError or self.input_amt.text() == '':
            pass
            self.main_label.setText(f'Enter an integer 2-4')
        else:
            self.button_calculate.setVisible(True)
            self.button_clear.setVisible(True)
            self.visibility_check(num=amt)
            self.input_num1.clear()
            self.input_num2.clear()
            self.input_num3.clear()
            self.input_num4.clear()

    def calculate(self):
        """
        calculates the selected function
        :return:
        """
        num1 = self.number_test(num=self.input_num1.text())
        num2 = self.number_test(num=self.input_num2.text())
        if self.input_num3.text() != '':
            num3 = self.number_test(num=self.input_num3.text())
        else:
            num3 = [None, 1]
        if self.input_num4.text() != '':
            num4 = self.number_test(num=self.input_num4.text())
        else:
            num4 = [None, 1]
        if num1[1] == 0 or num2[1] == 0 or num3[1] == 0 or num4[1] == 0:
            self.main_label.setText('Please enter numeric values')
            self.input_num1.clear()
            self.input_num2.clear()
            self.input_num3.clear()
            self.input_num4.clear()
            return
        num1 = num1[0]
        num2 = num2[0]
        num3 = num3[0]
        num4 = num4[0]
        nums = [num1, num2, num3, num4]
        true_nums = []
        for num in nums:
            if num is not None:
                true_nums.append(num)
        if self.button_add.isChecked() is True:
            self.add(nums=true_nums)
        if self.button_subtract.isChecked() is True:
            self.subtract(nums=true_nums)
        if self.button_multiply.isChecked() is True:
            self.multiply(nums=true_nums)
        if self.button_divide.isChecked() is True:
            self.divide(nums=true_nums)
        if self.button_power.isChecked() is True:
            self.power(nums=true_nums)
        if self.button_root.isChecked() is True:
            self.root(nums=true_nums)

    def clear(self):
        """
        clears all input boxes
        :return:
        """
        self.main_label.setText('')
        self.input_amt.setText('')
        self.input_num1.clear()
        self.input_num2.clear()
        self.input_num3.clear()
        self.input_num4.clear()
        self.input_num1.setVisible(False)
        self.input_num2.setVisible(False)
        self.input_num3.setVisible(False)
        self.input_num4.setVisible(False)
        self.label_num1.setVisible(False)
        self.label_num2.setVisible(False)
        self.label_num3.setVisible(False)
        self.label_num4.setVisible(False)
