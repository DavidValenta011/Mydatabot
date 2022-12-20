import myResources
import rdflib
from typing import Tuple

class Container(myResources.RdfResource):
    """
    ### Linked Data Platform Container (LDPC)

    A LDP-RS representing a collection of linked documents that responds to client requests for creation, modification, and/or enumeration of its linked members and documents, and that conforms to the simple lifecycle patterns and conventions described [here](https://www.w3.org/…dpc).
    """
    def __init__(self, iri: str):
        self.iri = iri
        self.content = rdflib.Graph()
        self.documents = []

    def Graph(self):
        return self.content

    def serialize(self):
        return self.content.serialize()

    def add(self, triple):
        self.content.add(triple)


class BasicContainer(Container):
    """
    ### Linked Data Platform Basic Container (LDP-BC)

    An LDPC that defines a simple link to its contained documents (information resources).
    """
    def __init__(self, iri: str):
        super().__init__(iri)
        self.resources = []

    def SetContainer(self, c):
        self.c = c
        self.g.add((self.Node(), "ldp:Container", c))

    def Container(self):
        return self.c

class DirectContainer(Container):
    """
    ### Linked Data Platform Direct Container (LDP-DC)

    An LDPC that adds the concept of membership, allowing the flexibility of choosing what form its membership triples take, and allows members to be any resources, not only documents.
    """
    def __init__(self, iri: str):
        super().__init__(iri)

class IndirectContainer(Container):
    """
    ### Linked Data Platform Indirect Container (LDP-IC)

    An LDPC similar to a LDP-DC that is also capable of having members whose URIs are based on the content of its contained documents rather than the URIs assigned to those documents.
    """
    def __init__(self, iri: str):
        super().__init__(iri)
