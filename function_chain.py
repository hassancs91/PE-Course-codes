import helpers
import llm
from prompts import text_analysis

selected_model = "gpt-3.5-turbo"

sentence = "that was a great tutorial!"

# prompt = text_analysis.sentiment_analysis.format(sentence=sentence)

# response = llm.llm_generate_text_with_save(prompt, "OpenAI", selected_model)
# print(response)


# turn into a function
def analyse_sentiment(sentence):
    prompt = text_analysis.sentiment_analysis_numbers.format(sentence=sentence)
    response = llm.llm_generate_text_with_save(prompt, "OpenAI", selected_model)
    return response


result = analyse_sentiment(sentence)
print(result)
