from sentiment import analyze


def test_positive():
    assert analyze("This is great and I love it")["label"] == "positive"


def test_negative():
    assert analyze("Terrible, slow and broken")["label"] == "negative"


def test_negation_flips():
    assert analyze("not good")["label"] == "negative"
