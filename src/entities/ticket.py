from .utilities import format_timestamp


class Ticket:
    def __init__(self, data, all_fields, submitter_data, assignee_data, org_data):
        self.data = data
        self.all_fields = all_fields
        self.submitter = submitter_data
        self.assignee = assignee_data
        self.associated_org = org_data
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
    def _make_associated_user_info(user):
        user_info = f"{user['name']} (Id: {user['_id']})"
        return user_info

    @property
    def readable_data(self):
        readable_data = {
            "Id": self.data["_id"],
            "Subject": self.data["subject"],
            "Priority": self.data["priority"],
            "Status": self.data["status"],
            "Description": self.data["description"],
            "Organization name": self._make_associated_org_name(self.associated_org) if self.associated_org else "",
            "Organization Id": self.data["organization_id"],
            "URL": self.data["url"],
            "External Id": self.data["external_id"],
            "Tags": ", ".join(self.data["tags"]) if self.data["tags"] else "",
            "Created at": format_timestamp(self.data["created_at"]) if self.data["created_at"] else "",
            "Due at": format_timestamp(self.data["due_at"]) if self.data["due_at"] else "",
            "Has incidents": self.data["has_incidents"],
            "Via": self.data["via"],
        }
        if self.submitter:
            readable_data.update({"Submitter": self._make_associated_user_info(self.submitter)})
        if self.assignee:
            readable_data.update({"Assignee": self._make_associated_user_info(self.assignee)})
        return readable_data

