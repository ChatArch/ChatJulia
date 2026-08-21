# CLI 树

`ChatJulia` 当前是 root-only CLI。这个页面必须从真实 `chatjulia --tree` 输出同步，不能手写未来命令。公开树根使用规范命令名 `chatjulia`。

```text
chatjulia
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

ChatStyle 的默认 `--tree` 保留参数签名；`--tree-brief` 省略参数签名，同时保留命令节点和说明。当前 CLI 只有布尔根选项，没有带参数的子命令，因此两种输出暂时相同。

## 当前状态

| 入口 | 状态 | 说明 |
| --- | --- | --- |
| `chatjulia --help` | 已实现 | 显示根命令帮助。 |
| `chatjulia --version` | 已实现 | 显示已安装包版本。 |
| `chatjulia --tree` | 已实现 | 显示包含参数签名的当前真实 CLI 树。 |
| `chatjulia --tree-brief` | 已实现 | 显示省略参数签名、保留节点和说明的 CLI 树。 |
| Julia 工具子命令 | 尚未实现 | 未来有实际 Julia 编排能力后再加入 CLI。 |

## 更新规则

新增真实命令时，先更新 Click 注册面和测试，再运行 `chatjulia --tree` 和 `chatjulia --tree-brief` 回填 README 与本页。
