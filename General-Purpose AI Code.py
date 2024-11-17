import openai

# Function to interact with OpenAI's GPT model
def ask_gpt(prompt, api_key):
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=200,  # Adjust response length
            temperature=0.7,  # Creativity level
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Example Usage
if __name__ == "__main__":
    # Replace 'your_api_key_here' with your OpenAI API key
    API_KEY = "your_api_key_here"
    print("Welcome to General Purpose AI!")
    while True:
        user_input = input("\nAsk anything (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = ask_gpt(user_input, API_KEY)
        print("\nAI Response:")
        print(response)
