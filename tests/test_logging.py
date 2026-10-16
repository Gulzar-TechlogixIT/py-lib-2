from gulzar_logging_utils import get_logger


def test_get_logger_name():
    assert get_logger("demo").name == "demo"
