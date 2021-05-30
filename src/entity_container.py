import json


class EntityContainer:
    def __init__(self, entity_file_path):
        self.file_path = entity_file_path
        self.data = self.parse_entity_file()

    def parse_entity_file(self):
        try:
            with open(self.file_path, "r") as f_in:
                return json.load(f_in)
        except json.decoder.JSONDecodeError as e:
            print(f"The json file provided at {self.file_path} is invalid.\n"
                  f"Please try again with a well-formed json file.")
            raise e
        except FileNotFoundError as e:
            print(f"Unable to find the data file provided at {self.file_path}\n"
                  f"Please try again with another file location.")
            raise e

    @property
    def all_fields(self):
        all_fields = set()
        for ent in self.data:
            all_fields.update(ent.keys())
        return list(all_fields)

