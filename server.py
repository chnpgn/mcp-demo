from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Demo MCP Server")


@mcp.tool()
def get_weather(city: str) -> str:
    """Return fake weather data for a city"""
    weather_data = {
        "London": "Cloudy, 12C",
        "Johannesburg": "Sunny, 24C",
        "New York": "Rainy, 10C"
    }

    return weather_data.get(city, "Weather data not available")


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


if __name__ == "__main__":
    mcp.run()
