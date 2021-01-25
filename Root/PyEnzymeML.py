from pyenzyme.enzymeml.tools import EnzymeMLReader, EnzymeMLWriter
from pyenzyme.enzymeml.core import *
import pandas as pd

#doc = EnzymeMLReader().readFromFile("Modified.omex", omex=True)

doc = EnzymeMLDocument("Test", 3, 2)

# Create Vessel

vessel = Vessel("name", "v0", 2.0, "nmole/l")

#reactant = Protein()



doc.setVessel(vessel)

# Create Reactant

reactant = Reactant("pyruvat", "v0", 1.0, "mmole/l", False)
pyruvat = doc.addReactant(reactant)
print(pyruvat)


# Puffer wird einfach als Reactant hinzugefügt

# add Reaction

# educts, product, modifiers are not mandatory

reaction = EnzymeReaction(37.0, "C", 6.0, "Reeaktion1", True)


# addEduct : replicates are not madatrory
# Educts need to be defined previously as reactant

reaction.addEduct(pyruvat, 1.0, False, doc)

replicate = Replicate("Repl1", pyruvat, "conc", "nmole/l", "s", 1.0)
series = pd.Series([1,2,3])
series.Index = [1,2,3]
replicate.setData(series)
reaction.addReplicate(replicate, doc)



# mit reaction.exportReplicates() zieht man sich die Messdaten aus dem Omex archive

# mit doc.printReaction() zeiht man die Infos über die Reaktanden aus dem Omex file raus



doc.addReaction(reaction)

writer = EnzymeMLWriter()
writer.toFile(doc, "Neu")






