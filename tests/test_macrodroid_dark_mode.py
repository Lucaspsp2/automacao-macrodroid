import pytest
import allure

from pages.macrodroid_page import MacroDroidPage


@allure.title("Enable Dark Mode and restore original state")
@allure.feature("Settings")
@allure.story("Dark Mode configuration")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.settings
@pytest.mark.regression
def test_enable_dark_mode(driver):
    """
    Fluxo:
    - abre o app
    - ativa dark mode
    - valida retorno à home
    - restaura estado
    """
    app = MacroDroidPage(driver)

    with allure.step("Open MacroDroid"):
        app.open()
        app.wait_until_foreground()

    with allure.step("Navigate to Settings"):
        app.go_to_settings()

    with allure.step("Open Dark Mode configuration"):
        app.open_dark_mode()

    with allure.step("Enable Dark Mode"):
        app.set_dark_mode("On")

    with allure.step("Return to Home"):
        app.go_to_home()

    with allure.step("Validate application still in foreground"):
        app.assert_in_foreground()

    with allure.step("Restore original state (disable Dark Mode)"):
        app.go_to_settings()
        app.open_dark_mode()
        app.set_dark_mode("Off")
        app.go_to_home()
