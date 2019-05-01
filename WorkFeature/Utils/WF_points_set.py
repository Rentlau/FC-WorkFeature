# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 22:19:48 2016

@author: laurent
"""
import os


def write_ascii(filename, text):
    """Write the text into an ASCII file.

    **Return** True if success, false if not.

    *filename*: (string) full path name.

    *text*: (string) the text to write.

    >>> filename = "toto.txt"
    >>> text = "my text to write!"
    >>> write_ascii(filename, text)
    """
    if (None in [filename, text]):
        print("\nERROR in: " + str(write_ascii.func_name))
        print("At least one of arguments not defined !")
        return False
    try:
        __m_f = open(filename, 'w')
        __m_f.write(text)
        __m_f.close()
        return True
    except Exception as inst:
        print(inst.args)
        print("\nERROR:in: " + str(write_ascii.func_name))
        print("The file " + str(filename) + " cannot be opened in write mode !")
        return False


class points_set():
    def __init__(self, points=None, filename="pointSet.txt"):
        """Create a points_set object.

        *points*: (tuple, list, dict or set) a serie of triplet (x, y, z).

        *filename*: (string) full path name.

        **Return**: None if points not defined
            False if points not (tuple, list, dict, set)

        >>> # To load a set of points from titi.txt
        >>> m_pts = points_set([],"titi.txt")
        >>> m_points = m_pts.load()
        """
        if (None in [points]):
            print("\nERROR in: points_set.__init__")
            print("'points' not defined !")
            return None

        if not isinstance(points, (tuple, list, dict, set)):
            print("\nERROR in: points_set.__init__")
            print("points arguments must be one of (tuple, list, dict, set) !")
            return False

        self.__points = list(points)
        self.__format = '<15.3f'
        if filename is None:
            filename = "pointSet.txt"
        self.__filename = filename

    def __str__(self):
        return str(self.__points)

    def load(self, filename=None):
        """Load a set of points from an ASCII file.

        ASCII format is 3 values by line separated by blank as:
        <15.3f  <15.3f  <15.3f
        Values are read as float

        Lines starting with characeter: # or / are considered as comment lines

        *filename*: (string) full path name.

        >>> # To read
        >>> m_pts2 = points_set([],"titi.txt")
        >>> m_points =  m_pts2.load()
        >>> print m_points
        >>> # or
        >>> print points_set([],"tutu.txt").load()
        """
        if (None in [filename]):
            m_file = self.__filename
        else:
            m_file = filename
        if not os.path.exists(m_file):
            print("\nERROR in: points_set.load")
            print("not able to find the file " + str(m_file) + " !")
            return False
        try:
            fo = open(m_file, 'r')
            fo.close()
        except Exception as inst:
            print(inst.args)
            print("\nERROR in: points_set.load")
            print("not able to open the file " + str(m_file) + " !")
            return False
        with open(m_file, 'r') as f:
            m_points = []
            for line in f:
                x = 0.0
                y = 0.0
                z = 0.0
                if line[0] == '#' or line[0] == '/':
                    continue
                words = line.strip().split()

                if len(words) == 0:
                    continue
                if words[0] == '#' or line[0] == '/':
                    continue
                if len(words) >= 1:
                    x = words[0]
                if len(words) >= 2:
                    y = words[1]
                if len(words) >= 3:
                    z = words[2]
                m_points.append((x, y, z))

        if len(m_points) == 0:
            print("\nWARNING in: points_set.load")
            print("no point read from the file " + str(m_file) + " !")
            return False
        self.__points.append(m_points)
        return m_points

    def save(self, filename=None, fmt='<15.3f'):
        """Save a points set into an ASCII file.

        One (x, y, z) triplet per line separated by blank.

        *filename*: (string) full path name.

        *fmt*: (char or string) format pattern.

        >>> # Save from a list
        >>> m_points = []
        >>> x = 0.0; y = 10.0; z = 10.0
        >>> m_points.append((x, y, z))
        >>> x = 0.0; y = 0.0; z = 10.0
        >>> m_points.append((x, y, z))
        >>> m_pts = points_set(m_points)
        >>> m_pts.save("titi.txt")
        >>> # or
        >>> sample = [(-1, -1, 0.0), (0, 3, 0.0), (1, 2.5, 0.0), (2, 5, 0.0), (3, 4, 0.0), (5, 2, 0.0), (7, 5, 0.0), (9, 4, 0.0)]
        >>> m_points2 = list(sample)
        >>> m_pts1 = points_set(m_points2, filename="tutu.txt")
        >>> m_pts1.save()
        """
        if (None in [filename]):
            m_file = self.__filename
        else:
            m_file = filename
        try:
            fo = open(m_file, 'w')
            fo.close()
        except Exception as inst:
            print(inst.args)
            print("\nERROR in: points_set.save")
            print("not able to open the file " + str(m_file) + " !")
            return False

        if len(self.__points) < 1:
            return False

        self.__format = fmt
        with open(m_file, 'w') as f:
            # m_line = "# ASCII:  <15.3f  <15.3f  <15.3f\n"
            m_line = "# ASCII:  " + str(self.__format) + "  " + str(self.__format) + "  " + str(self.__format) + "\n"
            f.write(m_line)
            m_format = "{0:" + str(self.__format) + "}"
            for m_point in self.__points:
                m_line = "  "
                for m_i in range(2):
                    # m_line = m_line + '{0:<15.3f}'.format(m_point[m_i])
                    m_line = m_line + str(m_format).format(m_point[m_i])
                    m_line = m_line + "  "
                m_i = 2
                # m_line = m_line + '{0:<15.3f}'.format(m_point[m_i])
                m_line = m_line + str(m_format).format(m_point[m_i])
                m_line = m_line + '\n'
                f.write(m_line)

        return True


if __name__ == "__main__":
    filename = "toto.txt"
    text = "my text"
    write_ascii(filename, text)

    m_points = []
    x = 0.0
    y = 10.0
    z = 10.0
    m_points.append((x, y, z))
    x = 0.0
    y = 0.0
    z = 10.0
    m_points.append((x, y, z))
    x = 10.0
    y = 0.0
    z = 10.0
    m_points.append((x, y, z))
    x = 10.0
    y = 0.0
    z = 0.0
    m_points.append((x, y, z))
    x = 0.0
    y = 0.0
    z = 10.0
    m_points.append((x, y, z))
    x = 0.0
    y = 0.0
    z = 0.0
    m_points.append((x, y, z))
    x = 10.0
    y = 10.0
    z = 10.0
    m_points.append((x, y, z))
    x = 10.0
    y = 10.0
    z = 0.0
    m_points.append((x, y, z))

    m_pts = points_set(m_points)
    m_pts.save("titi.txt")
    print("Save done!")

    sample = [(-1, -1, 0.0), (0, 3, 0.0), (1, 2.5, 0.0), (2, 5, 0.0), (3, 4, 0.0), (5, 2, 0.0), (7, 5, 0.0), (9, 4, 0.0)]
    m_points2 = list(sample)
    m_pts1 = points_set(m_points2, filename="tutu.txt")
    m_pts1.save()
    print("Save done!")

    m_pts2 = points_set([], "titi.txt")
    m_points = m_pts2.load()
    print("First set of points after reading: ")
    print(m_points)
    print("Second set of points after reading: ")
    print(points_set([], "tutu.txt").load())
