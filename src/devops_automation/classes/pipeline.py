import logging
from collections.abc import Callable

logger = logging.getLogger(__name__)


class Pipeline:

    def __init__(self, name: str) -> None:
        self.name = name
        self.steps: list[Callable[[], None]] = []

    def add_step(self, step: Callable[[], None]) -> None:
        self.steps.append(step)

    def run(self) -> None:
        logger.info("Running pipeline: %s", self.name)

        for step in self.steps:
            try:
                step()
            except Exception:
                logger.exception("Pipeline failed")
                raise

        logger.info("Pipeline %s completed successfully", self.name)
