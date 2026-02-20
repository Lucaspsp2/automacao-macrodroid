import os
import sys
import time
from pathlib import Path

# Garante que a raiz do projeto esteja no sys.path (para imports como "pages.*" e "core.*")
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

# Defaults (podem ser sobrescritos por variáveis de ambiente)
APP_PACKAGE = os.getenv("APP_PACKAGE", "com.arlosoft.macrodroid")
APP_ACTIVITY = os.getenv("APP_ACTIVITY", "com.arlosoft.macrodroid/.intro.IntroActivity")
APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
DEVICE_NAME = os.getenv("DEVICE_NAME", "emulator-5554")


@pytest.fixture
def driver():
    """
    Fixture do Pytest que:
    - cria a sessão Appium
    - entrega o driver para o teste
    - garante cleanup (fecha app + encerra sessão) no final
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
