"""CLI entrypoint for chatjulia."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatjulia import __version__


@click.group(name="chatjulia", invoke_without_command=True)
@click.version_option(__version__, prog_name="chatjulia")
@add_tree_option(renderer_options={"root_name": "chatjulia"})
@click.pass_context
def main(ctx: click.Context) -> None:
    """chatjulia command line interface."""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


if __name__ == "__main__":
    main()
