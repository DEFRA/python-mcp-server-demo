from mcp.server.fastmcp import FastMCP

demo_mcp_server = FastMCP("Python MCP Server Demo")

@demo_mcp_server.tool()
def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y

