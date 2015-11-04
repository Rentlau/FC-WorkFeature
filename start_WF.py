# -*- coding: utf-8 -*-
import sys
import os.path

try:
    # try import
    import WorkFeature.WF_2015 as WF
except:
    # get the path of the current python script    
    m_current_path = os.path.realpath(__file__)
    m_current_path = os.path.dirname(m_current_path)
    # check if this path belongs to the PYTHONPATH variable and if not add it
    if not sys.path.__contains__(str(m_current_path)):
        sys.path.append(str(m_current_path))
    # retry import now
    import WorkFeature.WF_2015 as WF
  
WF.myDialog = WF.WorkFeatureTab()
