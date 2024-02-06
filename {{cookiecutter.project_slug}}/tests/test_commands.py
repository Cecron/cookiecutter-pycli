import shlex

import {{ cookiecutter.project_slug }}.cli
import {{ cookiecutter.project_slug }}.commands


def test_hello():
    args = {{ cookiecutter.project_slug }}.cli.parse_args(shlex.split("hello --name there"))
    assert isinstance(args.action, {{ cookiecutter.project_slug }}.commands.Hello)
    assert args.name == "there"
