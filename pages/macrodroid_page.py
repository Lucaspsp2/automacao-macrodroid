from __future__ import annotations

import time

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class MacroDroidPage(BasePage):
    APP_PACKAGE = "com.arlosoft.macrodroid"

    # Navegação inferior
    NAV_SETTINGS = (AppiumBy.ID, "com.arlosoft.macrodroid:id/navigation_settings")
    NAV_HOME = (AppiumBy.ID, "com.arlosoft.macrodroid:id/navigation_home")

    # Navegação superior
    NAVIGATE_UP = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    BACK_BUTTON = (AppiumBy.ID, "com.arlosoft.macrodroid:id/backButton")

    # Configuração Dark Mode
    DARK_MODE_OPTION = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.RelativeLayout").instance(4)',
    )
    DARK_MODE_ON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("On")',
    )
    DARK_MODE_OFF = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Off")',
    )

    # Logs / itens da Home
    SYSTEM_LOG_OPTION = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.arlosoft.macrodroid:id/clickContainer").instance(8)',
    )

    # Melhor abordagem para User Log: scroll até o texto
    USER_LOG_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("User Log")',
    )
    USER_LOG_SCROLL_INTO_VIEW = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("User Log"))',
    )

    def open(self) -> None:
        self.log.info("Ativando o MacroDroid (activate_app)...")
        self.driver.activate_app(self.APP_PACKAGE)

    def wait_until_foreground(self, timeout: float = 20.0, interval: float = 0.5) -> None:
        self.log.info("Aguardando MacroDroid ficar em foco (current_package)...")
        end = time.time() + timeout
        while time.time() < end:
            pkg = self.driver.current_package
            if pkg == self.APP_PACKAGE:
                self.log.info("MacroDroid em foco. package=%s", pkg)
                return
            time.sleep(interval)

        act = self.driver.current_activity
        raise AssertionError(
            f"MacroDroid não ficou em foco em {timeout}s. package={self.driver.current_package!r}, activity={act!r}"
        )

    def _wait_for_element(self, locator: tuple[str, str], timeout: float = 8.0, interval: float = 0.5):
        end = time.time() + timeout
        last_error = None

        while time.time() < end:
            try:
                element = self.driver.find_element(*locator)
                return element
            except Exception as exc:
                last_error = exc
                time.sleep(interval)

        raise AssertionError(f"Elemento não encontrado após {timeout}s. locator={locator!r}. erro={last_error!r}")

    def assert_in_foreground(self) -> None:
        pkg = self.driver.current_package
        self.log.info("Verificando foreground. current_package=%r", pkg)
        assert pkg == self.APP_PACKAGE, f"App não está em foco. package atual: {pkg!r}"

    def log_app_state(self) -> None:
        self.log.info(
            "Estado do app: package=%r activity=%r",
            self.driver.current_package,
            self.driver.current_activity,
        )

    def assert_not_launcher(self) -> None:
        act = self.driver.current_activity
        self.log.info("Activity atual: %r", act)
        assert "NexusLauncherActivity" not in act, f"Ainda no launcher: {act!r}"

    def assert_expected_activity(self) -> None:
        act = self.driver.current_activity
        allowed = ("IntroActivity", "NewHomeScreenActivity")
        self.log.info("Validando activity. atual=%r allowed=%s", act, allowed)
        assert any(a in act for a in allowed), f"Activity inesperada no MacroDroid: {act!r}"

    def go_to_settings(self) -> None:
        self.log.info("Clicando na aba Settings...")
        self._wait_for_element(self.NAV_SETTINGS).click()

    def go_to_home(self) -> None:
        self.log.info("Clicando na aba Home...")
        self._wait_for_element(self.NAV_HOME).click()

    def open_dark_mode(self) -> None:
        self.log.info("Abrindo a configuração de Dark Mode...")
        self._wait_for_element(self.DARK_MODE_OPTION).click()

    def set_dark_mode(self, state: str) -> None:
        normalized = state.strip().capitalize()
        self.log.info("Definindo Dark Mode para %r...", normalized)

        if normalized == "On":
            self._wait_for_element(self.DARK_MODE_ON).click()
            return

        if normalized == "Off":
            self._wait_for_element(self.DARK_MODE_OFF).click()
            return

        raise ValueError(f"Valor inválido para Dark Mode: {state!r}. Use 'On' ou 'Off'.")

    def open_system_log(self) -> None:
        self.log.info("Abrindo System Log...")
        self._wait_for_element(self.SYSTEM_LOG_OPTION).click()

    def scroll_to_user_log(self) -> None:
        self.log.info("Rolando até o User Log...")
        self._wait_for_element(self.USER_LOG_SCROLL_INTO_VIEW, timeout=10)

    def open_user_log(self) -> None:
        self.log.info("Abrindo User Log...")
        self.scroll_to_user_log()
        self._wait_for_element(self.USER_LOG_TEXT).click()

    def navigate_up(self) -> None:
        self.log.info("Clicando em Navigate up...")
        self._wait_for_element(self.NAVIGATE_UP).click()

    def tap_back_button(self) -> None:
        self.log.info("Clicando no backButton...")
        self._wait_for_element(self.BACK_BUTTON).click()