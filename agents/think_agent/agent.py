from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters

root_agent = Agent(
    name="research_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that help the user solve math problems and task that needs thinking"
    ),
    instruction=(
        "You are a helpful agent that users to solve complex tasks"
    ),
    tools=[
      MCPToolset(
        connection_params = StdioConnectionParams(
          server_params = StdioServerParameters(
            command="npx",
            args=[
              "-y",
              "@modelcontextprotocol/server-sequential-thinking"
            ]
          )
        )
      )
    ],
)