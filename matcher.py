from entities.user import User
from entities.ticket import Ticket
from entities.organization import Organization


class Matcher:
    def __init__(self, org_container, tick_container, user_container, searching_on, field, value):
        self.orgs = org_container
        self.tickets = tick_container
        self.users = user_container
        self.searching_on = searching_on
        self.match_field = field
        self.match_value = value

    @property
    def match_data(self):
        if self.searching_on == "users":
            return self.users
        elif self.searching_on == "tickets":
            return self.tickets
        elif self.searching_on == "organizations":
            return self.orgs

    def get_entity_data_by_field_value(self):
        if self.match_field not in self.match_data.all_fields:
            return []
        else:
            results = []
            all_values = []
            for i, ent in enumerate(self.match_data.data):
                curr_value = ent.get(self.match_field, "")
                all_values.append((i, curr_value))
            for ind, val in all_values:
                if type(val) is list:
                    if self._is_value_in_array(val):
                        results.append(self.match_data.data[ind])
                if type(val) is bool:
                    if self._does_value_match_case_insensitive(val):
                        results.append(self.match_data.data[ind])
                else:
                    if str(self.match_value) == str(val):
                        results.append(self.match_data.data[ind])
            return results

    def _does_value_match_case_insensitive(self, val):
        if str(self.match_value).lower() == str(val).lower():
            return True
        else:
            return False

    def _is_value_in_array(self, array):
        if self.match_value in array:
            return True
        else:
            return False

    def _get_user_by_id(self, user_id):   # assume user id is unique
        user = next((user for user in self.users.data if user["_id"] == user_id), None)
        return user

    def _get_org_by_id(self, org_id):   # assume org id is unique
        org = next((org for org in self.orgs.data if org["_id"] == org_id), None)
        return org

    def get_associated_entity_data(self, results):
        associated_results = []
        if self.searching_on == "users":
            for user in results:
                user_org = self._get_org_by_id(user["organization_id"]) if user.get("organization_id") else None
                submitted_tickets = [ticket for ticket in self.tickets.data if ticket.get("submitter_id") == user["_id"]]
                assigned_tickets = [ticket for ticket in self.tickets.data if ticket.get("assignee_id") == user["_id"]]
                user_obj = User(user, self.users.all_fields, user_org, submitted_tickets, assigned_tickets)
                associated_results.append(user_obj)
        elif self.searching_on == "tickets":
            for ticket in results:
                ticket_submitter = self._get_user_by_id(ticket.get("submitter_id"))
                ticket_assignee = self._get_user_by_id(ticket.get("assignee_id"))
                ticket_org = self._get_org_by_id(ticket.get("organization_id"))
                ticket_obj = Ticket(ticket, self.tickets.all_fields, ticket_submitter, ticket_assignee, ticket_org)
                associated_results.append(ticket_obj)
        elif self.searching_on == "organizations":
            for org in results:
                org_ticket = [t for t in self.tickets.data if t.get("organization_id") == org["_id"]]
                org_users = [u for u in self.users.data if u.get("organization_id") == org["_id"]]
                org_obj = Organization(org, self.orgs.all_fields, org_ticket, org_users)
                associated_results.append(org_obj)
        return associated_results

