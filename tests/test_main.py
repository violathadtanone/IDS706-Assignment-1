from src.main import setting_goals, welcome_message


def test_welcome_message():
    assert welcome_message("John") == "John, welcome to the Data Engineering course. Hope you have fun!"


def test_setting_goals():
    assert setting_goals("200") == "Let's try together to earn 200 points!"
