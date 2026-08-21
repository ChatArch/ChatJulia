# CLI Tree

`ChatJulia` is currently a root-only CLI. This page must stay synchronized from the real `chatjulia --tree` output and must not invent future commands. The public tree root uses the canonical command name `chatjulia`.

```text
chatjulia
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

ChatStyle's default `--tree` retains parameter signatures; `--tree-brief` omits signatures while retaining command nodes and descriptions. Because the current CLI has only boolean root options and no parameterized subcommands, their output is presently identical.

## Current Status

| Entry | Status | Notes |
| --- | --- | --- |
| `chatjulia --help` | Implemented | Shows root command help. |
| `chatjulia --version` | Implemented | Shows the installed package version. |
| `chatjulia --tree` | Implemented | Shows the current real CLI tree with parameter signatures. |
| `chatjulia --tree-brief` | Implemented | Shows the tree without signatures while retaining nodes and descriptions. |
| Julia tooling subcommands | Not implemented | Add them only after real Julia orchestration capability exists. |

## Update Rule

When real commands are added, update the Click registration and tests first, then run `chatjulia --tree` and `chatjulia --tree-brief` to refresh README and this page.
