# Linear transformation visualization in 3D

## Why?

A linear transformation is a function from one vector space to another that respects the linear structure of each vector space ([Learn more](https://brilliant.org/wiki/linear-transformations/)). For visualizing this we can transform a vector as we can see in the Fig. 1. 

<figure>
  <img src="https://i.ibb.co/VTRy5Tx/vector-linear-Transformation.png" alt="vector transformed" style="width:40%;
                                                                                                       display: block;
                                                                                                       margin-left: auto;
                                                                                                       margin-right: auto;">
  <figcaption  style="text-align: center;">Fig.1 - Vector transformed with a transformation matrix</figcaption>
</figure>

But it has an obvious problem, because the linear transformation transform the whole space, not just the vector, in other words it transforms the basis vectors thus every vector in the space gets transformed too. That's why i created this app so everyone can see how a transformation matrix change the whole space.

## Installation guide

### With the executable file

1. Install Python from the [python web](https://www.python.org/).
2. Download the executable file for your OS (Linux or Windows).
3. Execute the file.
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

