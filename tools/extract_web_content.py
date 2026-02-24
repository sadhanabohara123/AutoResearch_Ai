import requests
from bs4 import BeautifulSoup


def extractWebContent(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        textContent = " ".join(p.get_text() for p in paragraphs)
        return textContent[:3000]
    except Exception as error:
        return f"Error extracting content: {str(error)}"