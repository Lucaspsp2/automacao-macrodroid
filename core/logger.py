import logging
import os


def get_logger(name: str = "automacao-macrodroid") -> logging.Logger:
    """
    Logger padrão do projeto.
    - Nível padrão: INFO
    - Pode ser sobrescrito com LOG_LEVEL=DEBUG (ou INFO, WARNING, etc.)
    """
    level_name = os.getenv("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)

    logger = logging.getLogger(name)

    # Evita duplicar handlers em re-runs do pytest
    if not logger.handlers:
        logger.setLevel(level)
        handler = logging.StreamHandler()
        fmt = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(fmt)
        logger.addHandler(handler)

    logger.setLevel(level)
    return logger
