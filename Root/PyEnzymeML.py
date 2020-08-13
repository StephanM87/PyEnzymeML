from pyenzyme.enzymeml.tools import EnzymeMLReader, EnzymeMLWriter
from pyenzyme.enzymeml.core import *
import pandas as pd

#doc = EnzymeMLReader().readFromFile("Modified.omex", omex=True)

doc = EnzymeMLDocument("Test", 3, 2)

# Create Vessel

vessel = Vessel("name", "v0", "meta_v0", True, 2.0, "nmol/l")

doc.setVessel(vessel)

# Create Reactant

reactant = Reactant("pyruvat", "r0", "meta_r0", "SBO:0003", "v0", 1.0, "mmol/l", False, False)
doc.addReactant(reactant)

# add Reaction

# educts, product, modifiers are not mandatory

reaction = EnzymeReaction(37.0, "°C", 6.0, "Reeaktion1", True, "reac0", "meta_reac0")


# addEduct : replicates are not madatrory
# Educts need to be defined previously as reactant

reaction.addEduct("r0", 1.0, False, doc)

replicate = Replicate("Repl1", "r0", "conc", "nmol/l", "s")
series = pd.Series([1,2,3])
series.Index = [1,2,3]
replicate.setData(series)
reaction.addReplicate(replicate)



doc.addReaction(reaction)

writer = EnzymeMLWriter()
writer.toFile(doc, "Neu")






