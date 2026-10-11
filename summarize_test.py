from google import genai

client = genai.Client()

text = """Python is a high-level programming language known for its readable
syntax. It is widely used in web development, data science, automation, and
AI engineering, and has a large ecosystem of third-party libraries."""

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=f"Summarize this in one sentence:\n\n{text}",
)
print(response.text)
