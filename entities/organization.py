from entities.utilities import format_timestamp


class Organization:
    def __init__(self, data, all_fields, tickets_data, users_data):
        self.data = data
        self.all_fields = all_fields
        self.associated_tickets = tickets_data
        self.associated_users = users_data
        self._fill_data()

    def _fill_data(self):
        for field in self.all_fields:
            if field not in self.data:
                self.data.update({field: ""})

    @staticmethod
    def _make_associated_user_list(users):
        user_list_string = "\n"
        user_list = []
        for user in users:
            user_list.append(f"  - {user['name']} (Id: {user['_id']})")
        user_list_string += "\n".join(user_list)
        return user_list_string

    @staticmethod
    def _make_associated_ticket_list(tickets):
        ticket_list_string = "\n"
        ticket_list = []
        for ticket in tickets:
            ticket_list.append(f"  - {ticket.get('subject')}  (Id: {ticket.get('_id')})")
        ticket_list_string += "\n".join(ticket_list)
        return ticket_list_string

    @property
    def readable_data(self):
        readable_data = {
            "Id": self.data["_id"],
            "Name": self.data["name"],
            "Details": self.data["details"],
            "URL": self.data["url"],
            "External Id": self.data["external_id"],
            "Tags": ", ".join(self.data["tags"]) if self.data["tags"] else "",
            "Domain names": ", ".join(self.data["domain_names"]) if self.data["domain_names"] else "",
            "Created at": format_timestamp(self.data["created_at"]) if self.data["created_at"] else "",
            "Shared tickets": self.data["shared_tickets"]
        }
        if self.associated_users:
            readable_data.update({"Users": self._make_associated_user_list(self.associated_users)})
        if self.associated_tickets:
            readable_data.update({"Tickets": self._make_associated_ticket_list(self.associated_tickets)})
        return readable_data

