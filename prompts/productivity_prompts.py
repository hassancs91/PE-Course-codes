summarize_text_to_bullet_points = """Your task is to create a concise summary
of the provided text.

I want you to remember the following information: When it comes to writing content,
two factors are crucial, "perplexity" and "burstiness."
Perplexity measures the complexity of text. Separately,
burstiness compares the variations of sentences.

Your summary should adhere to the given bullet points number.

Please format your response as bullet points. and add emojies when relevant

Minimum Number of Bullet Points: [{Minimum}]
Maximum Number of Bullet Points: [{Maximum}]
Provided Text: [{Text}]"""


extract_template_from_subject_line = """Your task is to create a
versatile email subject line 
template that can be adapted for use in various niches. 
You will be given a specific subject line, and your response should include
the generated generic template based on that input.

To generate this adaptable template, 
replace unique elements within the original subject line with placeholders
(such as X or [Goal]) while preserving the overall
structure of the initial subject line. Your final
output should enable users to easily customize it to their
needs by substituting these placeholders with relevant content
related to their niche.

And then share some catchy subject line examples
using the generated template.

Input Subject Line: [{subject_line}]
"""


auto_gpt_prototype = """I will provide you with a task and [user_input], 
and you should understand and pick the right action from the following:
1- search the web for the [user_input]
2- summarize [user_input]
3- translate [user_input] to english
output: reply only with action number like 1,2, or 3
Task and User input: [{user_input}]"""


prompt_generator = """Act as a prompt generator for ChatGPT.
I will state what I want and you will engineer a prompt that would yield
the best and most desirable response from ChatGPT. Each prompt should
involve asking ChatGPT to "act as [role]", for example, "act as a digital marketer".
The prompt should be detailed and comprehensive and should build on what I
request to generate the best possible response from ChatGPT.
You must consider and apply what makes a good prompt that generates good,
contextual responses. Don't just repeat what I request, improve and build
upon my request so that the final prompt will yield the best, most useful
and favorable response out of ChatGPT. 
Here is the prompt I want: [{basic_prompt}]"""
