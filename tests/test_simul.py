from chemlab import Atom, Molecule, display
from chemlab.molsim import integrators, forces
from chemlab.molsim import cforces as forces
from chemlab.graphics.viewer import Viewer
import numpy as np
import time
import multiprocessing as mp
import threading
from chemlab.core.system import MonatomicSystem
from chemlab.graphics.renderers import SphereRenderer, CubeRenderer, PointRenderer
from chemlab.molsim.analysis import pair_correlation
import pylab as pl

def test_1():
    boxsize = 50.0
    sys = MonatomicSystem.random("Ne",500, boxsize)
    #x, y = pair_correlation(sys, 20)
    #pl.plot(x, y)
    for i in range(1000):
        print "Step ", i
        farray = forces.lennard_jones(sys.rarray, "Ne", periodic=boxsize)
        # Just this time let's assume masses are 1
        sys.rarray, sys.varray = integrators.euler(sys.rarray, sys.varray, farray/300.17, 0.011)
        
        # Add more periodic conditions
        rarray = sys.rarray
        
        i_toopositive = rarray > boxsize * 0.5
        rarray[i_toopositive] -= boxsize  
        i_toonegative = rarray < - boxsize * 0.5
        rarray[i_toonegative] += boxsize
        
        sys.rarray = rarray

    #x, y = pair_correlation(sys, 20)
    #pl.plot(x, y)
    
    #pl.show()
    
def test_2():
    # Let's try with threads
    boxsize = 30.0
    nmol = 1000
    sys = MonatomicSystem.random("Ne", nmol, boxsize)
    
    v = Viewer()
    v.add_renderer(PointRenderer(sys))
    v.add_renderer(CubeRenderer(boxsize))
    
    sys.varray = np.random.rand(nmol, 3).astype(np.float32) - 0.5
    
    def iterate(dt):
        # Let's try to make periodic boundary conditions
        farray = forces.lennard_jones(sys.rarray, "Ne", periodic=boxsize)
        # Just this time let's assume masses are 1
        sys.rarray, sys.varray = integrators.euler(sys.rarray, sys.varray, farray/30.17, 0.01)
        
        # Add more periodic conditions
        rarray = sys.rarray
        
        i_toopositive = rarray > boxsize * 0.5
        rarray[i_toopositive] -= boxsize  
        i_toonegative = rarray < - boxsize * 0.5
        rarray[i_toonegative] += boxsize
        
        sys.rarray = rarray
        v.update()
    
    import pyglet
    pyglet.clock.schedule(iterate)
    pyglet.app.run()

from chemlab.graphics.viewer import ProcessViewer

def test_3():
    '''Make this much more interactive'''
    boxsize = 30.0
    nmol = 1000
    sys = MonatomicSystem.random("Ne", nmol, boxsize)
    v = ProcessViewer()
    pr = v.add_renderer(SphereRenderer, sys.atoms)
    v.add_renderer(CubeRenderer, boxsize)
    
    for i in range(100):
        # Let's try to make periodic boundary conditions
        farray = forces.lennard_jones(sys.rarray, "Ne", periodic=boxsize)
        # Just this time let's assume masses are 1
        sys.rarray, sys.varray = integrators.euler(sys.rarray, sys.varray, farray/30.17, 0.01)
        
        # Add more periodic conditions
        rarray = sys.rarray
        
        i_toopositive = rarray > boxsize * 0.5
        rarray[i_toopositive] -= boxsize  
        i_toonegative = rarray < - boxsize * 0.5
        rarray[i_toonegative] += boxsize
        
        sys.rarray = rarray
        pr.update(rarray)
    
    v._p.join()
    

if __name__ == '__main__':
    test_3()
