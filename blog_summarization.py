import helpers
import llm
from prompts import blog_prompts

selected_model = "gpt-3.5-turbo"

blog_url = "https://learnwithhasan.com/chatgpt-earthquake/"

blog_article = helpers.get_article_from_url(blog_url)

prompt = blog_prompts.blog_bullet_summary_prompt.format(
    MaxPoints="10", MinPoints="5", InputText=blog_article
)

response = llm.llm_generate_text(prompt, "OpenAI", selected_model)

print(response)
