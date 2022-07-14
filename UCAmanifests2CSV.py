#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 20:11:11 2022

@author: gustavo
"""

import urllib.request, json
import csv


class Record:
  def __init__(self, urlmanifest):
    
    self.manifest = json.load(urllib.request.urlopen(urlmanifest))  
      
    self.label = ''
    self.alternativeTitle = ''
    self.creatorContributor = ''
    self.dateCreatedDateIssued = ''
    self.owningRepository = ''
    self.sourceCollectionName = ''
    self.sourceCollectionURI = ''
    self.sourceCollectionLocalIdentifier = ''
    self.type = ''
    self.formMedium = ''
    self.genre = ''
    self.extent = ''
    self.language = ''
    self.topic = ''
    self.timePeriodCovered = ''
    self.geographicCoverage = ''
    self.geographicCode = ''
    self.placeName = ''
    self.cartographicInformation = ''
    self.identifierUTLDAMSPID = ''
    self.identifierLocal = ''
    self.relatedResourceHost = ''
    self.relatedResourceOther = ''
    self.primaryTitle = ''
    self.description = ''
    self.license = ''
    self.identifierPID = ''
    self.thumbnailURI = ''
    self.IIIFImage = ''
    self.IIIFResource = ''
    self.dateAdded = ''
    self.manifestURI = ''
    self.extra = ''
  
  # describe record  
  def describe(self):
      #return self.primaryTitle + " " + self.creatorContributor
      return self.extra
  
  # get all metadata fields in manifest    
  def getMetadataFields(self):
    for met in self.manifest['metadata']:
        print(met['label'])

  # get from manifest a field value
  def getFieldValue(self, field):
    #print(field)  
    for met in self.manifest['metadata']:
        if met['label'] == field:
            if isinstance(met['value'], list):
                if str(met['value']) != '[{}]':
                    value = ''
                    for mv in met['value']:
                        if '@value' in mv:
                             value = value + mv['@value'] + "@" + mv['@language'] + '|'
                        elif 'type' in mv:
                             value = value + mv['type'] + "@" + mv['@id'] + '|'     
                    return value
            elif isinstance(met['value'], dict):
                return met['value']['@value'] + "@" + met['value']['@language']
            else:
                return met['value']
  
  # set values from manifest to record
  def setValues(self):
    r.placeName = self.getFieldValue('Place Name')
    r.alternativeTitle = self.getFieldValue('Alternative Title')
    r.creatorContributor = self.getFieldValue('Creator/Contributor')
    r.dateCreatedDateIssued = self.getFieldValue('Date Created/Date Issued')
    r.owningRepository = self.getFieldValue('Owning Repository')
    r.sourceCollectionName = self.getFieldValue('Source Collection Name')
    r.sourceCollectionURI = self.getFieldValue('Source Collection URI')
    r.sourceCollectionLocalIdentifier = self.getFieldValue('Source Collection Local Identifier')
    r.type = self.getFieldValue('Type')
    r.formMedium = self.getFieldValue('Form/Medium')
    r.genre = self.getFieldValue('Genre')
    r.extent = self.getFieldValue('Extent')
    r.language = self.getFieldValue('Language')
    r.topic = self.getFieldValue('Topic')
    r.timePeriodCovered = self.getFieldValue('Time Period Covered')
    r.geographicCoverage = self.getFieldValue('Geographic Coverage')
    r.geographicCode = self.getFieldValue('Geographic Code')
    r.cartographicInformation = self.getFieldValue('Cartographic Information')
    r.identifierUTLDAMSPID = self.getFieldValue('Identifier - UTL DAMS PID')
    r.identifierLocal = self.getFieldValue('Identifier - Local')
    r.relatedResourceHost = self.getFieldValue('Related Resource - Host')
    r.relatedResourceOther = self.getFieldValue('Related Resource - Other')
    r.primaryTitle = self.getFieldValue('Primary Title')
    r.description = self.getFieldValue('Description')
    r.license = self.getFieldValue('License')
    r.identifierPID = self.getFieldValue('Identifier - PID')
    r.thumbnailURI = self.getFieldValue('Thumbnail URI')
    r.IIIFImage = self.getFieldValue('IIIF Image')
    r.IIIFResource = self.getFieldValue('IIIF Resource')
    r.dateAdded = self.getFieldValue('Date Added')
    r.manifestURI = self.getFieldValue('Manifest URI')
    r.extra = self.getFieldValue('extra')

  def getRowCSV(self):
    return [self.placeName, self.alternativeTitle,
        self.creatorContributor, self.dateCreatedDateIssued,
        self.owningRepository,self.sourceCollectionName, 
        self.sourceCollectionURI,self.sourceCollectionLocalIdentifier,  
        self.type,self.formMedium,self.genre,
        self.extent,self.language,self.topic, 
        self.timePeriodCovered,self.geographicCoverage, 
        self.geographicCode,self.cartographicInformation, 
        self.identifierUTLDAMSPID,self.identifierLocal, 
        self.relatedResourceHost,self.relatedResourceOther,
        self.primaryTitle, self.description, self.license, 
        self.identifierPID, self.thumbnailURI,self.IIIFImage,
        self.IIIFResource,self.dateAdded,self.manifestURI,self.extra]

if __name__ == "__main__":
    
    # Using readlines()
    file1 = open('input/manifests.txt', 'r')
    lines = file1.readlines()
    
    records = []
      
    count = 0
    # Strips the newline character
    for line in lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))
        urlmanifest = line.strip()
        #urlmanifest = "https://curio.lib.utexas.edu/assets/DAMS/utblac/utblac_38127378-7a33-412f-a425-cc511ff1d351/manifests/2/utblac_38127378-7a33-412f-a425-cc511ff1d351.json"
       
        r = Record(urlmanifest) 
        #r.getMetadataFields()
        r.setValues()
        print(r.describe())
        records.append(r)
        

    header = ['placeName', 'alternativeTitle',
    'creatorContributor', 'dateCreatedDateIssued',
    'owningRepository','sourceCollectionName', 
    'sourceCollectionURI','sourceCollectionLocalIdentifier',  
    'type','formMedium','genre',
    'extent','language','topic', 
    'timePeriodCovered','geographicCoverage', 
    'geographicCode','cartographicInformation', 
    'identifierUTLDAMSPID','identifierLocal', 
    'relatedResourceHost','relatedResourceOther',
    'primaryTitle', 'description', 'license', 
    'identifierPID', 'thumbnailURI','IIIFImage',
    'IIIFResource','dateAdded','manifestURI','extra']   

    with open('output/relaciones.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        
        # write the header
        writer.writerow(header)
    
        # transform to CSV
        for r in records:
            # write the data    
            writer.writerow(r.getRowCSV())
    

    

   