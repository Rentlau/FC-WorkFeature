
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# <center>Macro Work features for FreeCAD<br> </center>
----------

Updated in January 2018

Tool utility to create:
- Origin (X, Y Z axes, Origin (0,0,0) point and XZ, XY, YZ planes)
- Points (Center of Mass of object(s), mid points, center of circle, ...), 
- Axes (from 2 points, Normal of a plane...), 
- Planes (from 3 points, from one axis and a point...) 
and many other useful features to facilitate the creation of your project. 

<img src="./WorkFeature/Doc/Images/Documentation/Title/Title.png">

 

<center><img src="./WorkFeature/Doc/Images/Documentation/Title/WF_icon1.png"></center>





 

<center><img src="./WorkFeature/Doc/Images/Documentation/Title/WF_icon3.png"></center>

<b>Version 2018-01</b> <center>by Rentlau_64</center>

###  Installing
----------

Download and install FreeCAD from [wiki Download page](http://www.freecadweb.org/wiki/Download) and either install this macro by : 
- using the [FreeCAD macro addons_installer](https://github.com/FreeCAD/FreeCAD-addons/blob/master/addons_installer.FCMacro) to install easily WorkFeatures and other interesting macros or,
- manually by copying the WorkFeature folder into the Macro sub-directory of the FreeCAD application (most of the time ~/.FreeCAD/Macro).

see [Here](https://www.freecadweb.org/wiki/How_to_install_macros) for "How to install macros" detailed.

### Requirements
----------
Numpy is required
The development of the macro is done with Python2.7

### Abstract
----------

This utility is up next in the combo view with "Work Features" label.<br>
Several Tab panels will be added into this widget:
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
