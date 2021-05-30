import pytest
import json
from src.entity_container import EntityContainer


@pytest.fixture()
def sample_container():
    return EntityContainer("tests/fixtures/users_fixture.json")


def test_json_file_is_loaded(sample_container):
    assert type(sample_container.data) is list and len(sample_container.data) == 3 \
           and type(sample_container.data[0]) is dict


def test_all_fields_are_loaded(sample_container):
    assert len(sample_container.all_fields) == 19


def test_file_path_invalid_handling(capsys):
    with pytest.raises(FileNotFoundError):
        container_with_broken_path = EntityContainer("path/to/nowhere")
    captured = capsys.readouterr()
    expected_out = "Unable to find the data file provided at path/to/nowhere\n" \
                   "Please try again with another file location.\n"
    assert captured.out == expected_out


def test_invalid_json_file_handling(capsys):
    with pytest.raises(json.decoder.JSONDecodeError):
        container_with_invalid_json = EntityContainer("tests/fixtures/not_json.file")
    captured = capsys.readouterr()
    expected_out = "The json file provided at tests/fixtures/not_json.file is invalid.\n"\
                   "Please try again with a well-formed json file.\n"
    assert captured.out == expected_out