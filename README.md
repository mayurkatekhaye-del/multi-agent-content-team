# AI Content Team — Multi-Agent System

A multi-agent content generation pipeline built with **LangGraph**, **LangChain**, and **Google Gemini**. Three AI agents — Researcher, Writer, and Editor — work together sequentially to research a topic, draft social media content, and polish it into a final version.

## How It Works
- **Researcher Agent**: Searches the web (via Tavily) and summarizes key points about the topic.
- **Writer Agent**: Turns the research into an engaging social media post.
- **Editor Agent**: Reviews and polishes the draft for grammar, tone, and impact.

## Tech Stack

- Python
- LangGraph (agent orchestration)
- LangChain
- Google Gemini API (`gemini-2.5-flash`)
- Tavily Search API
- Gradio (UI)

## Setup

1. Clone the repo:
```bash
   git clone https://github.com/mayurkatekhaye-del/multi-agent-content-team.git
   cd multi-agent-content-team
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Create a `.env` file and add your API keys:
- Get a Gemini API key: https://aistudio.google.com/app/apikey
   - Get a Tavily API key: https://tavily.com

4. Run the app:
```bash
   python app.py
```

5. Open the local URL shown in the terminal (usually `http://127.0.0.1:7860`).

## Project Structure
## Example

**Input:** `"SYNTIX - AI marketing automation for local businesses in India"`

**Output:** A researched, written, and polished social media post ready to publish.

## Future Improvements

- Conditional routing: Editor sends draft back to Writer if it needs more work
- Add an SEO/Hashtag Generator agent
- Deploy on Hugging Face Spaces for a live demo link