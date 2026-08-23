# Money OS Shared Core v0.1 — 仓库边界

---

## 1. 建议的新仓库

| 项 | 值 |
|---|---|
| **名称** | `money-os-core`（建议；最终由 Owner 定） |
| **可见性** | **建议 private** —— 内含组合级财务结构与项目注册表 |
| **归属** | `fcubeve-alt`（与现有项目同账号） |
| **依赖** | Python 3.11+ 标准库；schema 校验可选 `jsonschema`。**不引入框架** |

⚠️ **建库是不可逆的外部动作，属 Approval Gate。** 我不会自行创建。
名称与可见性确认后再执行。

## 2. 目录结构

```
money-os-core/
├── README.md
├── CONTRACT.md                  ← 契约规范（权威文本）
├── schemas/                     ← JSON Schema，契约的机器可读形式
│   ├── project.schema.json
│   ├── work_item.schema.json
│   ├── approval.schema.json
│   ├── ledger_entry.schema.json
│   ├── decision.schema.json
│   └── event.schema.json
├── projects/
│   └── registry.yaml            ← 唯一权威项目列表
├── moneyos/                     ← Python 包
│   ├── contract.py              ← 六个对象的读写与校验
│   ├── aggregate.py             ← 跨项目只读聚合
│   ├── supervisor.py            ← 组合状态 + 阻塞 + 建议
│   └── cli.py                   ← moneyos validate / status / report
├── tests/
│   └── fixtures/m1/             ← 用 M1 真实数据做回归夹具
└── docs/
    └── INTEGRATION_GUIDE.md     ← 给 Tax / Pearl 的接入指南
```

## 3. 边界：什么进，什么不进

| 进 `money-os-core` | 留在项目仓库 |
|---|---|
| 六个契约对象的 schema | 全部业务逻辑 |
| 校验器 | 平台 Adapter（Adobe/Freepik/Vecteezy/CF…） |
| 跨项目只读聚合 | 内容生产（图像、文章） |
| Supervisor 报告 | 平台政策研究、Evidence Store |
| 项目注册表 | 项目自己的 `.moneyos/` 输出与那层薄适配 |
| 给客户的接入指南 | 一切只对单一项目有意义的东西 |

## 4. M1 侧的改动 —— 刻意做到最小

M1 **不重构**。新增一个目录，其余不动：

```
project-m1-autopublishing/
├── ledger/                  ← 原样保留，仍是 M1 的工作账本
├── evidence/                ← 原样保留，不上交 Money OS
├── .moneyos/                ← 新增：契约面输出
│   ├── project.json
│   ├── ledger.ndjson
│   ├── work_items.ndjson
│   ├── approvals.ndjson
│   ├── decisions.ndjson
│   └── events.ndjson
└── tools/moneyos_export.py  ← 新增：约 100 行，从现有 CSV 生成上面的文件
```

**`ledger/*.csv` 仍是真相源，`.moneyos/` 是导出物。** 这样：
- M1 现有工作流零改动
- 导出可随时重跑
- 删掉 `.moneyos/` 与 `tools/moneyos_export.py`，M1 完全回到今天的状态

## 5. 为什么不把 Money OS 做成 M1 的子目录

因为**它会立刻被 M1 的需求污染**。共享核心的价值全在"第二个客户能不改自己就接上"，
而共享核心一旦住在第一个客户家里，第一个客户的假设会不断渗进契约，
等第二个客户来时才发现契约里全是 M1 的形状。

**独立仓库是这条边界唯一可强制执行的形式。**

## 6. 依赖方向（单向，不可逆转）

```
money-os-core   ──不依赖──▶  任何项目
项目            ──可选依赖──▶  money-os-core（仅为方便；手写文件同样合规）
```

**Money OS 永远不 import 任何项目的代码。** 若哪天需要，说明边界已经破了。
