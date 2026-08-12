# CLI Tree

`ChatJulia` is currently a root-only CLI. This page must stay synchronized from the real `chatjulia --tree` output and must not invent future commands.

```text
chatjulia  # ChatArch Julia tooling entrypoint
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## Current Status

| Entry | Status | Notes |
| --- | --- | --- |
| `chatjulia --help` | Implemented | Shows root command help. |
| `chatjulia --version` | Implemented | Shows the installed package version. |
| `chatjulia --tree` | Implemented | Shows the current real CLI tree. |
| Julia tooling subcommands | Not implemented | Add them only after real Julia orchestration capability exists. |

## Update Rule

When real commands are added, update the Click registration and tests first, then run `chatjulia --tree` to refresh README and this page.
