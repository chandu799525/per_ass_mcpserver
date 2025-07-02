import pandas as pd
from mcp.server.fastmcp import FastMCP
import os
import uvicorn

mcp = FastMCP("vishesh")

@mcp.tool()
async def get_company_faq() -> str:
    """
    Reads an Excel file with company FAQs and returns a formatted FAQ summary.
    Excel must contain columns: 'Question' and 'Answer'.
    """
    file_path = "C:/Users/Vishesh/Documents/chandu/about_vishesh.xlsx"  # Update if needed
    try:
        df = pd.read_excel(file_path)
        if "Question" not in df.columns or "Answer" not in df.columns:
            return "❌ Excel file must have 'Question' and 'Answer' columns."

        summary = "📌 Vishesh Country Cache - FAQ\n\n"
        for index, row in df.iterrows():
            q = str(row["Question"]).strip()
            a = str(row["Answer"]).strip()
            summary += f"**Q: {q}**\nA: {a}\n\n"

        return summary.strip()

    except Exception as e:
        return f"❌ Failed to read FAQ Excel: {str(e)}"

if __name__ == "__main__":
    uvicorn.run(mcp.sse_app, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
