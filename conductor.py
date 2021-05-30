from entity_container import EntityContainer
from matcher import Matcher


class Conductor:
    def __init__(self, file_paths, searching_on=None, search_field=None, search_value=""):
        self.file_paths = file_paths
        self.searching_on = searching_on
        self.search_field = search_field
        self.search_value = search_value
        self.TicketContainer = None
        self.UserContainer = None
        self.OrgContainer = None
        self.results = None

    def _load_user_data(self):
        self.UserContainer = EntityContainer(self.file_paths["users"])

    def _load_ticket_data(self):
        self.TicketContainer = EntityContainer(self.file_paths["tickets"])

    def _load_org_data(self):
        self.OrgContainer = EntityContainer(self.file_paths["organizations"])

    def load_all_data(self):
        self._load_user_data()
        self._load_ticket_data()
        self._load_org_data()

    def match(self):
        matcher = Matcher(self.OrgContainer, self.TicketContainer, self.UserContainer,
                          self.searching_on, self.search_field, self.search_value)
        original_results = matcher.get_entity_data_by_field_value()
        self.results = matcher.get_associated_entity_data(original_results)
        return self.results

    def print_results(self, padding=5):
        for result in self.results:
            data_to_print = result.readable_data
            max_key_length = max(len(k) for k in data_to_print.keys())
            space = max_key_length + padding
            for k, v in data_to_print.items():
                print(f"{k+':':{space}}{v}")
            print("\n")

    def list_searchable_fields(self, dataset):
        if dataset == "all":
            self.load_all_data()
            user_fields = self.UserContainer.all_fields
            print("You can search users with the below fields:")
            for field in user_fields:
                print(field)
            print("\n")
            org_fields = self.OrgContainer.all_fields
            print("You can search organizations with the below fields:")
            for field in org_fields:
                print(field)
            print("\n")
            ticket_fields = self.TicketContainer.all_fields
            print("You can search tickets with the below fields:")
            for field in ticket_fields:
                print(field)

        elif dataset == "users":
            self._load_user_data()
            user_fields = self.UserContainer.all_fields
            print("You can search users with the below fields:")
            for field in user_fields:
                print(field)

        elif dataset == "tickets":
            self._load_ticket_data()
            ticket_fields = self.TicketContainer.all_fields
            print("You can search tickets with the below fields:")
            for field in ticket_fields:
                print(field)

        elif dataset == "organizations":
            self._load_ticket_data()
            ticket_fields = self.TicketContainer.all_fields
            print("You can search tickets with the below fields:")
            for field in ticket_fields:
                print(field)

