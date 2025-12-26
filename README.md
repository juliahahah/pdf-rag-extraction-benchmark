# Python PDF 提取與 OCR 工具評測報告 (2024/2025 版)

---

## 1. 執行摘要 (Executive Summary)

在 RAG 流程中，PDF 解析的品質直接決定了檢索的準確度（Garbage In, Garbage Out）。**準確率**與**結構還原度**（表格、標題層級）比單純的文字提取更重要。

*   **最強綜合表現 (推薦)**：**LlamaParse** (LlamaIndex 官方工具)。它專為 RAG 設計，能將 PDF 轉為 Markdown，完美保留表格結構，準確率目前最高。
*   **最佳本地端開源**：**Marker**。使用深度學習將 PDF 轉 Markdown，效果比傳統工具好，但需要 GPU 跑得才快。
*   **最快速度**：**PyMuPDF (fitz)**。適合處理海量簡單排版的 PDF。
*   **不推薦**：單純使用 `pypdf`。雖然它是許多教學的預設，但它對表格和複雜排版的處理能力較弱，容易導致 RAG 檢索失敗。

---

## 2. 工具深度分析 (Tool Analysis)

我們將工具分為三個梯隊，方便進行 Benchmark 比較：

### 第一梯隊：AI 增強與 RAG 專用 (準確率最高)
這類工具能輸出 **Markdown** 格式，這對 LLM 理解文件結構至關重要。

| 工具名稱 | 特點 | RAG 適用性 | 缺點 |
| :--- | :--- | :--- | :--- |
| **LlamaParse** | **首選**。LlamaIndex 推出的 API 服務，極強的表格與複雜排版理解能力。 | ⭐⭐⭐⭐⭐ <br> 直接輸出 Markdown，LLM 讀得懂表格數據。 | 需使用 API Key (有免費額度)，資料需上網。 |
| **Marker** | 將 PDF 轉為 Markdown 的深度學習模型 (比 Meta 的 Nougat 更快更準)。 | ⭐⭐⭐⭐⭐ <br> 適合本地端部署，數學公式與表格還原度高。 | 依賴 GPU 資源，純 CPU 跑很慢。 |

### 第二梯隊：規則式提取 (特定場景強)

| 工具名稱 | 特點 | RAG 適用性 | 缺點 |
| :--- | :--- | :--- | :--- |
| **PDFPlumber** | 專精於**表格提取** (Table Extraction)。 | ⭐⭐⭐⭐ <br> 如果你的 PDF 主要是財務報表，這很好用。 | 速度較慢。 |
| **Unstructured** | "瑞士刀"型的工具，整合了 OCR 與各種格式解析。 | ⭐⭐⭐⭐ <br> 功能強大但安裝環境較複雜。 | 依賴系統底層套件 (Tesseract 等)。 |

### 第三梯隊：基礎提取 (速度快但結構差)

| 工具名稱 | 特點 | RAG 適用性 | 缺點 |
| :--- | :--- | :--- | :--- |
| **PyMuPDF (fitz)** | **速度王者**。C 語言底層，極快。 | ⭐⭐⭐ <br> 適合初步清洗大量簡單文件。 | 對複雜排版（如雙欄文章）的順序容易錯亂。 |
| **pypdf** | 純 Python 庫，輕量。 | ⭐⭐ <br> 僅適合極簡單的純文字檔。 | 表格會變成亂碼，斷句混亂，干擾 Embedding。 |

---

## 3. 評測比較 (Benchmarks & Comparison)

根據 2024 年社群與技術文章的綜合評測結果：

### 1. 文字提取準確度 (Accuracy)
*   **複雜排版 (多欄位/表格)**: `LlamaParse` > `Marker` > `PDFPlumber` > `PyMuPDF` > `pypdf`
*   **掃描文件 (OCR)**: `PaddleOCR` > `Tesseract` (中文環境下)
*   **數學公式**: `Nougat` > `Marker` > 其他所有工具

### 2. 處理速度 (Speed)
*   **極快**: `PyMuPDF` (每頁毫秒級)
*   **中等**: `pypdf`, `Unstructured` (純文字模式)
*   **慢**: `PDFPlumber`, `LlamaParse` (受限於 API 延遲)
*   **極慢**: `Nougat`, `Marker` (若無高階 GPU)

### 3. RAG 適用性 (Clean Output)
RAG 最需要的是**結構化且帶有語意的文本** (如 Markdown 標題層級)。
*   **最佳選擇**: `LlamaParse` 和 `Marker`。它們直接輸出 Markdown，保留了標題層級 (#, ##) 和表格結構，讓 Embedding 模型更容易理解上下文。
*   **傳統工具問題**: `pypdf` 和 `PyMuPDF` 輸出的通常是 "文字流 (Stream of text)"，表格會變成一堆亂碼或無意義的換行，嚴重干擾 RAG 檢索。

---

## 4.程式碼範例 (Python)

如果你想快速試用效果最好的 **LlamaParse** (需安裝 `llama-parse` 和 `llama-index`)請參考demo_llama_parse.py
