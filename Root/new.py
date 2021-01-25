from pyenzyme.enzymeml.tools import EnzymeMLReader

doc = EnzymeMLReader().readFromFile("Modified.omex", omex=True)

protein = doc.getProteinDict()

print(protein)

