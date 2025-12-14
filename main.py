import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt


def generate_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    return response


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # if len(sys.argv) < 2:
    #     print("Must input a prompt for the program to run")
    #     sys.exit(1)

    if len(sys.argv) >= 2:
        user_prompt = sys.argv[1]
    else:
        user_prompt = "Let the user know you would like to assist them!"

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    client = genai.Client(api_key=api_key)

    response = generate_content(client, messages)

    generated_text, prompt_tokens, response_tokens = (
        response.text,
        f"Prompt tokens: {response.usage_metadata.prompt_token_count}",
        f"Response tokens: {response.usage_metadata.candidates_token_count}",
    )

    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        print(f"User prompt: {user_prompt}")
        print(prompt_tokens)
        print(response_tokens)
    else:
        print(prompt_tokens)
        print(response_tokens)
        print(generated_text)


if __name__ == "__main__":
    main()
