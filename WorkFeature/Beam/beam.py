# -*- coding: utf-8 -*-

import os
import FreeCAD as App
import FreeCADGui as Gui
import Part

def sketch_normal(sketch):
    a = App.Vector(0, 0, 1)
    return sketch.Placement.Rotation.multVec(a)

def project_to_plane(plane_p, plane_n, p, n):
    '''p + l * n = plane_p + x * plane_n'''
    return p + n * (plane_n.dot(plane_p - p) / (n.dot(plane_n)))

class Beam():
    def __init__(self, obj, profile, path, path_name):
        "'''Beam: representing a straight extrusion of a profile'''"
        obj.addProperty("App::PropertyString", "type", "Beam", "type of the object").type = "beam"
        obj.addProperty("App::PropertyLink","profile","Beam","sketch profile of the beam").profile = profile
        obj.addProperty("App::PropertyLink","path","Beam","path of the beam").path = path
        obj.addProperty("App::PropertyString","path_name","Beam", "name of beam line").path_name = path_name
        obj.addProperty("App::PropertyDistance", "exdent_1", "Beam", "exdent side 1").exdent_1 = "0 mm"
        obj.addProperty("App::PropertyDistance", "exdent_2", "Beam", "exdent side 2").exdent_2 = "0 mm"
        obj.setEditorMode("path_name", 1)
        obj.Proxy = self
        self.Object = obj
        

    def initialize(self):
        print("initialize ...")

    @property
    def profile(self):
        profile = Part.Face(self.Object.profile.Shape.Wires)
        if profile.Area < 0:
            profile = Part.Face(self.Object.profile.Shape.Wires[::-1])
        return profile

    @property
    def outer_shape(self):
        path, a, b, n = self.path_a_b_n
        profile = Part.Face(self.profile.Wires[0])
        new_profile = self.transform_to_n(profile, self.midpoint, a - n * self.Object.exdent_1.Value, n)
        return new_profile.extrude(App.Vector(b - a) + n * (self.Object.exdent_1.Value + self.Object.exdent_2.Value))

    def attach(self, fp):
        fp.Proxy.Object = fp

    def execute(self, fp):
        '''Do something when doing a recomputation, this method is mandatory'''
        fp.Proxy.Object = fp
        path, a, b, n = self.path_a_b_n
        new_profile = self.transform_to_n(self.profile, self.midpoint, a - n * fp.exdent_1.Value, n)
        fp.Shape = new_profile.extrude(App.Vector(b - a) + n * (fp.exdent_1.Value + fp.exdent_2.Value))

    def transform_to_n(self, profile, midpoint, p, n):
        '''transform a profile (Shape) lying in z = 0 to p and n'''

        t = sketch_normal(self.Object.path)
        n.normalize()
        v = n.cross(t)

        mat2 = App.Matrix()
        mat2.move(App.Vector() - midpoint)
        new_profile = profile.transformGeometry(mat2)

        rot_mat = App.Matrix()
        rot_mat.A11 = v.x
        rot_mat.A21 = v.y
        rot_mat.A31 = v.z
        rot_mat.A12 = t.x
        rot_mat.A22 = t.y
        rot_mat.A32 = t.z
        rot_mat.A13 = n.x
        rot_mat.A23 = n.y
        rot_mat.A33 = n.z
        new_profile = new_profile.transformGeometry(rot_mat)

        mat3 = App.Matrix()
        mat3.move(p)
        new_profile.transformShape(mat3)
        return new_profile

    @property
    def midpoint(self):
        profile_midpoint = filter(lambda x: isinstance(x, App.Base.Vector), self.Object.profile.Geometry)
        if len(profile_midpoint) == 0 or profile_midpoint is None:
            profile_midpoint = App.Vector(0, 0, 0)
        else:
            profile_midpoint = profile_midpoint[0]
        return profile_midpoint

    @property
    def path_a_b_n(self):
        path = self.Object.path.Shape.getElement(self.Object.path_name)
        a, b = path.Vertexes
        n = b.Point - a.Point
        n.normalize()
        return (path, a.Point, b.Point, n)

    @property
    def profile_bound_box(self):
        fac = 0.3
        bb = self.Object.profile.Shape.BoundBox
        xmax = bb.XMax + bb.XLength * fac
        xmin = bb.XMin - bb.XLength * fac
        ymax = bb.YMax + bb.YLength * fac
        ymin = bb.YMin - bb.YLength * fac
        pol = Part.makePolygon(
            [App.Vector(xmax, ymax, 0),
             App.Vector(xmax, ymin, 0),
             App.Vector(xmin, ymin, 0),
             App.Vector(xmin, ymax, 0),
             App.Vector(xmax, ymax, 0)])
        path, a, b, n = self.path_a_b_n
        return self.transform_to_n(pol, self.midpoint, a, n)

    def project_profile_bound_box(self, plane_n, plane_p):
        bb = self.profile_bound_box.Vertexes
        vectors = [v.Point for v in bb]
        path, a, b, n = self.path_a_b_n
        projected = [project_to_plane(plane_p, plane_n, v, n) for v in vectors]
        projected.append(projected[0])
        pol = Part.makePolygon(projected)
        return pol

    def __getstate__(self):
        return None

    def __setstate__(self, state):
        return None


