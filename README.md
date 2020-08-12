# Welcome, this is the PyEnzymeML documentation

<img src="/Root/Images/PyEnzymeML.png" width="80%">
      
# 1. Read EnzymeML files from Omex

## import EnzymeML Reader:

- Import from pyenzyme.enzymeml.tools import EnzymeMLReader 

## Open EnzymeML File:

- doc = EnzymeMLReader().readFromFile("Filename.omex", omex=True)

---

## Extract information from EnzymeML

### Step 1.1 Extract Dictionarys from EnzymeML

- proteinDict = doc.getProteinDict() **--> calls the Dictionary containing all Protein Infromtion**

Further dictionary extraction function are:  


**- doc.getUnitDict()**  
**- doc.getReactantDict()**  
**- doc.getReactionDict()**

### Step 1.2 Extract Objects from Dictionarys

- protein = proteinDict['id']

--> This function extracts the object to the corresponding *id*

### Step 1.3 Extract attribute from Object

- proteinName = protein.getName()

**All selectors are displayed here** 

# 2. Write/Update EnzymeML

## Step 2.1 Create new EnzymeML EnzymeMLObjects

- protein = Protein(  
    name = String,  
    id=String,  
    metaid=String,  
    seuquence=String,  
    sboterm=String,  
    compartment_id=String,  
    init_conc=float,  
    substance_units=String,  
    boundary=bool,  
    constant=bool)

## Step 2.2 Update Existing EnzymeMLObject

1. Access the respecive EnzymeMLObject
- protein = doc.getProteinDict()[id]  
2. Update the respective attribute
- protein.setName(String)

# 3. Create new EnzymeML File (.omex)

## 3.1 Import EnzymeMLwriter and EnzymeML core:
- from pyenzyme.enzymeml.tools import EnzymeMLReader, EnzymeMLWriter
- from pyenzyme.enzymeml.core import *

## 3.2 Instantiate new writer Object

- writer = EnzymeMLWriter()

## 3.3 Create new EnzymeML File (.omex)

- writer.toFile(doc, "Path")
