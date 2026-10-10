# Cognitive-Aware Adaptive LLM Collaboration Interface

本專案為碩士推甄研究計畫《基於多模態操作串流探勘之認知感知 LLM 動態協作架構》之概念驗證原型 
## 系統核心架構
- **微觀互動遙測層**：即時監聽 DOM 閱讀停頓與操作軌跡。
- **認知狀態機判定**：分級識別使用者認知流暢度（流暢吸收 / 局部受阻 / 全域過載）。
- **非同步自適應渲染**：動態觸發 LLM 核心概念微干預，平順化解心智負荷。

## 系統架構圖
## 快速啟動
\`\`\`bash
# 本地啟動後端
python3 -m uvicorn app:app --reload

# 開啟前端
open index.html
\`\`\`
