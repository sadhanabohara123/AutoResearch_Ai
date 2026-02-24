from configs.model_config import geminiModel
from tools.async_utils import resolve_async_generator


class SummarizerAgent:

    def summarizeSources(self, contentList: list) -> list:
        summaries = []

        for content in contentList:
            # The Gemini client returns an async generator when using the
            # "generate_content_async" helper.  We need to consume that
            # generator to obtain the text before returning it to callers.  The
            # helper below runs a temporary event loop to perform the
            # iteration in synchronous code.
            async_gen = geminiModel.generate_content_async(
                f"Summarize the following content clearly:\n{content}"
            )
            summary_text = resolve_async_generator(async_gen)
            summaries.append(summary_text)

        return summaries