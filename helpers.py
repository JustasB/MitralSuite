import matplotlib.pyplot as g
import pickle, os, neuronunit.neuroelectro

from ipywidgets import interact
from neuronunit.neuron.models import *
from neuronunit.tests import *
from quantities import nA, pA, s, ms, mV, ohm

Mohm = pq.UnitQuantity('megaohm', ohm*1e6, symbol='Mohm')
rootPath = os.getcwd()



def createModel(name, path, getSectionScript):
    
    # Go to folder with mod files
    os.chdir(path)
    
    # Compile mod files (if needed)
    #import subprocess
    #subprocess.call("nrnivmodl",shell=True)
    #subprocess.call("mknrndll", shell=True)

    # Load neuron
    from neuron import h

    # Run custom steps to get the target cell
    soma = getSectionScript(h)
    
    # Create NeuronUnit model
    mod1 = SingleCellModel(hVar = h, \
                       section = soma, \
                       loc = 0.5, # Current and voltage injection and measurement location on the section \
                       name = name)

    mod1.setTimeStep(1/32.0 * ms)
    mod1.setStopTime(2*s)
    
    return mod1

# Creates three text boxes that can be used to find desirable current pulses
def IClampWidget(model):
    
    def IClamp(amp,delay,dur):
        
        # Inject a current pulse
        model.inject_square_current({'amplitude': float(amp)*nA, 'delay': float(delay)*ms, 'duration': float(dur)*ms})

        plotModelV(model)

    # Create the widget, use manual update mode
    interact(IClamp,amp="1",delay="500",dur="1000", __manual=True)

def plotModelV(model, APIndex = 0):
    
    # Plot the full simulation result
    v = model.get_membrane_potential()
    g.plot(v.times, v)
    g.ylim([-80,40])
    g.show()

    # Show a closeup of an action potential (if any)
    if len(model.get_APs() > 0):
        ap = model.get_APs()[APIndex]
        g.plot(ap.times*1000,ap)
        #g.ylim([-80,40])
        g.show()

def setupTests(i_rest, i_passive, i_ap, i_thresh, expectedSource = "Pooled"):
    
    # Define the tests to perform on the cell
    testTypes = [ \
        [RestingPotentialTest,           {'injected_square_current': i_rest }],
        [InputResistanceTest,            {'injected_square_current': i_passive }],
        [TimeConstantTest,               {'injected_square_current': i_passive }],
        [InjectedCurrentAPWidthTest,     {'injected_square_current': i_ap }], \
        [InjectedCurrentAPThresholdTest, {'injected_square_current': i_thresh }], \
        [InjectedCurrentAPAmplitudeTest, {'injected_square_current': i_thresh }],
    ]

    tests = []
    
    with open(rootPath + "/observations.dat", "rb") as file:
        observations = pickle.load(file) # Use UserDefined, Pooled, or UnPooled

    # Fetch NeuroElectro property values for each test
    for t in xrange(len(testTypes)):
        testType = testTypes[t][0]
        params = testTypes[t][1]

        # Get the observations: property means and stds
        obs = observations[expectedSource][testType.name]

        # Create a test instance using the observations
        test = testType(obs)

        if(params is not None):
            test.params = params

        tests.append(test)
        
    return tests

def runOneTest(test, model):
    print("----------")
    print("Running Test: %s"%test.name)
    print("Expected: %s +/- %s SD"%(test.observation["mean"],test.observation["std"]))

    pred = test.generate_prediction(model)
    mean = pred["mean"] if "mean" in pred else pred["value"]

    if mean.units == s:
        mean.units = ms

    z = (mean-test.observation["mean"])/test.observation["std"]
    
    print("Actual: %s, Z: %s SDs"%(mean,float(z)))

    plotModelV(model)
    
    return mean

def runAllTests(tests, model):

    results = { model.name: {} }
    
    for test in tests:
        results[model.name][test.name] = runOneTest(test, model)
        
    return results

def loadResults():
    # Load previous results
    with open(rootPath + "/results.dat", "rb") as file:
        results = pickle.load(file)
        
    return results

def saveResults(newResults):

    results = loadResults()

    results.update(newResults)
    
    # Save current results
    with open(rootPath + "/results.dat", "wb") as file:
        pickle.dump(results, file)