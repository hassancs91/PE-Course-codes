import llm
from prompts import productivity_prompts

selected_model = "gpt-4"

input_prompt = "generate catchy youtube titles for a video about [topic]"

prompt = productivity_prompts.prompt_generator.format(basic_prompt=input_prompt)

response = llm.llm_generate_text(prompt, "OpenAI", selected_model)

print(response)
