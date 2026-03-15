from pages.macrodroid_page import MacroDroidPage


def test_enable_dark_mode(driver):
    """
    Fluxo funcional:
    - abre o MacroDroid
    - navega para Settings
    - ativa Dark Mode
    - valida app em foreground
    - restaura estado (desativa Dark Mode)
    """
    app = MacroDroidPage(driver)

    app.open()
    app.wait_until_foreground()

    # ativa dark mode
    app.go_to_settings()
    app.open_dark_mode()
    app.set_dark_mode("On")
    app.go_to_home()

    # validação mínima
    app.assert_in_foreground()
    app.assert_not_launcher()

    # cleanup
    app.go_to_settings()
    app.open_dark_mode()
    app.set_dark_mode("Off")
    app.go_to_home()