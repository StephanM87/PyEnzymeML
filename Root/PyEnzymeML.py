from pyenzyme.enzymeml.tools import EnzymeMLReader

doc = EnzymeMLReader().readFromFile("Modified.omex", omex=True)
#print(doc)

#proteinDict = doc.getProteinDict()

#protein = proteinDict["s0"]

#print(protein.getName())
#print(protein.getId())

#unit = doc.getUnitDict()
#print(unit)

#reactant = doc.getReactantDict()
#print(reactant)

#reaction = doc.getReactionDict()
#print(reaction)
