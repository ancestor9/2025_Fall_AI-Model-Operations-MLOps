# server.py
# week11/server.py (예시: add 툴 추가)
from fastmcp import FastMCP

mcp = FastMCP("MCP Demo Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)

