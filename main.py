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

"""Transformation matrix"""
transformationMatrix = Matrix([[1, 0, 0],
                               [0, 0.5, 0],
                               [0, 0, 1]])

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

if __name__ == "__main__":

    originalGrid = get_grid(-2,2)
    transformedGrid = transformPoint(originalGrid[0],originalGrid[1],originalGrid[2])
    xyzgrid = array([transformedGrid[0,:][0,:],     #
                     transformedGrid[1,:][0,:],     # Save the transformed grid as a numpy array 
                     transformedGrid[2,:][0,:]])    #

    colors = list(map(colorizer, originalGrid[0], originalGrid[1], originalGrid[2])) # Asign the colors to the points

    app = QtWidgets.QApplication([])
    plot = PlotWidget(xyzgrid[0], xyzgrid[1], xyzgrid[2], colors = colors, alpha = 0.7)

    plot.axes.set_xlim([-2, 2]) #
    plot.axes.set_ylim([-2, 2]) # Set the limits of the plot
    plot.axes.set_zlim([-2, 2]) #
    plot.axes.axis('on')        # Show the axis
    plot.axes.set_xlabel('x')   #
    plot.axes.set_ylabel('y')   # Axes names
    plot.axes.set_zlabel('z')   #
    plot.axes.grid(False)       # Don't show the grid
    plot.axes.view_init(10,5)   # View init at 15 and 5 degrees

    plot.show()
    app.exec()