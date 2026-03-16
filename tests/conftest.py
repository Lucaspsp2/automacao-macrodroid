import os
import sys
from datetime import datetime
from pathlib import Path

import pytest
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options


# Garante que a raiz do projeto esteja no sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


# Defaults (podem ser sobrescritos por variáveis de ambiente)
APP_PACKAGE = os.getenv("APP_PACKAGE", "com.arlosoft.macrodroid")
APP_ACTIVITY = os.getenv("APP_ACTIVITY", "com.arlosoft.macrodroid/.intro.IntroActivity")
APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
DEVICE_NAME = os.getenv("DEVICE_NAME", "emulator-5554")


@pytest.fixture
def driver():
    """
    Fixture do Pytest responsável por criar e encerrar a sessão Appium.
    """

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = DEVICE_NAME

    options.no_reset = True
    options.auto_grant_permissions = True

    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY

    drv = webdriver.Remote(APPIUM_SERVER_URL, options=options)

    try:
        yield drv
    finally:
        try:
            drv.terminate_app(APP_PACKAGE)
        except Exception:
            pass

        try:
            drv.quit()
        except Exception:
            pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook do Pytest que tira screenshot automaticamente quando um teste falha
    e anexa a imagem ao relatório do Allure.
    """

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            filename = f"{screenshots_dir}/failure_{item.name}_{timestamp}.png"

            driver.save_screenshot(filename)

            with open(filename, "rb") as f:
                allure.attach(
                    f.read(),
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            print(f"\nScreenshot salva em: {filename}")