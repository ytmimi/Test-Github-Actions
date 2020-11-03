import pytest


def test_one(tmp_path):
    directory = tmp_path / "sub"
    directory.mkdir()
    test_file = directory / "example.txt"
    print(test_file)
    test_file.write_text("hello")
    assert test_file.read_text() == "hello"


def test_two(tmp_path):
    directory = tmp_path / "sub1" / "sub2"
    directory.mkdir(parents=True, exist_ok=True)
    test_file = directory / "example.txt"
    print(test_file)
    test_file.write_text("hello")
    assert test_file.read_text() == "hello"


@pytest.fixture
def my_temp_dir(tmp_path):
    directory = tmp_path / "sub1" / "sub2" / "sub3"
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def test_three(my_temp_dir):
    test_file = my_temp_dir / "example.txt"
    print(test_file)
    test_file.write_text("hello")
    assert test_file.read_text() == "hello"
