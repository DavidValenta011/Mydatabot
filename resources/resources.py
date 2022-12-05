print("hura")

class Resource():
    def __init__(self, iri):
        self.iri = iri

class RdfResource(Resource):
    def __init__(self, iri):
        super().__init__(iri)
        self.resources = []

class NonRdfResource(Resource):
    def __init__(self, iri, data):
        super().__init__(iri)
        self.data = data