youtube_to_points_summary = """I want you to only answer in English. 
Please extract key takeaways of the youtube transcript. 
Each key takeaway should be a list item, of the following format:
"- [relevant emoji] [takeaway]"
Keep emoji unique to each takeaway item. 
Please try to use different emojis for each takeaway. Do not render brackets.
VIDEO TRANSCRIPT:{transcript}"""


tweet_from_youtube_prompt = """Act as if you're a social media expert. 
Give me a 10 tweet thread based on the follwing youtube transcript: {transcript}. 
The thread should be optimised for virality and contain 
hashtags and emoticons. Each tweet should not exceed 280 characters in length."""
