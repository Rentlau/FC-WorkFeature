# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 21:21:12 2016

@author: laurent
"""

import Draft, Part
 
__title__   = "FCConvertLines"
__author__  = "Mario52"
__url__     = "http://www.freecadweb.org/index-fr.html"
__version__ = "00.01"
__date__    = "19/01/2016"
 
def dashLine(dash01 = 2.0, space01 = 1.0, dash02 = 1.0, space02 = 1.0, compLine = 0, red = 0, green = 0, blue = 0, typeLine = 1):
                                                                                              # typeLine = 1 "_ _ _ _ _ _ _ _ _ "  dash         (dash01, space01)
                                                                                              # typeLine = 2 "___ _ ___ _ ___ _ "  dash dot     (dash01, space01, dash02)
                                                                                              # typeLine = 3 "___ _ _ ___ _ _ ___" dash dot dot (dash01, space01, dash02, space02)
    def createLines(numberOfPoints, points):
        space = 0
        for lin in range(numberOfPoints-1):
            if space == 0:
                creaLine = [FreeCAD.Vector(points[lin]),FreeCAD.Vector(points[lin+1])]
                wire =  Draft.makeWire(creaLine,closed=False,face=False,support=None)
                space = 1
                ligne.append(wire.Shape)                                      # for compount 
                nom.append(wire.Name)                                         # for compount
            else:
                space = 0
            # si pas possible affiche cette ligne                             # Cannot compute Inventor representation for the shape of Shape. 
 
    def colorize():
        FreeCADGui.activeDocument().activeObject().LineColor  = (float(red)/255,float(green)/255,float(blue)/255)
        FreeCADGui.activeDocument().activeObject().PointColor = (float(red)/255,float(green)/255,float(blue)/255)
        FreeCADGui.activeDocument().activeObject().ShapeColor = (float(red)/255,float(green)/255,float(blue)/255)
 
    if dash01 and space01 and dash02 and space02 != 0:
        nom       = []; nom[:]     = []
        ligne     = []; ligne[:]   = []
        comp2     = []; comp2[:]   = []
        points    = []; points[:]  = []
        points2   = []; points2[:] = []
 
        precision = 1000                                                      # permet 3 decimales = 0.001
        dash01    = dash01  * precision
        space01   = space01 * precision
        dash02    = dash02  * precision
        space02   = space02 * precision
 
        try:
#######Selectionne un ou des objets vue 3D ou vue combinnee (subObjects complete) getSelection()############################
#            compt_Oject = -1                                                                                              #
#            selectionObjects = FreeCADGui.Selection.getSelection()                                                        # Select an object or primitive getSelection()
#            for selection in enumerate(selectionObjects):                                                                 #
#                compt_Oject += 1                                                                                          #
#                compt_Edges = -1                                                                                          #
#                for selectedEdge in enumerate(selectionObjects[compt_Oject].Shape.Edges):                                 # Search the "Edges" and their lengths
#                    compt_Edges += 1                                                                                      #
#                    longueur = (selectionObjects[compt_Oject].Shape.Edges[compt_Edges].Length) * precision                #
#                    if (dash01 + space01 + dash02 + space02) >= longueur:                                                 #
#                        dash01    = int(longueur / 6)                                                                     # altenate solution
#                        space01   = int(longueur / 6)                                                                     # altenate solution
#                        dash02    = int(longueur / 6)                                                                     # altenate solution
#                        space02   = int(longueur / 6)                                                                     # altenate solution
#                        FreeCAD.Console.PrintError("Alernate Dash"+"\n")                                                  # altenate solution
#                    numberOfPoints = longueur                                                                             #
#                    points = selectionObjects[compt_Oject].Shape.Edges[compt_Edges].discretize(int(numberOfPoints))       # Dicretize
############################################################################################################################
#####selection 1 objet ou sous objet a la fois dans la vue 3D getSelectionEx()#############################################
            selectionObjects = FreeCADGui.Selection.getSelectionEx()                                                      # Select an object or sub object getSelectionEx
            for selection in selectionObjects:                                                                            #
                for selectedEdge in selection.SubObjects:                                                                 #
                    longueur = (selectedEdge.Length) * precision                                                          #
                    if (dash01 + space01 + dash02 + space02) >= longueur:                                                 # altenate solution
                        dash01    = int(longueur / 6)                                                                     # altenate solution
                        space01   = int(longueur / 6)                                                                     # altenate solution
                        dash02    = int(longueur / 6)                                                                     # altenate solution
                        space02   = int(longueur / 6)                                                                     # altenate solution
                        FreeCAD.Console.PrintError("Alernate Dash"+"\n")                                                  # altenate solution
                    numberOfPoints = longueur                                                                             #
                    points = selectedEdge.Edges[0].discretize(int(numberOfPoints))                                        # Dicretize
###########################################################################################################################
            #######cut line in dashDot coordinates#########################################################################
                    compt = 0
                    points2 += [points[0]]
 
                    for ii2 in range(len(points)):
                        try:
                            compt += int(dash01)
                            points2 += [points[compt]]
                            compt += int(space01)
                            points2 += [points[compt]]
                            if typeLine > 1:                                  # typeLine = 2    "___ _ ___ _ ___ _ "  dash dot
                                compt += int(dash02)
                                points2 += [points[compt]]
                                compt += int(space01)
                                points2 += [points[compt]]
                                if typeLine > 2:                              # typeLine = 3    "___ _ _ ___ _ _ ___" dash dot dot
                                    compt += int(dash02)
                                    points2 += [points[compt]]
                                    compt += int(space01)
                                    points2 += [points[compt]]
                        except Exception:
                            points2 += [points[-1]]
                            points2[-1] = points[-1]
                            break
 
                    createLines(len(points2), points2)
            #######cut line in dash coordinates##############################################################################
 
                    if compLine == 0:
                        comp = Part.makeCompound(ligne)                           # si compount ligne separee
                        Part.show(comp)                                           # si compount ligne separee
                    else:
                        comp2 += ligne
                    colorize()
                    ligne[:]  = []                                            # si compount ligne separee
 
                    points[:]  = []
                    points2[:] = []
 
            for i in nom:
                FreeCAD.ActiveDocument.removeObject(i)
 
            if compLine != 0:                                                 # 1 = toutes les selections en un compount
                comp = Part.makeCompound(comp2)                               # si compount ensemble complet
                Part.show(comp)                                               # si compount ensemble complet
                colorize()
 
            nom[:]     = []
            ligne[:]   = []
            comp2[:]   = []
            points[:]  = []
            points2[:] = []
 
        except Exception:
            FreeCAD.Console.PrintError("can not create"+"\n")
    else:
        FreeCAD.Console.PrintError("Zero not permitted"+"\n")
 
#dashLine(dash01 = 1.0, space01 = 0.2, dash02 = 0.2, space02 = 0.2, compLine = 0, red = 0, green = 0, blue = 255, typeLine = 2)