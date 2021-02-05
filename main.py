"""
Visualization of the tranformation matrix
Author: Manuel Garcia
Date: January 27 2021
"""
from sympy.matrices import Matrix       #It's easier work with matrices in sympy than numpy
from sympy import sin,cos,pi,N          #Trigonometric functions
import matplotlib.pyplot as plt         #Plotting
from numpy import linspace,column_stack,array #For create the linspace for the plotting

import PyQt5.QtWidgets as QtWidgets     #Python GUI
from PyQt5.QtGui import QFont           #Pyqt5 fonts

from Plotting import PlotWidget         #The plot object

from MatrixButtons import MatrixButtons # Interface class

def transformPoint(x,y,z,transformationMatrix):
    """Return the vector transformed
    
    """
    return transformationMatrix*Matrix([x,y,z])

def colorizer(x, y,z):
    """Color the points in the space by their position
    
    """
    r = min(1, 1-y/3)
    g = min(1, 1+x/3)
    b = 1/4 + x/16
    return (r, g, b)

def get_grid(min,max):
    """Return a grid in x, y and z
    
    ...

    Parameters
    ----------
    min
        minimum value in the x,y and z axes
    max
        maximum value in the x,y and z axes
    """
    xvals = linspace(min, max, abs(min-max)+1)
    yvals = linspace(min, max, abs(min-max)+1)
    zvals = linspace(min, max, abs(min-max)+1)
    xyzgrid = column_stack([[x, y,z] for x in xvals for y in yvals for z in zvals])
    return xyzgrid

def get_transformedGrid(originalGrid, transformationMatrix):
    """Return a grid in x, y and z transformed
    
    ...

    Parameters
    ----------
    originalGrid
        
    transformationMatrix
        
    """
    transformedGrid = transformPoint(originalGrid[0],originalGrid[1],originalGrid[2],transformationMatrix)

    return array([transformedGrid[0,:][0,:],     #
                  transformedGrid[1,:][0,:],     # Save the transformed grid as a numpy array 
                  transformedGrid[2,:][0,:]])    #

def adjust_plot(axes):
    axes.set_xlim([-2, 2]) #
    axes.set_ylim([-2, 2]) # Set the limits of the plot
    axes.set_zlim([-2, 2]) #
    axes.axis('on')        # Show the axis
    axes.set_xlabel('x')   #
    axes.set_ylabel('y')   # Axes names
    axes.set_zlabel('z')   #
    axes.grid(True)       # Don't show the grid

def exceptionDialog(msg):
    dlg = QtWidgets.QErrorMessage()
    dlg.showMessage(msg)
    dlg.exec_()

def transformAndPlot(plot,matrix):
    
    try:
        matrix = array(matrix)
        print(matrix)
        interface.setMatrix(matrix)
        xyzgrid = get_transformedGrid(originalGrid, Matrix([[N(matrix[0,0]),N(matrix[0,1]),N(matrix[0,2])],
                                                            [N(matrix[1,0]),N(matrix[1,1]),N(matrix[1,2])],
                                                            [N(matrix[2,0]),N(matrix[2,1]),N(matrix[2,2])]])) # get a transformed grid
        plot.scatter(xyzgrid,colors)
        adjust_plot(plot.axes)
        plot.fig.canvas.draw()
        plot.fig.canvas.flush_events()
    except:
        exceptionDialog('An error has ocurred. Remember that you only can write operations between numbers or trigonometric functions in the matrix boxes. ex. sin(3*pi/2) or sqrt(2)/2+5')

