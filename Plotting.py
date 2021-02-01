import PyQt5.QtWidgets as QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

"""
TODO:
    -
"""
class PlotWidget(QtWidgets.QWidget):
    """Widget for PyQt5 with the plot

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
    def __init__(self):
        super().__init__()
        self.fig = Figure() # Create a matplotlib figure
        self.canvas = FigureCanvas(self.fig) # Get the plot image
        self.axes = self.fig.add_subplot(111,projection='3d') # Create matpotlib axes

        self.setWindowTitle('Linear transformations')

        self.layout = QtWidgets.QGridLayout(self) # Set the layout

        self.addToLayout(self.canvas, [0,0],[10,10]) # add the plot to the layout

    def scatter(self,xyzgrid:list,colors:list):
        """Scatter the data
    
        ...

        Parameters
        ----------
        xyzgrid:list
            data for plotting
            xyzgrid[0] the x data
            xyzgrid[1] the y data
            xyzgrid[2] the z
        colors:list
            colors
        """
        self.axes.clear()
        self.axes.scatter(xyzgrid[0],xyzgrid[1],xyzgrid[2],c = colors,alpha=0.7)

    def addToLayout(self, widget, position:list = [0,0], size:list = [1,1]):
        """Add widget to layout
        """
        self.layout.addWidget(widget,position[1],position[0],size[1],size[0])