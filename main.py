import helpers
import llm
from prompts import blog_prompts, productivity_prompts, text_analysis, Ideas
import blog_summarization


selected_model = "gpt-3.5-turbo"
input_text = "no code tools"


prompt = Ideas.domain_brand_names.format(Niche=input_text)


# caclulate prompt cost
token_count = helpers.count_tokens(prompt, selected_model)
estmiated_cost = helpers.estimate_input_cost(selected_model, token_count)
print(f"Cost: {estmiated_cost}")


response = llm.llm_generate_text_with_save(prompt, "OpenAI", selected_model)

print("Result:")
print(response)
