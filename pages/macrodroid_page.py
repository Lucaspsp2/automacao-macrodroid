from __future__ import annotations

import time

from pages.base_page import BasePage


class MacroDroidPage(BasePage):
    APP_PACKAGE = "com.arlosoft.macrodroid"

    def open(self) -> None:
        """
        Traz o MacroDroid para o primeiro plano.
        """
        self.log.info("Ativando o MacroDroid (activate_app)...")
        self.driver.activate_app(self.APP_PACKAGE)

    def wait_until_foreground(self, timeout: float = 20.0, interval: float = 0.5) -> None:
        """
        Espera até o MacroDroid estar em primeiro plano, validando pelo package.
        """
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

    def assert_in_foreground(self) -> None:
        """
        Assert direto para garantir que estamos no MacroDroid.
        """
        pkg = self.driver.current_package
        self.log.info("Verificando foreground. current_package=%r", pkg)
        assert pkg == self.APP_PACKAGE, f"App não está em foco. package atual: {pkg!r}"

    def log_app_state(self) -> None:
        """
        Loga estado atual para debugging.
        """
        self.log.info("Estado do app: package=%r activity=%r", self.driver.current_package, self.driver.current_activity)

    def assert_not_launcher(self) -> None:
        act = self.driver.current_activity
        self.log.info("Activity atual: %r", act)
        assert "NexusLauncherActivity" not in act, f"Ainda no launcher: {act!r}"

    def assert_expected_activity(self) -> None:
        """
        Aceita as activities iniciais mais comuns do MacroDroid.
        """
        act = self.driver.current_activity
        allowed = ("IntroActivity", "NewHomeScreenActivity")
        self.log.info("Validando activity. atual=%r allowed=%s", act, allowed)
        assert any(a in act for a in allowed), f"Activity inesperada no MacroDroid: {act!r}"
