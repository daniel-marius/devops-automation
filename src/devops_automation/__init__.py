from ipaddress import IPv4Address

from devops_automation.server import Server
from devops_automation.docker_manager import DockerManager
from devops_automation.pipeline import Pipeline


def main():
    server: Server = Server(
        name="web-server",
        ip=IPv4Address("192.168.1.10")
    )

    docker_manager: DockerManager = DockerManager(image="my-app:latest")

    pipeline: Pipeline = Pipeline(name="Production CI/CD Pipeline")

    pipeline.add_step(server.connect)
    pipeline.add_step(docker_manager.build)
    pipeline.add_step(docker_manager.run)
    pipeline.add_step(server.deploy)

    pipeline.run()

if __name__ == "__main__":
    main()