# Changelog

## 2026-08-21 - 0.1.2

### Changed

- Migrated the top-level Click CLI from its local tree formatter to ChatStyle's shared `add_tree_option()` runtime.
- Added canonical `chatjulia` full and brief tree readbacks: `--tree` retains parameter signatures and `--tree-brief` omits them while preserving command nodes and descriptions.
- Updated runtime bounds to `chatstyle>=0.2.0,<0.3.0` and `chatenv>=0.2.10,<0.3.0`.
- Added package and CI smoke coverage for the version and both tree modes.

## 2026-08-12 - 0.1.1

### Added

- Added real root-only `chatjulia --tree` generated from the Click command surface.
- Added CLI contract tests for `--help`, `--version`, and `--tree`.

### Changed

- Aligned documentation URLs to `https://arch.gh.wzhecnu.cn/ChatJulia/`.
- Enabled bilingual MkDocs navigation and Material icon rendering.
- Hardened Preview Docs and tag-only OIDC publish workflows.

## 2026-07-01 - 0.1.0

### Added

- Initial ChatJulia package scaffold with `chatjulia` CLI.
- ChatEnv provider entry point for `chatjulia` configuration discovery.
- CI and tag-driven Trusted Publisher workflow scaffold.
