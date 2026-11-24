import logging

logger = logging.getLogger(__name__)


class DockerManager:

    def __init__(self, image: str) -> None:
        self.image = image

    def build(self) -> None:
        logger.info("Building Docker image: %s", self.image)

    def run(self) -> None:
        logger.info("Running container: %s", self.image)

    def stop(self) -> None:
        logger.info("Stopping container: %s", self.image)
