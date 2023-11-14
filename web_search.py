import helpers
import llm
import serp
from prompts import blog_prompts

selected_model = "gpt-3.5-turbo"

query = "chatgpt tricks"

search_results = serp.search_google(query, 3)


for result in search_results:
    print(f"Summary For: {result}")
    print("-----------------------")
    transcript = helpers.get_article_from_url(
        result
    )  # change the prompt to whatever you want

    prompt = blog_prompts.blog_bullet_summary_prompt.format(
        MaxPoints="10", MinPoints="5", InputText=transcript
    )

    response = llm.llm_generate_text(prompt, "OpenAI", selected_model)

    print(response)
    print("-----------------------")
