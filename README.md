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

[英文版](README.en.md) | [简体中文](README.md)
</div>

# ChatJulia

ChatJulia 是 ChatArch 的 Julia tooling 包入口。当前包保持最小 root-only CLI，用于保留可安装、可发现、可发布的 Julia 工具壳；真实 Julia 编排命令尚未暴露。

## 快速开始

```bash
pip install ChatJulia
chatjulia --help
chatjulia --version
chatjulia --tree
chatjulia --tree-brief
```

## 当前 CLI 树

```text
chatjulia
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## CLI 边界

- 当前 CLI 只有根选项，没有业务子命令。
- `--tree` 和 `--tree-brief` 由 ChatStyle 从实际 Click 命令注册面生成，公开树根固定为规范命令名 `chatjulia`。
- `--tree` 默认保留参数签名；`--tree-brief` 省略参数签名，但保留命令节点和说明。当前只有布尔根选项，没有带参数的子命令，所以两种输出暂时相同。
- 后续新增真实 Julia 环境、包、脚本或执行编排命令时，必须先更新 Click 注册面，再用真实 `chatjulia --tree` 和 `chatjulia --tree-brief` 同步文档。

## 目录结构

- `src/`：包源码
- `tests/code-tests/`：代码测试和历史测试迁移
- `tests/cli-tests/`：真实 CLI 测试，doc-first
- `tests/mock-cli-tests/`：mock/fake CLI 测试，doc-first
- `docs/`：长期维护文档，由 MkDocs 构建

## 开发说明

扩展脚手架前，先阅读 `DEVELOP.md` 和 `AGENTS.md`。
