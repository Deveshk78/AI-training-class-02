# Minimal MCP-like tool registration example for teaching.
# Real MCP would use a protocol and tool schemas, but this helps explain the mindset.

class MCPTool:
    def __init__(self, name: str, description: str, function):
        self.name = name
        self.description = description
        self.function = function


class MCPServer:
    def __init__(self):
        self.tools = []

    def register(self, tool: MCPTool):
        self.tools.append(tool)

    def list_tools(self):
        return [(tool.name, tool.description) for tool in self.tools]


if __name__ == "__main__":
    server = MCPServer()
    server.register(MCPTool("search_documents", "Find documents by semantic query.", lambda q: f"search:{q}"))
    server.register(MCPTool("get_weather", "Retrieve weather info.", lambda q: f"weather:{q}"))
    print(server.list_tools())
