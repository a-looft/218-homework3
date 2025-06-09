from typing import List
from calculator.calculation import Calculation

class Calculator:

    history: List[Calculation] = []


    @classmethod
    def addCalculation(class, calculation: Calculation) -> None:
        class.history.append(calculation)

    @classmethod
    def getLastCalculation(class) -> Calculation:
        return class.history[-1]

    @classmethod
    def clearHistory(class) -> None:
        class.history.clear()


    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
