import gradio as gr
import requests

def query_api(user_input):
    response = requests.post("http://localhost:8000/search", json={"query": user_input})
    data = response.json()["results"]
    print(data)  # Debugging line to check the response data
    # Prepare images with captions
    gallery_items = [(item["result"], item["url"]) for item in data]
    return gallery_items

with gr.Blocks() as demo:
    gr.Markdown("## 🖼️ Semantic Search: Text + Image")
    with gr.Row():
        query_input = gr.Textbox(label="Enter your query")
        search_btn = gr.Button("Search")
    
    gallery_output = gr.Gallery(label="Results",columns=2, height="auto")

    search_btn.click(fn=query_api, inputs=query_input, outputs=gallery_output)

demo.launch()
