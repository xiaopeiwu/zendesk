import pytest
from src.matcher import Matcher
from src.entity_container import EntityContainer


@pytest.fixture()
def sample_matcher():
    return Matcher(EntityContainer("tests/fixtures/organizations_fixture.json"),
                   EntityContainer("tests/fixtures/tickets_fixture.json"),
                   EntityContainer("tests/fixtures/users_fixture.json"),
                   None, None, None)


def test_user_can_be_found_by_id(sample_matcher):
    sample_matcher.searching_on = "users"
    sample_matcher.match_field = "_id"
    sample_matcher.match_value = "13"
    result = sample_matcher.get_entity_data_by_field_value()
    assert len(result) == 1


def test_empty_values_can_be_found(sample_matcher):
    sample_matcher.searching_on = "users"
    sample_matcher.match_field = "email"
    sample_matcher.match_value = ""
    result = sample_matcher.get_entity_data_by_field_value()
    assert len(result) == 1 and result[0]["name"] == "Shelly Clements"


def test_boolean_values_can_be_found_case_insensitively(sample_matcher):
    sample_matcher.searching_on = "tickets"
    sample_matcher.match_field = "has_incidents"
    sample_matcher.match_value = "false"
    result_1 = sample_matcher.get_entity_data_by_field_value()
    sample_matcher.match_value = "False"
    result_2 = sample_matcher.get_entity_data_by_field_value()
    assert result_1 == result_2


def test_values_in_arrays_can_be_found_individually(sample_matcher):
    sample_matcher.searching_on = "organizations"
    sample_matcher.match_field = "domain_names"
    sample_matcher.match_value = "isoplex.com"
    result = sample_matcher.get_entity_data_by_field_value()
    assert len(result) == 1 and result[0]["name"] == "Terrasys"


def test_empty_list_will_be_returned_if_value_does_not_match(sample_matcher):
    sample_matcher.searching_on = "users"
    sample_matcher.match_field = "name"
    sample_matcher.match_value = "Roger Federer"
    result = sample_matcher.get_entity_data_by_field_value()
    assert result == []


def test_users_associated_organization_can_be_found(sample_matcher):
    sample_matcher.searching_on = "users"
    sample_matcher.match_field = "_id"
    sample_matcher.match_value = "11"
    result = sample_matcher.get_entity_data_by_field_value()
    associated_result = sample_matcher.get_associated_entity_data(result)
    assert associated_result[0].associated_org["name"] == "Bitrex"


def test_users_associated_tickets_can_be_found(sample_matcher):
    sample_matcher.searching_on = "users"
    sample_matcher.match_field = "_id"
    sample_matcher.match_value = "11"
    result = sample_matcher.get_entity_data_by_field_value()
    associated_result = sample_matcher.get_associated_entity_data(result)
    assert len(associated_result[0].submitted_tickets) == 2 and len(associated_result[0].assigned_tickets) == 0


def test_orgs_associated_users_can_be_found(sample_matcher):
    sample_matcher.searching_on = "organizations"
    sample_matcher.match_field = "_id"
    sample_matcher.match_value = "123"
    result = sample_matcher.get_entity_data_by_field_value()
    associated_result = sample_matcher.get_associated_entity_data(result)
    assert len(associated_result[0].associated_users) == 1 and \
           associated_result[0].associated_users[0]["name"] == "Wade Moore"


def test_orgs_associated_tickets_can_be_found(sample_matcher):
    sample_matcher.searching_on = "organizations"
    sample_matcher.match_field = "_id"
    sample_matcher.match_value = "123"
    result = sample_matcher.get_entity_data_by_field_value()
    associated_result = sample_matcher.get_associated_entity_data(result)
    assert len(associated_result[0].associated_tickets) == 2 and \
           associated_result[0].associated_tickets[0]["subject"] == "A Drama in Cayman Islands"


def test_tickets_associated_users_can_be_found(sample_matcher):
    sample_matcher.searching_on = "tickets"
    sample_matcher.match_field = "_id"
    sample_matcher.match_value = "f3cc4dc6-3517-474b-b212-b82fdaa0800d"
    result = sample_matcher.get_entity_data_by_field_value()
    associated_result = sample_matcher.get_associated_entity_data(result)
    assert associated_result[0].submitter["name"] == "Shelly Clements" and \
           associated_result[0].assignee["name"] == "Wade Moore"


def test_tickets_associated_orgs_can_be_found(sample_matcher):
    sample_matcher.searching_on = "tickets"
    sample_matcher.match_field = "_id"
    sample_matcher.match_value = "f3cc4dc6-3517-474b-b212-b82fdaa0800d"
    result = sample_matcher.get_entity_data_by_field_value()
    associated_result = sample_matcher.get_associated_entity_data(result)
    assert associated_result[0].associated_org["name"] == "Terrasys"

