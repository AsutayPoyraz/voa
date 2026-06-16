import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=API_KEY)

# Model configuration
MODEL_NAME = os.getenv("MODEL", "gemini-1.5-flash")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
MAX_TOKENS = int(os.getenv("MAX_OUTPUT_TOKENS", "1024"))

def create_model():
    """Create and configure the Gemini model"""
    return genai.GenerativeModel(
        model_name=MODEL_NAME,
        generation_config={
            "temperature": TEMPERATURE,
            "max_output_tokens": MAX_TOKENS,
        }
    )

def chat_with_voa(user_message: str, conversation_history: list = None) -> str:
    """
    Send a message to VOA and get a response
    
    Args:
        user_message: The user's input message
        conversation_history: Previous messages for context
    
    Returns:
        The AI's response
    """
    model = create_model()
    
    # Start a chat session if we have history
    if conversation_history:
        chat = model.start_chat(history=conversation_history)
        response = chat.send_message(user_message)
    else:
        response = model.generate_content(user_message)
    
    return response.text

def main():
    """Main function to run VOA interactive chat"""
    print("=" * 60)
    print("🎤 VOA - Voice AI Assistant")
    print("=" * 60)
    print("Type 'quit' or 'exit' to end the conversation\n")
    
    conversation_history = []
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nVOA: Goodbye! 👋")
                break
            
            if not user_input:
                continue
            
            # Get response from VOA
            print("\nVOA: Thinking...", end="\r")
            response = chat_with_voa(user_input, conversation_history)
            
            # Clear the "Thinking..." message
            print("\rVOA: " + response + "\n")
            
            # Store in history for context
            conversation_history.append({
                "role": "user",
                "parts": [user_input]
            })
            conversation_history.append({
                "role": "model",
                "parts": [response]
            })
            
        except KeyboardInterrupt:
            print("\n\nVOA: Conversation interrupted. Goodbye! 👋")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Please try again.\n")

if __name__ == "__main__":
    main()
