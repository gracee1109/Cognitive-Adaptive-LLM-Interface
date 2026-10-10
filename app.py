import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Cognitive-Aware LLM Engine")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class TelemetryEvent(BaseModel):
  element_id: str
  dwell_time_ms: float
  regression_count: int
  selected_text: str = ""


@app.post("/api/telemetry")
async def process_telemetry(event: TelemetryEvent):
  state = "FLUENT"
  if event.dwell_time_ms > 3000 or event.regression_count >= 2:
    state = "LOCAL_IMPEDED"
  if event.dwell_time_ms > 8000:
    state = "GLOBAL_OVERLOAD" 

  intervention = {"state": state, "action": "NONE", "content": ""}
  if state == "LOCAL_IMPEDED":
    intervention["action"] = "MICRO_TOOLTIP"
    intervention["content"] = (
        "【工作記憶（Working Memory）過載】：指人腦在短時間內能暫存與處理的資訊容量有限（約"
        " 4±1 個組塊）。系統建議：降低單次輸出長度，以漸進式重點條列呈現。"
    )
  elif state == "GLOBAL_OVERLOAD":
    intervention["action"] = "STRUCTURAL_REBUILD"
    intervention["content"] = "偵測到認知超載，建議切換為樹狀摘要視圖。"

  return intervention
