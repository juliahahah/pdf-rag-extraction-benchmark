import os
import sys
from llama_parse import LlamaParse

# ---------------------------------------------------------
# 設定區
# ---------------------------------------------------------

# 1. 設定 API Key
# 您可以將 Key 設定在環境變數中，或是直接填入下方引號內
# 申請網址: https://cloud.llamaindex.ai/
API_KEY = "請填入您的_LLAMA_INDEX_API_KEY" 

# 2. 設定要讀取的 PDF 檔案路徑
FILE_PATH = "./Benchmarking_Collaborative_AI_Agents.pdf"

# ---------------------------------------------------------
# 主程式
# ---------------------------------------------------------

def main():
    # 檢查 API Key
    if API_KEY == "llx-..." and not os.getenv("LLAMA_CLOUD_API_KEY"):
        print("錯誤: 請先設定您的 LlamaCloud API Key")
        print("請編輯此檔案，將 API_KEY 變數修改為您的 Key")
        return

    # 設定環境變數 (如果尚未設定)
    if "LLAMA_CLOUD_API_KEY" not in os.environ:
        os.environ["LLAMA_CLOUD_API_KEY"] = API_KEY

    # 檢查檔案是否存在
    if not os.path.exists(FILE_PATH):
        print(f"錯誤: 找不到檔案 '{FILE_PATH}'")
        print("請編輯此檔案，將 FILE_PATH 變數修改為您實際的 PDF 路徑")
        return

    print(f"正在初始化 LlamaParse (目標語言: 英文)...")
    
    try:
        parser = LlamaParse(
            result_type="markdown",  # 關鍵：輸出 Markdown 格式，最適合 RAG
            num_workers=4,           # 平行處理的 worker 數量
            verbose=True,            # 顯示詳細進度
            language="en",           # 設定語言 (英文: "en", 繁體中文: "ch_tra")
            invalidate_cache=True    # 強制重新解析，不使用快取
        )

        print(f"開始解析檔案: {FILE_PATH} ...")
        documents = parser.load_data(FILE_PATH)

        if documents:
            print(f"\n成功提取 {len(documents)} 個文件片段/頁面。")
            
            # 將所有片段合併
            full_content = "\n\n".join([doc.text for doc in documents])
            
            print("\n" + "="*50)
            print("預覽前 500 字內容：")
            print("="*50 + "\n")
            
            print(full_content[:500] + "...\n")

            # 將結果存檔
            output_filename = os.path.splitext(FILE_PATH)[0] + "_parsed.md"
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(full_content)
            
            print("="*50)
            print(f"完整 Markdown 內容已儲存至: {output_filename}")
            print(f"檔案大小: {len(full_content)} 字元")
            print("="*50)
        else:
            print("警告: 未提取到任何內容。")

    except Exception as e:
        print(f"\n發生錯誤: {e}")
        print("請檢查 API Key 是否正確，或網路連線是否正常。")

if __name__ == "__main__":
    main()
