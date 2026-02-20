from __future__ import annotations

from appium.webdriver.webdriver import WebDriver

from core.logger import get_logger


class BasePage:
    """
    Classe base do Page Object Model (POM).
    Todas as páginas devem herdar dela.

    Responsabilidades:
    - Guardar o driver
    - Expor operações comuns de forma reutilizável
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.log = get_logger(self.__class__.__name__)

    def current_package(self) -> str:
        return self.driver.current_package

    def current_activity(self) -> str:
        return self.driver.current_activity
