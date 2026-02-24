from configs.model_config import geminiModel
from tools.async_utils import resolve_async_generator


class ReviewerAgent:

    def reviewContent(self, summaries: list) -> str:
        # summaries should already be plain strings; join them for the prompt
        combinedText = "\n".join(summaries)

        async_gen = geminiModel.generate_content_async(
            f"""
Improve clarity, remove duplicates, and ensure completeness:

{combinedText}
"""
        )

        # consume the async generator before returning
        finalText = resolve_async_generator(async_gen)
        return finalText