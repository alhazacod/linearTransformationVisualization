import PyQt5.QtWidgets as QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from sympy import Matrix

class MatrixButtons(QtWidgets.QWidget):
    """Widget for PyQt5 with the Matrix input and the buttons

    ...

    Attributes
    ----------
    layout: QtWidgets.QGridLayout
    """
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QGridLayout(self) # Set the layout

        #First row
        self.matrix00 = QtWidgets.QLineEdit()
        self.matrix10 = QtWidgets.QLineEdit()
        self.matrix20 = QtWidgets.QLineEdit()
        self.addToLayout(self.matrix00,[0,0],[1,1])
        self.addToLayout(self.matrix10,[1,0],[1,1])
        self.addToLayout(self.matrix20,[2,0],[1,1])

        # Second row
        self.matrix01 = QtWidgets.QLineEdit()
        self.matrix11 = QtWidgets.QLineEdit()
        self.matrix21 = QtWidgets.QLineEdit()
        self.addToLayout(self.matrix01,[0,1],[1,1])
        self.addToLayout(self.matrix11,[1,1],[1,1])
        self.addToLayout(self.matrix21,[2,1],[1,1])

        # Third row
        self.matrix02 = QtWidgets.QLineEdit()
        self.matrix12 = QtWidgets.QLineEdit()
        self.matrix22 = QtWidgets.QLineEdit()
        self.addToLayout(self.matrix02,[0,2],[1,1])
        self.addToLayout(self.matrix12,[1,2],[1,1])
        self.addToLayout(self.matrix22,[2,2],[1,1])

        # Button for plot the grid transformed by the matrix
        self.plotButton = QtWidgets.QPushButton('Plot')
        self.addToLayout(self.plotButton,[1,3],[1,1])

        
    def addToLayout(self, widget, position:list, size:list):
        self.layout.addWidget(widget,position[1],position[0],size[1],size[0])

    def setMatrix(self,matrix):
        """Add widget to layout
        """
        # First row
        self.matrix00.setText(str(matrix[0,0]))
        self.matrix10.setText(str(matrix[0,1]))
        self.matrix20.setText(str(matrix[0,2]))

        # Second row
        self.matrix01.setText(str(matrix[1,0]))
        self.matrix11.setText(str(matrix[1,1]))
        self.matrix21.setText(str(matrix[1,2]))

        # Third row
        self.matrix02.setText(str(matrix[2,0]))
        self.matrix12.setText(str(matrix[2,1]))
        self.matrix22.setText(str(matrix[2,2]))
