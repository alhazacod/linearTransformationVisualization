# Linear transformation visualization in 3D

## Why?

A linear transformation is a function from one vector space to another that respects the linear structure of each vector space ([Learn more](https://brilliant.org/wiki/linear-transformations/)). For visualizing this we can transform a vector as we can see in the Fig. 1. 

<figure>
  <img src="https://i.ibb.co/VTRy5Tx/vector-linear-Transformation.png" width = 400px height = 270px alt="vector transformed">
  <figcaption>Fig.1 - Vector transformed with a transformation matrix</figcaption>
</figure> </br>




But it has an obvious problem, because the linear transformation transform the whole space, not just the vector, in other words it transforms the basis vectors thus every vector in the space gets transformed too. That's why i created this app so everyone can see how a transformation matrix change the whole space.

## Installation guide

### With the executable file

1. Install Python from the [python web](https://www.python.org/).
2. Download the executable file for your OS ([Linux](https://sourceforge.net/projects/lineartransformationvisualized/files/V1.0.0/3d_linear_transformation_Linux/download) or [Windows](https://sourceforge.net/projects/lineartransformationvisualized/files/V1.0.0/3d_linear_transformation_Windows.exe/download)).
3. Execute the file (it might take a while to open).
4. Start using.

The executable was created with [PyInstaller](http://www.pyinstaller.org/).

### Manual installation

1. Install Python from the [python web](https://www.python.org/).
2. Install pip from the [pip web](https://pip.pypa.io/en/stable/installing/)
3. Install the dependences using pip.
   - pip install sympy
   - pip install pyqt5
   - pip install numpy
4. Download the main.py, Plotting.py and Matrix.py files.
5. In the console go to the files location
6. Run the main file with <code>python3.8 main.py</code>

## How to use

When you open the app you can see the grid at the left, and the interface at the right. The grid was plotted with color so you can notice the transformations. 

<figure>
  <img src="https://i.ibb.co/NVGsQKw/main-window.png" width = 508px height = 288px alt="vector transformed">
</figure> </br>

At the right you can choose an example from the list and it will transform the original grid by the transformation that you have choose from the examples list, remember that the app can't remember the posterior state, so you can't for example rotate the plot 45º in X and then rotate it again 45º in Y, when you do the second transformation it will transform the *original* grid not the grid you got in the first transformation. You can create any transformation matrix and write it in the app and see how it transforms the grid too.

<figure>
  <img src="https://i.ibb.co/n3PY8sd/examples.png" width = 1016px height = 288px alt="vector transformed">
</figure> </br>