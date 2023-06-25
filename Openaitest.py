import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write an email to my boss for resignation\n",
  temperature = 1,
  max_tokens = 256,
  top_p = 1,
  frequency_penalty = 0,
  presence_penalty = 0
)
print(response)
'''
{
  "id": "cmpl-7UUhfywa01fFp4aYzvB3NxJzmq0vu",
  "object": "text_completion",
  "created": 1687502219,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\nSubject: Formal Resignation \n\nDear [insert name],\n\nI am writing to inform you of my decision to resign from my position as [insert job title] at [insert company name]. After much thought and consideration, I feel that it is time for me to move on to new opportunities.\n\nMy last day of employment will be [insert date], and it has been a pleasure working here. I want to thank you for the support, encouragement, and guidance you have provided me over the past [insert time] years. I have enjoyed working here and have gained valuable experience that will hold me in good stead as I move on to the next stage of my career.\n\nI am happy to help transition the work I have been doing to the incoming [insert job title] in whatever way I can during my remaining time here. Please don't hesitate to contact me if there is anything I can provide to facilitate the process. \n\nWishing you all the best.\n\nSincerely, \n\n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 216,
    "total_tokens": 225
  }
}
'''
