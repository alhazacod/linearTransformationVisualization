import PyQt5.QtWidgets as QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

"""
TODO:
    - I should add the option of default colors and alpha but i couldn't, it's something to fix
"""
class PlotWidget(QtWidgets.QWidget):
    """

    Widget for PyQt5 with the plot

    ...

    Parameters
    ----------
    x: list
        List with the x values
    y: list
        List with the y values
    z: list
        List with the z values
    colors: tuple
        Tuple with the RGB colors
    alpha: float
        The transparency of the plot

    ...

    Attributes
    ----------
    fig: matplotlib.figure

    axes:  matplotlib.axes

    canvas: matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg
    """
    def __init__(self, x: list, y: list, z: list, colors: tuple, alpha: float):
        super().__init__()
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111,projection='3d')

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.canvas)

        self.axes.scatter(x, y, z, c = colors, alpha = alpha)