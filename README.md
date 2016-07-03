# MitralSuite - Objective Validation of Computational Neuroscience Models
Validation of Olfactory Bulb Mitral Cell models with data from NeuroElectro.org and using NeuronUnit framework.

# Requirements

 1. Ensure you have [Python >=2.7](https://www.python.org/downloads/), [numpy](https://www.scipy.org/install.html), and [matplotlib](http://matplotlib.org/users/installing.html)
 2. Install [NEURON with Python interface](http://neuron.yale.edu/neuron/download/getstd) ("import neuron" statement works)
 3. Install [SciUnit](https://github.com/scidash/sciunit) and [NeuronUnit](https://github.com/scidash/neuronunit)
 4. Install [iPython and Jupyter](https://ipython.org/)

# Simple Model Example

Once you have all the requirements installed, you should be able to run a example that subjects a simple HH cell to a suite of tests.

Download this repository and run the following notebook in iPython: [SimpleNeuronCellTests](https://github.com/JustasB/MitralSuite/blob/master/SimpleNeuronCellTests.ipynb)

# Pooled Data from NeuroElectro Example

Once the simple model example is working, you can see how to obtain pooled experimental results from [NeuroElectro database](http://neuroelectro.org/).

The notebook with the steps for pooling: [PooledPropertyValuesTest](https://github.com/JustasB/MitralSuite/blob/master/PooledPropertyValuesTest.ipynb)

# Mitral Cell Experimental Data
The results obtain from pooling the experimental data for the mitral cells can be found in the following notebook:
[ExperimentalObservations](https://github.com/JustasB/MitralSuite/blob/master/ExperimentalObservations.ipynb)

# Mitral Cell Model Results
The results of subjecting the mitral cell models to the 6 tests can be found here: [GetResultsSummary](https://github.com/JustasB/MitralSuite/blob/master/GetResultsSummary.ipynb)

The NEURON code for the models that were prepared (to isolate the cells and remove external inputs) in the following folder:
[Models](https://github.com/JustasB/MitralSuite/tree/master/Models)

The results of running individual models can be found in the notebooks that follow the "AuthorYYYY" format. For example the results fo the Bhalla & Bower (1993) Model can be found at this notebook: [BhallaBower1993](https://github.com/JustasB/MitralSuite/blob/master/BhallaBower1993.ipynb)

# Issues and Contact

If you run into problems or bugs, please report them as [Issues](https://github.com/JustasB/MitralSuite/issues).
