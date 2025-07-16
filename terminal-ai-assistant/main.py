import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent

# 1️⃣ Load your API key and environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def main():
    # 2️⃣ Initialize the OpenAI language model
    model = ChatOpenAI(temperature=0)

    # 3️⃣ Define tools (currently none)
    tools = []

    # 4️⃣ Create the agent using LangGraph ReAct
    agent_executor = create_react_agent(model, tools)

    print("👋 Welcome! I'm your AI assistant. Type 'quit' to exit.")

    # 5️⃣ Chat loop
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":
            print("👋 Goodbye!")
            break

        print("\nAssistant: ", end="")

        # 6️⃣ Stream AI response
        for chunk in agent_executor.stream({"messages": [HumanMessage(content=user_input)]}):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")

        print()  # New line after assistant reply

# 7️⃣ Run the chatbot
if __name__ == "__main__":
    main()
