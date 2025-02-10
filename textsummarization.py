import requests

# Define Ollama API Endpoint
OLLAMA_API = "http://localhost:11434/api/generate"
MODEL = "deepseek-r1:1.5b"  # Use DeepSeek model

def summarize_text(text):
    """Send a request to DeepSeek API for summarization."""
    payload = {
        "model": MODEL,
        "prompt": f"Summarize the following text in a few sentences:\n\n{text}",
        "stream": False
    }
    
    response = requests.post(OLLAMA_API, json=payload)
    
    if response.status_code == 200:
        return response.json().get("response", "No response received.")
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example: Input Text for Summarization
text_to_summarize = """
Artificial Intelligence (AI) is rapidly evolving, transforming industries from healthcare to finance. 
Machine learning and deep learning are key drivers behind AI advancements, allowing computers to learn 
from data and improve performance without explicit programming. Companies are investing heavily in AI 
research to develop smarter applications that enhance productivity and automate tasks.
"""

# Generate Summary
summary = summarize_text(text_to_summarize)
print("\n📝 **Original Text:**\n", text_to_summarize)
print("\n📌 **Summarized Version:**\n", summary)