import llm

selected_model = "gpt-4"

test_prompt = """Act as a creative content strategist and generate 5 catchy YouTube titles for a video about [topic]. Aim to 
create titles that grab attention, are easily searchable, and encourage users to click on and watch the video. The titles should be relevant to the video content and target audience, while also taking into consideration YouTube's character limits and best practices for titles."""

input_list = [
    "email marketing",
    "bitcoin trading",
    "advanced prompt engineering techniques",
]

for input in input_list:
    prompt = test_prompt.replace("topic", input)
    response = llm.llm_generate_text(prompt, "OpenAI", selected_model)
    print(response)
    print("---------------------")
