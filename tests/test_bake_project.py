import os
import pathlib
import shlex
import subprocess

from cookiecutter.main import cookiecutter

TEMPLATE_DIRECTORY = str(pathlib.Path(__file__).parent.parent)


def generate(directory, context):
    cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=str(directory),
        no_input=True,
        extra_context=context,
    )


def paths(directory):
    paths = list(pathlib.Path(directory).glob("**/*"))
    paths = [r.relative_to(directory) for r in paths]
    return {str(f) for f in paths if str(f) != "."}


def test_bake_static_and_templates(tmpdir):
    generate(
        tmpdir,
        {
            "project_name": "foo",
            "project_short_description": "blah",
        },
    )
    assert paths(tmpdir) == {
        "foo",
        "foo/src",
        "foo/src/foo",
        "foo/src/foo/foo.py",
        "foo/src/foo/cli.py",
        "foo/src/foo/__init__.py",
        "foo/src/foo/foo.py",
        "foo/pyproject.toml",
        "foo/README.rst",
    }


def test_bake_install_and_run(tmpdir):
    generate(
        tmpdir,
        {
            "project_name": "foo",
            "project_short_description": "blah",
        },
    )
    os.chdir(tmpdir / "foo")
    subprocess.check_call(shlex.split('poetry install'))
    result = subprocess.run(shlex.split('foo -v'), capture_output=True, check=True)
    assert result.stdout == b"Hello world\nInvoked with Namespace(log_level='INFO')\n"