class ViewProviderBeam:
    def __init__(self, obj):
        ''' Set this object to the proxy object of the actual view provider '''
        obj.Proxy = self

    def attach(self, vobj):
        self.vobj = vobj

    def getIcon(self):
        _dir = os.path.dirname(os.path.realpath(__file__))
        return(_dir + "/" + "Icons/beam.png")

    def __getstate__(self):
        return None

    def __setstate__(self, state):
        return None
 
 
def makeBeam2():
    def plot_edge(Vector_A, Vector_B, part="Part::Feature", name="Edge", grp="Work"):
        if not(App.ActiveDocument.getObject( grp )):
            App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
        edge = App.ActiveDocument.addObject(part, name)
        edge.Shape = Part.makeLine(Vector_A, Vector_B)
        App.ActiveDocument.getObject( grp ).addObject(edge)
        edge_User_Name = edge.Label
            
        return edge_User_Name, edge
    
    def plot_shape(Shape, part="Part::Feature", name="Shape", grp="Work"):
        if not(App.ActiveDocument.getObject( grp )):
            App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
        shape = App.ActiveDocument.addObject(part, name)
        shape.Shape = Part.Shape(Shape)
        App.ActiveDocument.getObject( grp ).addObject(shape)
        shape_User_Name = shape.Label
            
        return shape_User_Name, shape
    
    from FreeCAD import Base
    V1 = Base.Vector(0,10,0)
    V2 = Base.Vector(30,10,0)
    V3 = Base.Vector(30,-10,0)
    V4 = Base.Vector(0,-10,0)
    
    VC1 = Base.Vector(-10,0,0)
    C1 = Part.Arc(V1,VC1,V4)
    L0 = Part.Line(V1,V4)
    S0 = Part.Shape([C1,L0])
    
    v1 = App.Vector(0,0,0)    
    v2 = App.Vector(10,0,0)
    v3 = App.Vector(0,10,0)
    #profile = Part.makePolygon([v1,v2,v3,v1])
    v4 = App.Vector(0,0,100)
    L1 = Part.Line(v1,v4)
    S1 = Part.Shape([L1])
    
    
    #path = Part.makeLine(v1, v4)
    App.newDocument() 
    

    shape_User_Name, shape = plot_shape([C1,L0], part="Part::Feature", name="profile", grp="Work")
    edge_User_Name, edge = plot_edge(v1, v4, part="Part::Feature", name="path", grp="Work")

       
    a=App.ActiveDocument.addObject("Part::FeaturePython","Beam")
    Beam(a, shape_User_Name, edge_User_Name, "Beam")
    ViewProviderBeam(a.ViewObject)
    
class make_beam(object):
    def __init__(self, view):
        self.profile = None
        self.midpoint = None
        self.path = None
        self.n = None
        self.view = view
        App.Console.PrintMessage("choose the profile\n")
        Gui.Selection.clearSelection()
        self.klick_event = self.view.addEventCallback("SoMouseButtonEvent", self.choose_profile)
        

    def choose_profile(self, cb):
        if cb["State"] == "DOWN":
            sel = Gui.Selection.getSelection()
            if len(sel) > 0:
                self.profile = sel[0]
                App.Console.PrintMessage("Profile selected !\n")
                Gui.Selection.clearSelection()
                self.view.removeEventCallback("SoMouseButtonEvent", self.klick_event)
                self.klick_event = self.view.addEventCallback("SoMouseButtonEvent", self.choose_path)
                App.Console.PrintMessage("choose path\n")

    def choose_path(self, cb):
        if cb["State"] == "DOWN":
            sel = Gui.Selection.getSelectionEx()
            if sel:
                path_sketch = sel[0].Object
                path_name = sel[0].SubElementNames[0]
                App.Console.PrintMessage("Path selected !\n")
                self.view.removeEventCallback("SoMouseButtonEvent", self.klick_event)

                a = App.ActiveDocument.addObject("Part::FeaturePython","beam")
                Beam(a, self.profile, path_sketch, path_name)
                ViewProviderBeam(a.ViewObject)
                App.ActiveDocument.recompute()


                App.Console.PrintMessage("end of tube tool\n")


if __name__ == "__main__":
    view = Gui.ActiveDocument.activeView()
    selection = make_beam(view)

# if __name__ == '__main__':
#     makeBeam()
    