# -*- coding: utf-8 -*-

from __future__ import division


class Sweep():
    def __init__(self, obj, profile, path):
        """ Sweep: represents an extrusion of a profile along a path.
        """
        obj.addProperty("App::PropertyString", "type", "Sweep", "type of the object").type = "sweep"
        obj.addProperty("App::PropertyLink","profile","Sweep","wire/sketch profile of the sweep").profile = profile
    
    def execute(self, fp):
        """ Print a short message when doing a recomputation, this method is mandatory.
        """
        FreeCAD.Console.PrintMessage("Recompute Python Sweep object\n")