def examplesComboBox(window,comboBox):
    examples = {
        'Original Grid' :[[1, 0, 0],[0, 1, 0],[0, 0, 1]],
        'Personalized matrix' :[[1, 0, 0],[0, 1, 0],[0, 0, 1]],
        'Reflect in X' :[[-1, 0, 0],[0, 1, 0],[0, 0, 1]],
        'Reflect in Y' :[[1, 0, 0],[0, -1, 0],[0, 0, 1]],
        'Reflect in Z' :[[1, 0, 0],[0, 1, 0],[0, 0, -1]],
        'Stretch in Y' :[[1, 0, 0],[0, 2, 0],[0, 0, 1]],
        'Compact in Y' :[[1, 0, 0],[0, '1/2', 0],[0, 0, 1]],
        'X rotation 45º' :[[1, 0, 0],[0, 'cos(45*pi/180)', '-sin(45*pi/180)'],[0, 'sin(45*pi/180)', 'cos(45*pi/180)']],
        'Y rotation 45º' :[['cos(45*pi/180)', '-sin(45*pi/180)', 0],['sin(45*pi/180)', 'cos(45*pi/180)', 0],[0, 0, 1]],
        'Z rotation 45º' :[['cos(45*pi/180)', 0, '-sin(45*pi/180)'],[0, 1, 0],['sin(45*pi/180)', 0, 'cos(45*pi/180)']],
        'X-Y rotation 45º-10º':[['cos(45*pi/180)*cos(10*pi/180)','cos(45*pi/180)*sin(10*pi/180)-sin(45*pi/180)','cos(45*pi/180)*sin(10*pi/180)+sin(45*pi/180)*sin(10*pi/180)'],['sin(45*pi/180)*cos(10*pi/180)','sin(45*pi/180)*sin(10*pi/180)+cos(45*pi/180)','sin(45*pi/180)*sin(10*pi/180)-cos(45*pi/180)'],['-sin(10*pi/180)','cos(10*pi/180)','cos(10*pi/180)']],
        'Only XY dimension' :[[1, 0, 0],[0, 1, 0],[0, 0, 0]],
        'Only YZ dimension' :[[0, 0, 0],[0, 1, 0],[0, 0, 1]],
        'Only XZ dimension' :[[1, 0, 0],[0, 0, 0],[0, 0, 1]]
    }
    for key in examples:
        examplesWidget.addItem(key)

    examplesWidget.activated[str].connect(lambda str: transformAndPlot(window,examples.get(str)))

    window.addToLayout(examplesWidget, [13,2],[3,1])

def plotButton(plot,matrix):
    transformAndPlot(plot,matrix)
    examplesWidget.setCurrentIndex(1)

if __name__ == "__main__":
    """Transformation matrix"""
    transformationMatrix = [[1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 1]]

    originalGrid = get_grid(-2,2) # Create a straigh grid
    xyzgrid = get_transformedGrid(originalGrid, Matrix(transformationMatrix)) # get a transformed grid

    colors = list(map(colorizer, originalGrid[0], originalGrid[1], originalGrid[2])) # Asign the colors to the points

    app = QtWidgets.QApplication([]) # Create the app
    plot = PlotWidget() # Get the widget where the plot is

    plot.scatter(xyzgrid,colors) # Scatter

    adjust_plot(plot.axes) # Set the limits of the axes
    plot.axes.view_init(10,5)   # View init at 15 and 5 degrees
    
    examples_label = QtWidgets.QLabel('Examples')
    examples_label.setFont(QFont('Sans Serif', 20))
    plot.addToLayout(examples_label,[12,2],[1,1])
    examplesWidget = QtWidgets.QComboBox()
    examplesComboBox(plot,examplesWidget)

    matrix_label = QtWidgets.QLabel('Transformation Matrix')
    matrix_label.setFont(QFont('Sans Serif', 20))
    plot.addToLayout(matrix_label,[12,4],[2,1])
    interface = MatrixButtons() # Get the interface
    plot.addToLayout(interface,[11,5],[10,2]) # add the interface to the plot layout

    interface.setMatrix(array(transformationMatrix))

    interface.plotButton.clicked.connect(
        lambda: plotButton(plot,[[interface.matrix00.text(), interface.matrix10.text(), interface.matrix20.text()],
                                 [interface.matrix01.text(), interface.matrix11.text(), interface.matrix21.text()],
                                 [interface.matrix02.text(), interface.matrix12.text(), interface.matrix22.text()]]))

    plot.show() 
    app.exec()