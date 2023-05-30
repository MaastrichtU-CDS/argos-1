# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 12:23:48 2020
 
@author: Leonard Wee
"""
import os
#import pandas as pd
import pydicom as dicom
import json
import re


def generator(homeFolder,outputdir):
  jsonfile_list = []
  #Spinal-Cord dictionary
  spinalcorddict = {
          "labelID": 1,
          "SegmentDescription": "Spinal-Cord",
          "SegmentAlgorithmType": "MANUAL",
          "SegmentedPropertyCategoryCodeSequence": {
            "CodeValue": "123037004",
            "CodingSchemeDesignator": "SCT",
            "CodeMeaning": "Anatomical Structure"
          },
          "SegmentedPropertyTypeCodeSequence": {
            "CodeValue": "2748008",
            "CodingSchemeDesignator": "SCT",
            "CodeMeaning": "Spinal cord"
          },
          "recommendedDisplayRGBValue": [
            244,
            214,
            49
          ]
        }
  
  #Esophagus dictionary
  esophagusdict = {
          "labelID": 1,
          "SegmentDescription": "Esophagus",
          "SegmentAlgorithmType": "MANUAL",
          "SegmentedPropertyCategoryCodeSequence": {
            "CodeValue": "123037004",
            "CodingSchemeDesignator": "SCT",
            "CodeMeaning": "Anatomical Structure"
          },
          "SegmentedPropertyTypeCodeSequence": {
            "CodeValue": "32849002",
            "CodingSchemeDesignator": "SCT",
            "CodeMeaning": "Esophagus"
          },
          "recommendedDisplayRGBValue": [
            211,
            171,
            143
          ]
        }
  
  #Heart dictionary
  heartdict = {
          "labelID": 1,
          "SegmentDescription": "Heart",
          "SegmentAlgorithmType": "MANUAL",
          "SegmentedPropertyCategoryCodeSequence": {
            "CodeValue": "123037004",
            "CodingSchemeDesignator": "SCT",
            "CodeMeaning": "Anatomical Structure"
          },
          "SegmentedPropertyTypeCodeSequence": {
            "CodeValue": "80891009",
            "CodingSchemeDesignator": "SCT",
            "CodeMeaning": "Heart"
          },
          "recommendedDisplayRGBValue": [
            206,
            110,
            84
          ]
        }
  
  #Lung-Left dictionary
  leftlungdict = {
          "labelID": 1,
          "SegmentDescription": "Lung-Left",
          "SegmentAlgorithmType": "SEMIAUTOMATIC",
          "SegmentAlgorithmName": "Region-growing",
          "SegmentedPropertyCategoryCodeSequence": {
            "CodeValue": "123037004",
            "CodingSchemeDesignator": "SCT",
            "CodeMeaning": "Anatomical Structure"
          },
          "SegmentedPropertyTypeCodeSequence": {
            "CodeValue": "39607008",
            "CodingSchemeDesignator": "SCT",
            "CodeMeaning": "Lung"
          },
          "SegmentedPropertyTypeModifierCodeSequence": {
            "CodeValue": "7771000",
            "CodingSchemeDesignator": "SCT",
            "CodeMeaning": "Left"
          }
        }
  
  #Lung-Right dictionary
  rightlungdict = {
          "labelID": 1,
          "SegmentDescription": "Lung-Right",
          "SegmentAlgorithmType": "SEMIAUTOMATIC",
          "SegmentAlgorithmName": "Region-growing",
          "SegmentedPropertyCategoryCodeSequence": {
            "CodeValue": "123037004",
            "CodingSchemeDesignator": "SCT",
            "CodeMeaning": "Anatomical Structure"
          },
          "SegmentedPropertyTypeCodeSequence": {
            "CodeValue": "39607008",
            "CodingSchemeDesignator": "SCT",
            "CodeMeaning": "Lung"
          },
          "SegmentedPropertyTypeModifierCodeSequence": {
            "CodeValue": "24028007",
            "CodingSchemeDesignator": "SCT",
            "CodeMeaning": "Right"
          }
        }
  
  #Lungs-Total dictionary
  totallungdict = {
          "labelID": 1,
          "SegmentDescription": "Lungs-Total",
          "SegmentAlgorithmType": "SEMIAUTOMATIC",
          "SegmentAlgorithmName": "Region",
          "SegmentedPropertyCategoryCodeSequence": {
            "CodeValue": "123037004",
            "CodingSchemeDesignator": "SCT",
            "CodeMeaning": "Anatomical Structure"
          },
          "SegmentedPropertyTypeCodeSequence": {
            "CodeValue": "39607008",
            "CodingSchemeDesignator": "SCT",
            "CodeMeaning": "Lung"
          },
          "SegmentedPropertyTypeModifierCodeSequence": {
            "CodeValue": "51440002",
            "CodingSchemeDesignator": "SCT",
            "CodeMeaning": "Right and left"
          }
        }
  
  
  #### CHANGE THIS NEXT LINE TO WHERE IS YOUR DATA! ####
  # homeFolder=r'C:/Users/Leonard Wee/Desktop/reseg/NSCLC-Radiomics-1'
  # homeFolder=r'../Data/Lung1'

  # ------------------------Below Coded by Tianchen Luo-----------------------------------
  def generate_gtv_N_dict(index):
    name = 'GTV-'+str(index)
    dict = {
        "labelID": 1,
        "SegmentDescription": name, ## note you need to somehow handle GTV-N1, GTV-N2, GTV-N* and so on …….
        "SegmentAlgorithmType": "MANUAL",
        "AnatomicRegionSequence": {
          "CodeValue": "51185008",
          "CodingSchemeDesignator": "SCT",
          "CodeMeaning": "Thorax"
        },
        "SegmentedPropertyCategoryCodeSequence": {
          "CodeValue": "49755003",
          "CodingSchemeDesignator": "SCT",
          "CodeMeaning": "Morphologically Altered Structure"
        },
        "SegmentedPropertyTypeCodeSequence": {
          "CodeValue": "108369006",
          "CodingSchemeDesignator": "SCT",
          "CodeMeaning": "Neoplasm"
        }
      }
    return dict

  def generate_gtv_dict(index):
    name = 'GTV-'+str(index)
    dict = {
        "labelID": 1,
        "SegmentDescription": name, ## note you need to somehow handle GTV-2, GTV-3, GTV-4 and so on …….
        "SegmentAlgorithmType": "MANUAL",
        "AnatomicRegionSequence": {
          "CodeValue": "39607008",
          "CodingSchemeDesignator": "SCT",
          "CodeMeaning": "Lung"
        },
        "SegmentedPropertyCategoryCodeSequence": {
          "CodeValue": "49755003",
          "CodingSchemeDesignator": "SCT",
          "CodeMeaning": "Morphologically Altered Structure"
        },
        "SegmentedPropertyTypeCodeSequence": {
          "CodeValue": "86049000",
          "CodingSchemeDesignator": "SCT",
          "CodeMeaning": "Neoplasm, Primary"
        }
      }

    return dict
  # regex to detect GTVN-1,2...N
  def regex_gtvn(name):
    match = re.search(r'^.*GTVN.*\d',name,re.M|re.I)
    found = False
    if (match != None):
        found = True
        #print('*'*5,'Find GTV','*'*5)
        
    index = re.findall(r"^.*gtvn.*(\d+)", name,re.M|re.I)

    if (found == True):
        index = int(index.pop())
    else:
        index = []

    return found,index
  # regex to detect GTV-1,2...N
  def regex_gtv(name):
    match = re.search(r'^.*GTV.*\d',name,re.M|re.I)
    found = False
    if (match != None):
        found = True
        #print('*'*5,'Find GTV','*'*5)

    index = re.findall(r"^.*gtv.*(\d+)", name,re.M|re.I)

    if(found == True):
        index = int(index.pop())
    else:
        index = []

    return found,index
  # ------------------------Above Coded by Tianchen Luo-----------------------------------

  #detect which ROIs are present
  listOfFiles = [os.path.join(dp, f) for dp, dn, filenames in os.walk(homeFolder) for f in filenames if f.endswith('dcm')]
  #print(listOfFiles)
  for ff in listOfFiles:
      try:
          gtv_list = []
          gtvN_list = []
          this = dicom.read_file(ff, force=True)
          patid = this.PatientID
          inclusionBoolean = [False,False,False,False,False,False]
          #NOTE：in alphabetical order, but lowercase will always less prior than uppercase
          #So, if there is lowercase gtv-2, it should be appended right after spinal-cord
          rois = this.StructureSetROISequence
          ctr = 0

          for r in rois:
              ctr = ctr + 1
              if r.ROIName=='Spinal-Cord':
                  inclusionBoolean[5] = True
              elif r.ROIName=='Esophagus':
                inclusionBoolean[0] = True
              elif r.ROIName=='Heart':
                  inclusionBoolean[1] = True
              elif r.ROIName=='Lung-Left':
                  inclusionBoolean[2] = True
              elif r.ROIName=='Lung-Right':
                  inclusionBoolean[3] = True
              elif r.ROIName=='Lungs-Total':
                  inclusionBoolean[4] = True
          
          #iterated over all structures
          segmentattributeslist = []

          if inclusionBoolean[0]:
              segmentattributeslist.append([esophagusdict])

          for r in rois:
            name = r.ROIName
            (is_GTVN, index_GTVN) = regex_gtvn(name)
            (is_GTV, index_GTV) = regex_gtv(name)
            if is_GTV == True:
              gtv_list.append(index_GTV)
            if is_GTVN == True:
              gtvN_list.append(index_GTVN)
          
          # Ensure Alphabet order   
          gtv_list = list(reversed(gtv_list))
          gtvN_list = list(reversed(gtvN_list))
          # append dict to segmentattributeslist
          for i in range(0,len(gtv_list)):
            segmentattributeslist.append([generate_gtv_dict(gtv_list[i])])
          for i in range(0,len(gtvN_list)):
            segmentattributeslist.append([generate_gtv_N_dict(gtvN_list[i])])

          if inclusionBoolean[1]:
              segmentattributeslist.append([heartdict])
          if inclusionBoolean[2]:
              segmentattributeslist.append([leftlungdict])
          if inclusionBoolean[3]:
              segmentattributeslist.append([rightlungdict])
          if inclusionBoolean[4]:
              segmentattributeslist.append([totallungdict])
          if inclusionBoolean[5]:
              segmentattributeslist.append([spinalcorddict])   
          masterdictionary = {
              "ContentCreatorName": "Lung1CollectionOwner",
              "ClinicalTrialSeriesID": "Session1",
              "ClinicalTrialTimePointID": "1",
              "SeriesDescription": "Segmentation",
              "SeriesNumber": "300",
              "InstanceNumber": "1",
              "BodyPartExamined": "LUNG",
              "segmentAttributes": segmentattributeslist,
              "ContentLabel": "SEGMENTATION",
              "ContentDescription": "Image segmentation",
              "ClinicalTrialCoordinatingCenterName": "dcmqi"
              }
          
          # strForOutput = 'C:/Users/Leonard Wee/Desktop/reseg/json_templates/metadata_'+patid+'.json'
          print('*'*5,"Metadata Generate successfully",'*'*5)
          strForOutput = outputdir + patid+'.json'
          jsonfile_list.append(strForOutput)
          
          with open(strForOutput, 'w') as outfile:
              json.dump(masterdictionary, outfile, indent=2, sort_keys=False)
      except:
          pass
  return jsonfile_list


if __name__ == "__main__":
  homeFolder='../Data/Lung1'
  outputdir= '../output/metadata/'
  listt = generator(homeFolder,outputdir)
  