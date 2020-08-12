# Welcome, this is the PyEnzymeML documentation

## 1 Read EnzymeML files from Omex

### import EnzymeML Reader:

- import from pyenzyme.enzymeml.tools import EnzymeMLReader 

### Open EnzymeML File:

- doc = EnzymeMLReader().readFromFile("Filename.omex", omex=True)

---

### Extract information from EnzymeML

#### Step 2.1 Extract Dictionarys from EnzymeML

- proteinDict = doc.getProteinDict() **--> calls the Dictionary containing all Protein Infromtion**

Further dictionary extraction function are:  


**- doc.getUnitDict()**  
**- doc.getReactantDict()**  
**- doc.getReactionDict()**

#### Step 2.2 Extract Objects from Dictionarys

- protein = proteinDict['id']

--> This function extracts the object to the corresponding *id*

#### Step 2.3 Extract attribute from Object

- proteinName = protein.getName()

**All selectors are displayed here** 


 


--> Extract Dicionary with n entries:

{
    "s0":Python Object containing all Information of Protein s0,
    "s0":Python Object containing all Information of Protein s1
}

- Extractin information of the Object

Dict[id].getName() --> extracts name
Dict[id].getId() --> extracts id
Dict[id].getUnit() --> extract Unit
...




