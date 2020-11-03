def test_one(tmp_path):
    directory = tmp_path / "sub"
    directory.mkdir()
    test_file = directory/"example.txt"
    test_file.write_text("hello")

    assert test_file.read_text() == "hello"
