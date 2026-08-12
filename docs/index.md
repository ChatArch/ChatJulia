# ChatJulia 文档

ChatJulia 是 ChatArch 的 Julia tooling 包入口。当前文档记录已实现 CLI 和后续扩展边界。

<div class="grid cards" markdown>

-   :material-console-line: **CLI 树**

    ---

    查看当前真实命令入口、root-only 边界和更新规则。

    [查看 CLI 树](cli-tree.md)

-   :material-tools: **Julia 工具边界**

    ---

    当前包保持可安装、可测试、可发布的 Julia 工具壳；真实编排命令尚未暴露。

</div>

## 本地预览

```bash
pip install -e ".[docs]"
mkdocs serve
```
