from copy import copy

import click
from click.testing import CliRunner

from chatjulia import __version__
from chatjulia.cli import main


def test_help_mentions_tree_option():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "--tree" in result.output
    assert "--tree-brief" in result.output


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatjulia, version {__version__}" in result.output


def test_tree_reports_registered_root_only_surface():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0
    assert result.output == (
        "chatjulia\n"
        "├── --help  # Show this message and exit.\n"
        "├── --version  # Show the version and exit.\n"
        "├── --tree  # Print the registered CLI tree and exit.\n"
        "└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.\n"
    )


def test_tree_brief_reports_registered_root_only_surface():
    result = CliRunner().invoke(main, ["--tree-brief"])

    assert result.exit_code == 0
    assert result.output == (
        "chatjulia\n"
        "├── --help  # Show this message and exit.\n"
        "├── --version  # Show the version and exit.\n"
        "├── --tree  # Print the registered CLI tree and exit.\n"
        "└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.\n"
    )


def test_tree_modes_include_or_omit_registered_command_signatures():
    @click.command(help="Inspect a Julia target.")
    @click.argument("target")
    @click.option("--format", "output_format", help="Select output format.")
    def inspect(target: str, output_format: str | None) -> None:
        pass

    test_cli = copy(main)
    test_cli.commands = dict(main.commands)
    test_cli.add_command(inspect)

    full = CliRunner().invoke(test_cli, ["--tree"])
    brief = CliRunner().invoke(test_cli, ["--tree-brief"])

    assert full.exit_code == 0
    assert brief.exit_code == 0
    assert "└── inspect <TARGET> [--format OUTPUT-FORMAT]  # Inspect a Julia target." in full.output
    assert "└── inspect  # Inspect a Julia target." in brief.output
    assert "<TARGET>" not in brief.output
    assert "[--format OUTPUT-FORMAT]" not in brief.output
