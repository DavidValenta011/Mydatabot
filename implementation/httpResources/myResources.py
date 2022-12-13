import rdflib

class Resource():
    """
    ### Linked Data Platform Resource (LDPR)

    A HTTP resource whose state is represented in any way that conforms to the simple lifecycle patterns and conventions described [here](https://www.w3.org/TR/ldp/#ldpr).
    """
    def __init__(self, iri: str):
        self.iri = iri

    def Node(self):
        return rdflib.BNode()

class RdfResource(Resource):
    """
    ### Linked Data Platform RDF Source (LDP-RS)

    An LDPR whose state is fully represented in RDF, corresponding to an RDF graph
    """
    def __init__(self, iri: str):
        super().__init__(iri)
        self.resources = []

    def Node(self):
        return rdflib.URIRef(self.iri)


class NonRdfResource(Resource):
    """
    ### Linked Data Platform Non-RDF Source (LDP-NR)

    An LDPR whose state is not represented in RDF. For example, these can be binary or text documents that do not have useful RDF representations.
    """
    def __init__(self, iri: str, data: str):
        super().__init__(iri)
        self.data = data
    
    def Node(self):
        return rdflib.Literal(self.data)

if __name__ == "__main__":
    pass

