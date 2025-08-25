from openai import OpenAI
import re

client = OpenAI(
    base_url="https://ai.hackclub.com/",
    api_key="none-thanks-to-hackclub"
)

def generate_better_prompt(intent, user_text):
    """Use AI to generate an optimized prompt for the user's intent and text."""
    
    meta_prompt = f"""You are an expert prompt engineer. Your job is to take the user's basic intent and text, then create a highly effective, detailed prompt that will get much better results from AI systems.

User's Intent: {intent}
User's Text: {user_text}

Create an optimized prompt that:
1. Is specific and clear about the desired output
2. Provides proper context and constraints  
3. Uses proven prompt engineering techniques
4. Will work well with ChatGPT, Claude, and other AI systems
5. Is significantly better than just asking "{intent} {user_text}"

Return ONLY the optimized prompt, nothing else."""

    response = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=[{
            "role": "user", 
            "content": meta_prompt
        }]
    )
    
    # Clean the response
    raw_response = response.choices[0].message.content
    cleaned_response = re.sub(r'<think>.*?</think>', '', raw_response, flags=re.DOTALL)
    
    return cleaned_response.strip()

def ask_hackclub(messages, model="qwen/qwen3-32b"):
    """Send messages to Hack Club AI and clean the response."""
    response = client.chat.completions.create(
        model=model,
        messages=[{
            "role":"user",
            "content":messages,
        }]
    )
    
    raw_response = response.choices[0].message.content
    cleaned_response = re.sub(r'<think>.*?</think>', '', raw_response, flags=re.DOTALL)
    
    return cleaned_response.strip()
