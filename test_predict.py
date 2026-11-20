def test_exact_threshold():
    assert predict({"cat": 0.5, "dog": 0.2}) == "cat"
