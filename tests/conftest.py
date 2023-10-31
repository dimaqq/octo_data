import pytest


@pytest.fixture(scope="session")
def sample_data(pytestconfig):
    return (pytestconfig.rootpath / "data/sample.txt").read_text()


@pytest.fixture
def sample(sample_data):
    def sampler(start: str):
        for line in sample_data.splitlines():
            if line.startswith(start):
                return line

    return sampler
