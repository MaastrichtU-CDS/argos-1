# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pydicom as dicom
import os
import re

folderPath = 'C:/something' #CHANGE ME!
listOfFiles = [os.path.join(dp, f) for dp, dn, filenames in os.walk(folderPath) for f in filenames if not f.startswith('.')]



for ff in listOfFiles:
    try:
        this = dicom.read_file(ff,force=True)
        if this.Modality=='RTSTRUCT':
            for i in range(len(this.StructureSetROISequence)-1,-1,-1 ):
                if re.search(r'GTVp',this.StructureSetROISequence[i].ROIName):  #CHANGE HERE if you have ohter ROI names
                    print(this.StructureSetROISequence[i].ROIName)
                    this.StructureSetROISequence[i].ROIName = 'GTV-1'
                    print(this.StructureSetROISequence[i].ROIName)
            this.save_as(ff)
    except:
        pass
