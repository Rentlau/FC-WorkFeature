# WorkFeature
Tool utility to create:
- Origin (X, Y Z axes, Origin (0,0,0) point and XZ, XY, YZ planes)
- Points (Center of Mass of object(s), mid points, center of circle, ...), 
- Axes (from 2 points, Normal of a plane...), 
- Planes (from 3 points, from one axis and a point...) 
and many other useful features to facilitate the creation of your project. 

This utility is up next in the combo view with "Work Features" label.
Several Tab will be added into this widget:
- W.F. (for tools access) and Pref. (For preferences...dev on going)
- into Tab W.F. :
  - Origin (for Origin tools)
  - Point  (for Point creation)
  - Axis   (for Axis creation)
  - Circle (for Circle and Ellipse creation)
  - Plane  (for Plane creation)
  - Object (for Bounding box and Object creation)
  - View   (for View change)
  - Modif. (for Object cutting)
    

The MACRO will create into your FreeCAD document a new Group named `WorkFeatures`.
Depending of the tool you will use it can be created the following sub Groups:
- WorkFeatures/
  - Origin
  - WorkPoints
  - WorkAxes
  - WorkPlanes
  - WorkBoxes
  - WorkObjects
