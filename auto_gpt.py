import llm
from prompts import productivity_prompts


selected_model = "gpt-3.5-turbo"
input_text = "Get me the latest price of bitcoin"
# input_text = "Extract the main points of the following text: [text...]"


prompt = productivity_prompts.auto_gpt_prototype.format(user_input=input_text)


response = llm.llm_generate_text(prompt, "OpenAI", selected_model)


if response == "1":
    # simulate search the web
    print("searching the web...")
if response == "2":
    # simulate search the web
    print("Summarizing...")
if response == "3":
    # simulate search the web
    print("Translating...")
