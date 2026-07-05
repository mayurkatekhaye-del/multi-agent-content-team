import gradio as gr
from graph import app

def run_pipeline(topic):
    if not topic.strip():
        return "Please enter a topic.", "", ""
    result = app.invoke({"topic": topic})
    return result["research"], result["draft"], result["final_content"]

demo = gr.Interface(
    fn=run_pipeline,
    inputs=gr.Textbox(label="Topic", placeholder="e.g. SYNTIX - AI marketing automation for local businesses"),
    outputs=[
        gr.Textbox(label="🔍 Research"),
        gr.Textbox(label="✍️ Draft"),
        gr.Textbox(label="✅ Final Content")
    ],
    title="AI Content Team - Multi-Agent System",
    description="Researcher → Writer → Editor agents working together using LangGraph + Gemini"
)

if __name__ == "__main__":
    demo.launch()