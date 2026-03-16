import pytest

from pages.macrodroid_page import MacroDroidPage


@pytest.mark.navigation
@pytest.mark.regression
def test_logs_navigation_with_dark_mode_cleanup(driver):
    """
    Fluxo funcional completo:
    - abre o app
    - ativa dark mode
    - abre System Log
    - volta
    - abre User Log com scroll robusto
    - volta
    - desativa dark mode
    - volta para Home
    """
    app = MacroDroidPage(driver)

    app.open()
    app.wait_until_foreground()

    # Ativa dark mode
    app.go_to_settings()
    app.open_dark_mode()
    app.set_dark_mode("On")
    app.go_to_home()

    # Navega para System Log e volta
    app.open_system_log()
    app.navigate_up()

    # Abre User Log e volta
    app.open_user_log()
    app.tap_back_button()

    # Cleanup: desativa dark mode
    app.go_to_settings()
    app.open_dark_mode()
    app.set_dark_mode("Off")
    app.go_to_home()

    # Validação final mínima
    app.assert_in_foreground()
    app.assert_not_launcher()