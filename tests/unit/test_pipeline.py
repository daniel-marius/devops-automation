from devops_automation.classes.pipeline import Pipeline


def test_pipeline_execution() -> None:

    pipeline = Pipeline("Test Pipeline")

    executed = []

    pipeline.add_step(
        lambda: executed.append("build")
    )

    pipeline.add_step(
        lambda: executed.append("test")
    )

    pipeline.run()

    assert executed == ["build", "test"]
