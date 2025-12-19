import argparse
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions

from prompts import system_prompt


def generate_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")
    return response


def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()  # Now we can access `args.user_prompt`

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    # Create a client
    client = genai.Client(api_key=api_key)

    # Store the messages in a list to reference
    messages = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)]),
    ]

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

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(prompt_tokens)
        print(response_tokens)
    else:
        print(generated_text)


if __name__ == "__main__":
    main()
