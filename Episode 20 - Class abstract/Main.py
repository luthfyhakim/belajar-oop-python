# membuat class abstract
# import abc = abstract base class
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod # decorator abstract method
    def click(self):
        pass


class PushButton(Button):
    def click(self):
        print("push button click")


class RadioButton(Button):
    def click(self):
        print("radio button click")


tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()