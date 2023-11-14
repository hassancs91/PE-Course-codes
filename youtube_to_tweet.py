import helpers
import llm
from prompts import youtube_prompts

selected_model = "gpt-3.5-turbo"

youtube_url = "https://www.youtube.com/watch?v=r7uISjR_fLM"

video_transcript = helpers.get_video_transcript(youtube_url)

prompt = youtube_prompts.tweet_from_youtube_prompt.format(transcript=video_transcript)

response = llm.llm_generate_text(prompt, "OpenAI", selected_model)

print(response)
