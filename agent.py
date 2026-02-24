from sub_agents.web_research_agent import WebResearchAgent
from sub_agents.summarizer_agent import SummarizerAgent
from sub_agents.reviewer_agent import ReviewerAgent
from tools.generate_final_report import generateFinalReport


class RootAgent:

    def __init__(self):
        self.webResearchAgent = WebResearchAgent()
        self.summarizerAgent = SummarizerAgent()
        self.reviewerAgent = ReviewerAgent()

    def processQuery(self, userQuery: str) -> str:
        collectedContent = self.webResearchAgent.searchAndCollect(userQuery)
        collectedList = [collectedContent]
        summaries = self.summarizerAgent.summarizeSources(collectedList)
        finalAnswer = self.reviewerAgent.reviewContent(summaries)
        return generateFinalReport(finalAnswer)


if __name__ == "__main__":
    rootAgent = RootAgent()
    userQuery = input("Enter your research query: ")
    result = rootAgent.processQuery(userQuery)
    print(result)