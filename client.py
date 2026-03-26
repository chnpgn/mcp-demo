import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:", tools)

            weather = await session.call_tool(
                "get_weather",
                {"city": "Johannesburg"}
            )

            print("Weather:", weather)

            result = await session.call_tool(
                "add_numbers",
                {"a": 5, "b": 7}
            )

            print("Addition result:", result)


asyncio.run(main())
