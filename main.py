import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions, call_function

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

    # Run response generation in a loop until response is finished

    # Loop counter adds a limit to the response calls the agent can make
    loop_counter = 0

    while loop_counter < 20:
        # Generate the response object
        response = generate_content(client, messages)
        loop_counter += 1
        # Candidate is a response variation, where response.candidates is a list of response variations
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)
        else:
            raise Exception("Response contains no variations")

        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        # A list to store the result of the function calls
        function_responses = []

        if response.function_calls:
            for function_call in response.function_calls:
                result = call_function(function_call, args.verbose)

                if (
                    not result.parts
                    or not result.parts[0].function_response
                    or not result.parts[0].function_response.response
                ):
                    raise RuntimeError(
                        f"Empty function response for {function_call.name}"
                    )
                else:
                    function_responses.append(result.parts[0])

                if args.verbose:
                    print(f"-> {result.parts[0].function_response.response}")

            # Take the list of function responses and assign them the role of user to give back to the model
            messages.append(types.Content(parts=function_responses, role="user"))

        else:
            print(response.text)
            break


if __name__ == "__main__":
    main()
