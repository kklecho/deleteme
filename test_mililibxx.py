import mililibxx


def test_main():
    msg = mililibxx.main("Alice")
    assert msg == "Hello alice"
