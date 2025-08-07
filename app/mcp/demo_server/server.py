from random import randint

from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel


class WeatherData(BaseModel):
    location: str
    temperature: str
    condition: str

demo_mcp_server = FastMCP("Python MCP Server Demo")


@demo_mcp_server.tool()
def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y


@demo_mcp_server.tool()
def subtract(x: int, y: int) -> int:
    """Subtract two numbers."""
    return x - y


@demo_mcp_server.tool()
def get_weather(location: str) -> WeatherData:
    """Get the current weather in a given location"""

    return WeatherData(
        location=location,
        temperature=f"{randint(1, 30)}°C", # noqa: S311
        condition="Sunny"
    )
