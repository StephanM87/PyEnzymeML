# PyEnzymeML, Pyenz library for reading and writing of EnzymeML in Python

## EnzymeML is a XML based echange format to exchange experimental data in biocatalysis. The XML file has the following structure:  

<p align="center">
<img src="/Root/Images/PyEnzymeML.png" width="80%">
</p>

# 1. Read EnzymeML files from Omex

## import EnzymeML Reader:

- Import from pyenzyme.enzymeml.tools import EnzymeMLReader 

## Create new EnzymeML file

- doc = EnyzmeMLDocument("Name", SBMLLevel:Int, SBMLVersion:Int)

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
**- doc.getProteinDict()** 




### Step 1.2 Extract Objects from Dictionarys

- protein = proteinDict['id']

--> This function extracts the object to the corresponding *id*

### Step 1.3 Extract attribute from Object

- proteinName = protein.getName()



### Step 1.4 Extraction Selectors for Reaction Objects()

Extract first a Reaction from the EnzymeML as described in 1.1 and 1.2

--> a potential reaction object is called in this example reactionObj

- reactionObj.getId() --> Extracts the Reaction id: String
- reactionObj.getMetaId() --> Extracts the Meta id : String
- reactionObj.getph() --> Extracts the pH: float
- reactionObj.get Reversible() --> Extracts if reaction is reversible or not : boolean
- reactionObj.getTemperature() --> Extracts the temperature value : float
- reactionObj.getTempunit() --> Extracts the temperature unit Id: String
- reactionObj.getModifier() --> Extracts the Modifier: tuple

### Step 1.5 Extracting the Unit 

If you extract the Unit from an object, for example protein, reaction etc. you will not get the Unit name in return but identifier of the Unit in the *UnitDict*

to extract the unit name :
unitIdentifier = "u0"

unitDict = doc.gerUnitDict()
unitDict["u0"].getName() --> extract the name of the Unit: String
---

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

- doc.addProtein(protein)

## Step 2.2 Update Existing EnzymeMLObject


1. Access the respecive EnzymeMLObject
- protein = doc.getProteinDict()[id]  
2. Update the respective attribute
- protein.setName(String)

---

# 3. Create new EnzymeML File (.omex)

## 3.1 Import EnzymeMLwriter and EnzymeML core:
- from pyenzyme.enzymeml.tools import EnzymeMLReader, EnzymeMLWriter
- from pyenzyme.enzymeml.core import *

## 3.2 Instantiate new writer Object

- writer = EnzymeMLWriter()

## 3.3 Create new EnzymeML File (.omex)

- writer.toFile(doc, "Path")
