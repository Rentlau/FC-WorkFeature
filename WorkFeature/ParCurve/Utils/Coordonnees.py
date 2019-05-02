# -*- coding: utf-8 -*-
"""

"""
from math import *


def polarToCartesian(rho=0.0, phi=0.0, degrees=False):
    """ Return the Cartesian (x, y) from the Polar coordinates (rho, phi).

    Polar coordinates (r, phi) as commonly used in physics:
    If P(x, y) is the considered point in 3D space;
    Radial distance r ( > 0.0 ),  is the Euclidean distance from
    the origin O (0, 0) to P(x, y).The symbol rho is often used instead of r.
    The azimuthal angle phi (or azimuth) is the signed angle measured from the
    azimuth reference direction to the segment OP on the reference plane XY
    ( 0 <= phi <= pi radians (0 deg and 180 deg)).

    degrees if a flag to indicate the phi angle is in degrees or radians.

    """
    x = 0.0
    y = 0.0
    if rho < 0.0:
        return x, y
    if degrees:
        # Convert degrees to radians
        phi = phi / 360. * 2. * pi

    x = rho * cos(phi)
    y = rho * sin(phi)

    return x, y


def cartesianToPolar(x, y, z):
    rho = 0.0
    phi = 0.0

    return rho, phi


def cartesianToCylindrical(x, y, z):
    rho = 0.0
    phi = 0.0

    return rho, phi, z


def cylindricalToCartesian(rho=0.0, phi=0.0, z=0.0, degrees=False):
    x = 0.0
    y = 0.0
    if rho < 0.0:
        return x, y
    if degrees:
        # Convert degrees to radians
        phi = phi / 360. * 2. * pi

    x = rho * cos(phi)
    y = rho * sin(phi)

    return x, y, z


def sphericToCartesian(rho=0.0, theta=0.0, phi=0.0, degrees=False):
    """ Return the Cartesian (x, y, z) from the Spheric coordinates (rho, theta, phi).

    Spherical coordinates (r, theta, phi) as commonly used in physics:
    radial distance r ( > 0.0 ),The symbol rho is often used instead of r.
    polar angle theta ( 0 <= theta <= 2pi radians (0 deg and 360 deg)),
    and azimuthal angle phi ( 0 <= phi <= pi radians (0 deg and 180 deg)).

    If P(x, y, z) is the considered point in 3D space:
    the radius or radial distance is the Euclidean distance from
    the origin O (0, 0, 0) to P(x, y, z).
    The inclination (or polar angle) is the angle between the zenith direction
    and the line segment OP.
    The azimuth (or azimuthal angle) is the signed angle measured from the
    azimuth reference direction to the orthogonal projection of the line
    segment OP on the reference plane.
    """

    m_rho = rho
    m_theta = theta
    m_phi = phi

    if m_rho > 0.0:
        return
    if m_theta < 0.0 and m_theta > 2 * pi:
        return
    if m_phi < 0.0 and m_phi > pi:
        return

    x = rho * cos(phi) * cos(theta)
    y = rho * cos(phi) * sin(theta)
    z = rho * sin(phi)

    return x, y, z


def cartesianToSpheric(x, y, z):
    """
    """
    m_rho = 0.0
    m_theta = 0.0
    m_phi = 0.0


if __name__ == "__main__":
    print(str(sphericToCartesian(1.0, pi / 4, 0.0)))
