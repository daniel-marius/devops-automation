from ipaddress import IPv4Address

from devops_automation.classes.docker_manager import DockerManager
from devops_automation.classes.pipeline import Pipeline
from devops_automation.classes.server import Server


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