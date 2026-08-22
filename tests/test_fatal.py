import logging
from typing import Optional, Union, get_type_hints

import onelog
import pytest


@pytest.fixture(autouse=True)
def reset_onelog_state():
    onelog._configured = False
    onelog._global_config = None
    logging.getLogger().handlers.clear()
    yield
    logging.getLogger().handlers.clear()


def test_package_exposes_version_and_logger():
    logger = onelog.get_logger(
        __name__,
        level=logging.DEBUG,
        show_summary=False,
        gen_log=False,
    )

    assert onelog.__version__ == "0.1.2"
    assert isinstance(logger, logging.Logger)


def test_get_logger_exposes_complete_public_types():
    assert get_type_hints(onelog.get_logger) == {
        "name": Optional[str],
        "level": Optional[Union[int, str]],
        "show_loc": Optional[bool],
        "show_time": Optional[bool],
        "show_summary": Optional[bool],
        "gen_log": Optional[bool],
        "log_file": Optional[str],
        "return": logging.Logger,
    }


def test_fatal_logs_and_exits_with_one():
    logger = onelog.get_logger(
        __name__,
        show_summary=False,
        gen_log=False,
    )

    with pytest.raises(SystemExit) as raised:
        logger.fatal("无法继续")

    assert raised.value.code == 1
