import llm



def generate_template(user_input_1, user_prompt):
    try:
        prompt = user_prompt.replace("user_input_1", user_input_1)
        return prompt
    except Exception as e:
        return "Error"


response = generate_template(
    "digital marketing",
    "generate 5 seo optimized titles for a blog about [user_input_1]",
)

print(response)
