from click.testing import CliRunner

from chatjulia import __version__
from chatjulia.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatjulia, version {__version__}" in result.output
