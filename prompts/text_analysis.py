simple_classfication_prompt = """Your task as a text analyzer is to classify
a given sentence into one of the specific categories: 'food', 'sports', or 'business'.
In doing so, you must carefully consider the main theme and context of the sentence.
Your response should clearly communicate your classification choice for the sentence and
provide a brief explanation that highlights key elements, such as words or phrases,
that support your decision.
Please note that your analysis should be adaptable,
flexible, and capable of addressing a wide range of sentence types and structures.
Your objective is to deliver a precise, accurate,
and insightful categorization that demonstrates an in-depth understanding 
of the main theme and context of the sentence while focusing on the designated categories.
Input Sentence: [{sentence}]"""

sentiment_analysis = """I will provide you with a sentence, and I want to you to analyze the 
sentiment, and return back Positive, Negative, Neutral. reply with just a one word.
sentence:[{sentence}]"""

sentiment_analysis_numbers = """I will provide you with a sentence, and I want to you to analyze the 
sentiment, and return back 1 if Positive, -1 if Negative, and 0 if Neutral. reply with just a number.
sentence:[{sentence}]"""
