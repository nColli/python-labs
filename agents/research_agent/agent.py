from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters

root_agent = Agent(
    name="research_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that searchs academic papers about a topic entered by the user"
    ),
    instruction=(
        "You are a helpful agent that helps students find academic papers for their research and assignments"
    ),
    tools=[
      MCPToolset(
        connection_params = StdioConnectionParams(
          server_params = StdioServerParameters(
            command="python",
            args=[
              "-m",
              "mcp_simple_arxiv"
            ]
          )
        )
      ),
      MCPToolset(
        connection_params = StdioConnectionParams(
          server_params = StdioServerParameters(
            command="uvx",
            args=[
              "pubmedmcp@latest"
            ]
          )
        )
      )
    ],
)