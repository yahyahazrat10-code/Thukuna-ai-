
import os
import json
from datetime import datetime
from openai import OpenAI

# CART3R AI
# Personal AI assistant

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

MEMORY_FILE = "cart3r_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

memory = load_memory()

def ask_cart3r(message):
    memory.append({
        "role": "user",
        "content": message
    })

    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions="""
        Your name is CART3R.
        You are a helpful, intelligent AI assistant.
        Speak naturally and confidently.
        Remember useful conversation context.
        """,
        input=memory[-20:]
    )

    answer = response.output_text

    memory.append({
        "role": "assistant",
        "content": answer
    })

    save_memory(memory)
    return answer

def main():
    print("======================")
    print("      CART3R AI")
    print("======================")
    print("Online and ready.")
    print("Type 'exit' to quit.")

    while True:
        message = input("\nYou: ")

        if message.lower() == "exit":
            print("CART3R: Goodbye.")
            break

        try:
            answer = ask_cart3r(message)
            print("\nCART3R:", answer)
        except Exception as error:
            print("Error:", error)

if __name__ == "__main__":
    main()
