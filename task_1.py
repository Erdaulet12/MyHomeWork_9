"""task_1.py"""

import matplotlib.pyplot as plt
import numpy as np


class LinePlot:
    """LinePlot class"""

    def __init__(self, x, y):
        """initial class"""
        self.x = x
        self.y = y

    def plot(self):
        """method for plot diagramm"""
        plt.plot(self.x, self.y)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()


class BarPlot:
    """BarPlot class"""

    def __init__(self, x, y):
        """initial class"""
        self.x = x
        self.y = y

    def plot(self):
        """method for plot diagramm"""
        plt.bar(self.x, self.y)
        plt.xlabel("Категория")
        plt.ylabel("Значение")
        plt.show()


class Histogram:
    """Histogram class"""

    def __init__(self, data):
        """initial method"""
        self.data = data

    def plot(self):
        """method for plot diagram"""
        plt.hist(self.data)
        plt.xlabel("Значение")
        plt.ylabel("Частота")
        plt.show()


if __name__ == "__main__":
    line_data = LinePlot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
    line_data.plot()
    bar_data = BarPlot(["A", "B", "C", "D", "E"], [10, 20, 30, 40, 50])
    bar_data.plot()
    histo_data = Histogram(np.random.randn(100))
    histo_data.plot()
