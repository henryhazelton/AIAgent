import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from call_function import available_functions

from prompts import system_prompt

available_functions = types.Tool(
    function_declarations=[schema_get_files_info],
)


def generate_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    return response


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

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

    function_available = response.function_calls

    if function_available:
        for function in function_available:
            print(f"Calling function: {function.name}({function.args})")

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
