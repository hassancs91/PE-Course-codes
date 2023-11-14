import helpers
import llm
from prompts import productivity_prompts

selected_model = "gpt-3.5-turbo"
input_text = "3 Marketing Tips For Maximum Growth"


prompt = productivity_prompts.extract_template_from_subject_line.format(
    subject_line=input_text
)


response = llm.llm_generate_text(prompt, "OpenAI", selected_model)

print(response)
