from invoke import task

@task
def start(c):
    c.run("python src/tietotila/main.py")

@task
def test(c):
    c.run("pytest src")

@task(name="coverage-report")
def generate_coverage_report(c):
    c.run("coverage run --source=src -m pytest src")
    c.run("coverage html")

@task(name="pylint")
def generate_coverage_report(c):
    c.run("pylint src/tietotila")
    