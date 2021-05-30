from .utilities import format_timestamp


class User:
    def __init__(self, data, all_fields, org_data, submitted_data, assigned_data):
        self.data = data
        self.all_fields = all_fields
        self.associated_org = org_data
        self.submitted_tickets = submitted_data
        self.assigned_tickets = assigned_data
        self._fill_data()

    def _fill_data(self):
        for field in self.all_fields:
            if field not in self.data:
                self.data.update({field: ""})

    @staticmethod
    def _make_associated_org_name(org):
        org_name = ""
        if org.get("name"):
            org_name += org["name"]
        return org_name

    @staticmethod
    def _make_associated_ticket_list(tickets):
        ticket_list_string = "\n"
        ticket_list = []
        for ticket in tickets:
            ticket_list.append(f'  - {ticket.get("subject")}  (Id: {ticket.get("_id")})')
        ticket_list_string += "\n".join(ticket_list)
        return ticket_list_string

    @property
    def readable_data(self):
        readable_data = {
            "Id": self.data["_id"],
            "Name": self.data["name"],
            "Alias": self.data["alias"],
            "Signature": self.data["signature"],
            "Email": self.data["email"],
            "Phone": self.data["phone"],
            "Time zone": self.data["timezone"],
            "Locale": self.data["locale"],
            "Organization": self._make_associated_org_name(self.associated_org) if self.associated_org else "",
            "Organization Id": self.data["organization_id"],
            "Role": self.data["role"],
            "URL": self.data["url"],
            "External Id": self.data["external_id"],
            "Tags": ", ".join(self.data["tags"]) if self.data["tags"] else "",
            "Active": self.data["active"],
            "Verified": self.data["verified"],
            "Shared": self.data["shared"],
            "Suspended": self.data["suspended"],
            "Created at": format_timestamp(self.data["created_at"]) if self.data["created_at"] else "",
            "Last login at": format_timestamp(self.data["last_login_at"]) if self.data["last_login_at"] else ""
        }
        if self.submitted_tickets:
            readable_data.update({"Submitted tickets": self._make_associated_ticket_list(self.submitted_tickets)})
        if self.assigned_tickets:
            readable_data.update({"Assigned tickets": self._make_associated_ticket_list(self.assigned_tickets)})
        return readable_data

