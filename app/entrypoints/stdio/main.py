from app.mcp.demo_server.server import demo_mcp_server


async def async_main() -> None:
    print("Running MCP server via stdio")

    await demo_mcp_server.run_stdio_async()


def main() -> None:
    import asyncio
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
