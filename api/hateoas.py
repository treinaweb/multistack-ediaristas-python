class Hateoas:
    def __init__(self):
        self.links = []

    def add_get(self, rel, uri):
        self.add('GET', rel, uri)
    
    def add_post(self, rel, uri):
        self.add('POST', rel, uri)

    def add_put(self, rel, uri):
        self.add('PUT', rel, uri)

    def add_patch(self, rel, uri):
        self.add('PATCH', rel, uri)

    def add_delete(self, rel, uri):
        self.add('DETELE', rel, uri)

    def add(self, type, rel, uri):
        self.links.append({
            'type': type,
            'rel': rel,
            'uri': uri
        })

    def to_array(self):
        return self.links