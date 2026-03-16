import time
import pytest

from pages.macrodroid_page import MacroDroidPage


@pytest.mark.smoke
@pytest.mark.regression
def test_macrodroid_stays_in_foreground(driver):
    """
    Smoke test:
    - abre o MacroDroid
    - espera ficar em foco
    - valida que continua em foco após pequenas esperas
    """
    app = MacroDroidPage(driver)

    app.open()
    app.wait_until_foreground()
    app.assert_in_foreground()

    time.sleep(1)
    app.assert_in_foreground()

    time.sleep(1)
    app.assert_in_foreground()


@pytest.mark.smoke
@pytest.mark.regression
def test_log_current_state_for_debug(driver):
    """
    Smoke test:
    - abre o MacroDroid
    - registra estado atual (package/activity) no log
    - valida activity esperada
    """
    app = MacroDroidPage(driver)

    app.open()
    app.wait_until_foreground()

    app.log_app_state()
    app.assert_not_launcher()
    app.assert_expected_activity()
