import gradio as gr
import json
import os

history_file = "suhbat_tarixi.json"

def yukla_tarix():
    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def saqla_tarix(tarix):
    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(tarix, f, ensure_ascii=False, indent=4)

suhbat_tarixi = yukla_tarix()

def oddiy_javob(xabar):
    xabar = xabar.lower()
    if "salom" in xabar:
        javob = "Salom! Qalaysan?"
    elif "qalaysan" in xabar:
        javob = "Yaxshiman! Senchi?"
    elif "o'yin" in xabar:
        javob = "O'yinlar yaxshi! Qaysi birini yoqtirasan?"
    else:
        javob = "Qiziq! Yana ayt, eshitaman."
    
    suhbat_tarixi.append({"user": xabar})
    suhbat_tarixi.append({"bot": javob})
    saqla_tarix(suhbat_tarixi)
    return javob

# Gradio interfeysi
with gr.Blocks(title="Misha Bot") as demo:
    gr.Markdown("# Misha Bot - Chrome da suhbatlash! 😊")
    chatbot = gr.Chatbot(height=400)
    msg = gr.Textbox(placeholder="Xabar yozing...", label="Sizning xabaringiz")
    clear = gr.Button("Tozalash")

    def respond(message, chat_history):
        bot_message = oddiy_javob(message)
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch(share=True)  # share=True - link beradiS
    

    
