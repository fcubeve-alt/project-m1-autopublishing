# Money OS v0.1 — 设计文档（历史）

`00`–`04` 是设计阶段产物，保留作为决策记录。

**实现已在 `staging/money-os-core/`**，且相对本设计有两处经修正的偏离：

1. **传输不再固定为 Git。** `01_ARCHITECTURE` 曾把 git 定为传输层；
   现改为 **local-first outbox + 可插拔 transport**，Git 只是可选项之一。
   权威文本是 `staging/money-os-core/CONTRACT.md` §1–2。
2. **`human_minutes` 由必填降为建议。** 由 Monetools 兼容性分析改出，
   见 `staging/money-os-core/docs/COMPATIBILITY_MONETOOLS.md` §4。

**冲突时以 `staging/money-os-core/CONTRACT.md` 为准。**
