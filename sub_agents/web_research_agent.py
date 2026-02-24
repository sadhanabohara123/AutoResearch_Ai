from configs.model_config import geminiModel
from google.adk.tools.google_search_tool import GoogleSearchTool


class WebResearchAgent:

    def __init__(self):
        self.searchTool = GoogleSearchTool()

    def searchAndCollect(self, userQuery: str):
        prompt = f"""
Search the web for the following query and collect top 3-5 sources.
Extract key important information from the sources.
Return summarized findings.

Query: {userQuery}
"""
        response = geminiModel._generate_content_via_interactions(prompt,None)
        # generate(prompt)
        return response