"""
Visualization of the tranformation matrix
Author: Manuel Garcia
Date: January 27 2021
"""
from sympy.matrices import Matrix       #It's easier work with matrices in sympy than numpy
from sympy import sin,cos,pi            #Trigonometric functions
import matplotlib.pyplot as plt         #Plotting
from numpy import linspace,column_stack,array #For create the linspace for the plotting

import PyQt5.QtWidgets as QtWidgets     #Python GUI

from Plotting import PlotWidget         #The plot object

def transformPoint(x,y,z):
    """Return the vector transformed
    
    """
    return transformationMatrix*Matrix([x,y,z])

def colorizer(x, y,z):
    """Color the points in the space by their position
    
    """
    r = min(1, 1-y/3)
    g = min(1, 1+y/3)
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
    transformedGrid = transformPoint(originalGrid[0],originalGrid[1],originalGrid[2])
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
    axes.grid(False)       # Don't show the grid
    axes.view_init(10,5)   # View init at 15 and 5 degrees

if __name__ == "__main__":
    """Transformation matrix"""
    transformationMatrix = Matrix([[1, 0, 0],
                                   [0, 1, 0],
                                   [0, 1, 1]])

    originalGrid = get_grid(-2,2) # Create a straigh grid
    xyzgrid = get_transformedGrid(originalGrid, transformationMatrix) # get a transformed grid

    colors = list(map(colorizer, originalGrid[0], originalGrid[1], originalGrid[2])) # Asign the colors to the points

    app = QtWidgets.QApplication([])
    plot = PlotWidget()

    plot.scatter(xyzgrid,colors)

    adjust_plot(plot.axes)

    plot.show()
    app.exec()