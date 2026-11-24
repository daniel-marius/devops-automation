import logging
from ipaddress import IPv4Address

logger = logging.getLogger(__name__)


class Server:
    def __init__(self, name: str, ip: IPv4Address) -> None:
        self.name = name
        self.ip = ip

    def connect(self) -> None:
        logger.info("Connecting to %s - %s", self.name, self.ip)

    def deploy(self) -> None:
        logger.info("Deploying application to %s", self.name)
