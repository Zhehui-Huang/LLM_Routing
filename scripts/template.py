import openai
from openai import OpenAI

client = OpenAI()

# Initialize a list to store messages.
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]


# Function to add a message to the conversation history
def add_message(role, content):
    messages.append({"role": role, "content": content})


# Function to handle conversation and API interaction
def handle_conversation():
    while True:
        prompt = input("")

        add_message("user", prompt)

        # Construct the messages for the API request
        messages_for_api = [{"role": m["role"], "content": m["content"]} for m in messages]

        # Create a response using the OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use the model specified in the documentation
            messages=messages_for_api,
            max_tokens=150
        )

        # Extract and process the response
        if response.choices and len(response.choices) > 0:
            full_response = response.choices[0].message.content
            print("Assistant:", full_response)  # Display the full response
            add_message("assistant", full_response)
        else:
            print("No response received from the API.")


# Example of running the conversation handler
handle_conversation()
