import json


class EntityContainer:
    def __init__(self, entity_file_path):
        self.file_path = entity_file_path
        self.data = self.parse_entity_file()

    def parse_entity_file(self):
        with open(self.file_path, "r") as f_in:
            return json.load(f_in)

    @property
    def all_fields(self):
        all_fields = set()
        for ent in self.data:
            all_fields.update(ent.keys())
        return all_fields

