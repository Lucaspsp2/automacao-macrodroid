from pages.macrodroid_page import MacroDroidPage


def test_open_macrodroid_hello_world(driver):
    """
    Teste MVP usando Page Object Model.
    """

    macrodroid = MacroDroidPage(driver)

    macrodroid.open()
    macrodroid.wait_until_foreground()

    macrodroid.assert_not_launcher()
    macrodroid.assert_expected_activity()
