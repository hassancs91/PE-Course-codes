import openai
import nlpcloud
import cohere
import json

"""
LLMs:
OpenAI
NlpCloud
Cohere
You can add your own
"""


def llm_generate_text_with_save(prompt, service, model):
    if service == "OpenAI":
        generated_text = openai_generate(prompt, model)
        # save generated text
    elif service == "NlpCloud":
        generated_text = nlp_cloud_generate(prompt, model)
    elif service == "Cohere":
        generated_text = cohere_generate(prompt, model)

    save_to_json(prompt, generated_text)
    return generated_text


def save_to_json(prompt, response):
    data = {"prompt": prompt, "response": response}
    with open("ai_prompts_responses.json", "a") as f:
        f.write(json.dumps(data) + "\n")


def llm_generate_text(prompt, service, model):
    if service == "OpenAI":
        generated_text = openai_generate(prompt, model)
    elif service == "NlpCloud":
        generated_text = nlp_cloud_generate(prompt, model)
    elif service == "Cohere":
        generated_text = cohere_generate(prompt, model)

    return generated_text


# Open AI Function
openai.api_key = "sk-XXX"


def openai_generate(user_prompt, selected_model):
    completion = openai.chat.completions.create(
        model=selected_model, messages=[{"role": "user", "content": user_prompt}]
    )
    return completion.choices[0].message.content


# nlpCloud Function
nlp_cloud_key = "use-your-own-API"
def nlp_cloud_generate(user_prompt,selected_model):
    client = nlpcloud.Client(selected_model, nlp_cloud_key, gpu=True, lang="en")
    result = client.generation(
    user_prompt,
    max_length=200,
    length_no_input=True,
    remove_input=True,
    end_sequence=None,
    top_p=1,
    temperature=0.8,
    top_k=50,
    repetition_penalty=1,
    num_beams=1,
    num_return_sequences=1,
    bad_words=None,
    remove_end_sequence=False
)
    return result["generated_text"]


# Cohere API
cohere_api_key = "fk8B74dEf1DusuFJoi"


def cohere_generate(user_prompt, selected_model):
    co = cohere.Client(cohere_api_key)  # This is your trial API key
    response = co.generate(
        model=selected_model,
        prompt=user_prompt,
        max_tokens=300,
        temperature=0.9,
        k=0,
        stop_sequences=[],
        return_likelihoods="NONE",
    )

    return response.generations[0].text
