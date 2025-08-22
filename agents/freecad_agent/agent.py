from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters

root_agent = Agent(
    name="research_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that help users to create draws in freecad"
    ),
    instruction=(
        "You take the user request and transform it into a draw in freecad"
    ),
    tools=[
      MCPToolset(
        connection_params = StdioConnectionParams(
          server_params = StdioServerParameters(
            command="uvx",
            args=[
              "freecad-mcp"
            ]
          )
        )
      )
    ],
)