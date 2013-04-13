from .base import AbstractRenderer
from . import CylinderRenderer
import numpy as np
from chemlab.graphics.colors import default_atom_map

class BondRenderer(AbstractRenderer):
    def __init__(self, widget, bonds, r_array, type_array, radius=0.02):
        super(BondRenderer, self).__init__(widget)
        starts = r_array[bonds[:,0]]
        ends = r_array[bonds[:,1]]
        middle = (starts + ends)/2 
    
        bounds_a = np.empty((len(bonds), 2, 3))
        bounds_a[:, 0, :] = starts
        bounds_a[:, 1, :] = middle
    
        bounds_b = np.empty((len(bonds), 2, 3))    
        bounds_b[:, 0, :] = middle
        bounds_b[:, 1, :] = ends
    
        radii = [radius] * len(bounds_a)

        colors_a = []
        colors_b = []

        for i, j in bonds:
            colors_a.append(
                default_atom_map.get(type_array[i],
                                 default_atom_map['Xx']))
            colors_b.append(
                default_atom_map.get(type_array[j],
                                 default_atom_map['Xx']))

        self.cr1 = CylinderRenderer(widget, bounds_a, radii, colors_a)
        self.cr2 = CylinderRenderer(widget, bounds_b, radii, colors_b)

    def draw(self):
        self.cr1.draw()
        self.cr2.draw()