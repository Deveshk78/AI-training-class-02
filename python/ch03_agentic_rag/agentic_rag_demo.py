from typing import TypedDict, Annotated, Literal


class AgentState(TypedDict):
    query: str
    retrieved: list[str]
    tool_results: list[str]
    final_answer: str


class SimpleAgent:
    def __init__(self):
        self.tool_registry = {
            "search": self._search,
            "calendar": self._calendar,
        }

    def _search(self, query: str):
        return [f"Search result for: {query}"]

    def _calendar(self, query: str):
        return [f"Calendar result for: {query}"]

    def plan(self, query: str) -> list[str]:
        if "calendar" in query.lower():
            return ["calendar"]
        return ["search"]

    def run(self, query: str) -> str:
        retrieved = ["Document chunk A", "Document chunk B"]
        tool_calls = []
        for tool_name in self.plan(query):
            tool_call = self.tool_registry[tool_name](query)
            tool_calls.extend(tool_call)

        final_answer = (
            f"Answer for query: {query}\n"
            f"Retrieved context: {retrieved}\n"
            f"Tool outputs: {tool_calls}"
        )
        return final_answer


if __name__ == "__main__":
    agent = SimpleAgent()
    print(agent.run("Find the latest policy and check calendar availability."))
