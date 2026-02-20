import time

from appium import webdriver
from appium.options.android import UiAutomator2Options


def wait_until(predicate, timeout=20, interval=0.5, on_timeout_msg="Timeout"):
    end = time.time() + timeout
    last = None
    while time.time() < end:
        last = predicate()
        if last:
            return True
        time.sleep(interval)
    raise AssertionError(f"{on_timeout_msg}. Último estado: {last!r}")


def test_open_macrodroid_hello_world():
    APP_PACKAGE = "com.arlosoft.macrodroid"

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.no_reset = True
    options.auto_grant_permissions = True
    options.app_package = APP_PACKAGE
    options.app_activity = "com.arlosoft.macrodroid/.intro.IntroActivity"

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    try:
        driver.activate_app(APP_PACKAGE)

        wait_until(
            lambda: driver.current_package == APP_PACKAGE,
            timeout=20,
            interval=0.5,
            on_timeout_msg=f"MacroDroid não ficou em foco. package atual: {driver.current_package!r}",
        )

        current_activity = driver.current_activity
        assert "NexusLauncherActivity" not in current_activity, f"Ainda no launcher: {current_activity!r}"

        allowed = ("IntroActivity", "NewHomeScreenActivity")
        assert any(a in current_activity for a in allowed), f"Activity inesperada no MacroDroid: {current_activity!r}"

    finally:
        # Fecha o app explicitamente (mata o processo)
        driver.terminate_app(APP_PACKAGE)

        # Encerra a sessão Appium
        driver.quit()
