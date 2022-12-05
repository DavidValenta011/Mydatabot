print("hura")

import numpy as np
import pandas as pd

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

if __name__ == "__main__":
    testobject = NonRdfResource("iririr", pd.DataFrame())
