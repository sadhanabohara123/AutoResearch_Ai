def summarizeText(text: str, maxSentences: int = 5) -> str:
    sentences = text.split(".")
    summary = ".".join(sentences[:maxSentences])
    return summary.strip()