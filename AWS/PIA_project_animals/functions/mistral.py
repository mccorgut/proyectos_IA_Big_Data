# functions/mistral.py
import os
from mistralai import Mistral  # Import the Mistral class for making API requests

# Load environment variables from the .env file
from dotenv import load_dotenv
load_dotenv()

# Retrieve the Mistral API key from environment variables
api_key = os.environ["MISTRAL_API_KEY"]  # Get the MISTRAL API key
model = "mistral-large-latest"  # Define the model to use (mistral-large-latest)

# Create a Mistral client instance with the provided API key
client = Mistral(api_key=api_key)

# Function to generate fun facts about a given animal
def generate_fun_facts(animal_name):
    try:
        # Construct the user message to request fun facts about the animal
        prompt = f"Tell me 3 fun and interesting facts about the animal '{animal_name}' in an engaging and educational style."

        # Make a request to the Mistral API to generate the response
        chat_response = client.chat.complete(
            model=model,  # Specify the model to use
            messages=[  # Define the conversation format
                {
                    "role": "user",  # The user role is requesting information
                    "content": prompt  # The content of the user's message (the prompt)
                }
            ]
        )

        # Extract the generated fun facts from the response
        fun_facts = chat_response.choices[0].message.content
        print("Fun Facts:", fun_facts)  # Print the fun facts for debugging purposes
        return fun_facts  # Return the fun facts

    except Exception as e:
        # Print any errors that occur during the process
        print(f"Error generating fun facts: {e}")
        # Return a generic error message if the function fails
        return f"Error generating fun facts for {animal_name}."
