from src.main import setting_goals, welcome_message


def test_welcome_message():
    assert welcome_message("Ammy") == "Ammy, welcome to the Data Engineering course."


def test_setting_goals():
    assert setting_goals("200") == "Let's try together to earn 200 points!"
