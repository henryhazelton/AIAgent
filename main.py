import os
import sys
from config import system_prompt
from dotenv import load_dotenv
from google import genai
from google.genai import types


def generate_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    generated_text, prompt_tokens, response_tokens = (
        response.text,
        f"Prompt tokens: {response.usage_metadata.prompt_token_count}",
        f"Response tokens: {response.usage_metadata.candidates_token_count}",
    )
    # prompt_tokens = f"Prompt tokens: {response.usage_metadata.prompt_token_count}"
    # response_tokens = f"Response tokens: {response.usage_metadata.candidates_token_count}"
    return generated_text, prompt_tokens, response_tokens


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    client = genai.Client(api_key=api_key)

    generated_text, prompt_tokens, response_tokens = generate_content(client, messages)

    if len(sys.argv) < 2:
        print("Must input a prompt for the program to run")
        sys.exit(1)
    elif len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    else:
        print(generated_text)


if __name__ == "__main__":
    main()
