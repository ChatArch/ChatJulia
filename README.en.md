<div align="center">
    <a href="https://pypi.python.org/pypi/ChatJulia">
        <img src="https://img.shields.io/pypi/v/ChatJulia.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatJulia/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatJulia/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
    <a href="https://arch.gh.wzhecnu.cn/ChatJulia/">
        <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
    </a>
</div>

<div align="center">

[English](README.en.md) | [简体中文](README.md)
</div>

# ChatJulia

ChatJulia is the ChatArch Julia tooling package entrypoint. The package currently keeps a minimal root-only CLI so the Julia tooling shell remains installable, discoverable, and releasable; real Julia orchestration commands are not exposed yet.

## Quick Start

```bash
pip install ChatJulia
chatjulia --help
chatjulia --version
chatjulia --tree
```

## Current CLI Tree

```text
chatjulia  # ChatArch Julia tooling entrypoint
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## CLI Boundary

- The current CLI only exposes root options and has no business subcommands.
- `--tree` is generated from the real Click command registration and is used to align README, docs, and tests.
- When real Julia environment, package, script, or execution orchestration commands are added later, update the Click registration first and then sync docs from the real `chatjulia --tree` output.

## Layout

- `src/`: package source code
- `tests/code-tests/`: code tests and migrated historical tests
- `tests/cli-tests/`: real CLI tests, doc-first
- `tests/mock-cli-tests/`: mock/fake CLI tests, doc-first
- `docs/`: long-lived project docs built by MkDocs

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.
