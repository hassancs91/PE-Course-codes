import helpers
import llm
from prompts import youtube_prompts


selected_model = "gpt-3.5-turbo"

youtube_url = "https://www.youtube.com/watch?v=mBYu5NoXBcs"  # 30 minutes video

video_transcript = helpers.get_video_transcript(youtube_url)

# Split transcript into chunks if needed
chunks = (
    helpers.split_text_into_chunks(video_transcript, helpers.max_tokens_per_chunk)
    if helpers.count_tokens(video_transcript, selected_model)
    > helpers.max_tokens_per_chunk
    else [video_transcript]
)

# Initialize overall output
overall_output = ""

for chunk in chunks:
    prompt = youtube_prompts.youtube_to_points_summary.format(transcript=chunk)
    chunk_output = llm.llm_generate_text(prompt, "OpenAI", selected_model)
    overall_output += chunk_output


print(overall_output)
