from loguru import logger

logger.add(
    'ai.log',
    rotation="10 MB",
    retention="1 day",
    level="INFO",
    encoding="utf-8",
    colorize=True,
    backtrace=True
)