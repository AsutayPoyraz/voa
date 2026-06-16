# 🎤 VOA - Voice AI Assistant

A powerful AI chatbot powered by Google's Gemini 3.5 API. Chat with an intelligent assistant using natural language!

## 🚀 Features

- 💬 **Interactive Chat** - Have conversations with AI
- 🧠 **Context Awareness** - Remembers previous messages in the conversation
- ⚡ **Fast Responses** - Powered by Gemini 1.5 Flash model
- 🔐 **Secure** - API keys stored safely in `.env` file
- 🎯 **Configurable** - Easy to customize model parameters

## 📋 Requirements

- Python 3.8+
- Google Gemini API Key

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Brave-herart/voa.git
cd voa
```

### 2. Create virtual environment
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up API Key
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your Gemini API Key
# GEMINI_API_KEY=your_api_key_here
```

**How to get API Key?**
1. Go to [Google AI Studio](https://aistudio.google.com)
2. Click "Get API Key"
3. Create new API key
4. Copy and paste in `.env` file

## 💻 Usage

### Run the chatbot
```bash
python main.py
```

### Example conversation
```
==============================================================
🎤 VOA - Voice AI Assistant
==============================================================
Type 'quit' or 'exit' to end the conversation

You: What is machine learning?

VOA: Machine learning is a subset of artificial intelligence...

You: Can you explain it like I'm 5?

VOA: Imagine a robot that learns by playing games...

You: quit
VOA: Goodbye! 👋
```

## ⚙️ Configuration

Edit these in `.env` file:

```env
# Required
GEMINI_API_KEY=your_api_key_here

# Optional (defaults shown)
MODEL=gemini-1.5-flash
TEMPERATURE=0.7
MAX_OUTPUT_TOKENS=1024
```

**Parameters:**
- `TEMPERATURE` (0.0-2.0): How creative the responses are
  - Lower = More focused and deterministic
  - Higher = More random and creative
- `MAX_OUTPUT_TOKENS`: Maximum length of responses

## 📁 Project Structure

```
voa/
├── main.py              # Main application
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variables template
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🔒 Security

- ✅ API keys are **never** committed to GitHub
- ✅ `.env` file is ignored by Git
- ✅ Only `.env.example` is shared as a template

## 🐛 Troubleshooting

### "GEMINI_API_KEY not found"
- Check `.env` file exists
- Verify API key is set correctly
- Make sure you're in the right directory

### "ModuleNotFoundError"
- Activate virtual environment
- Run `pip install -r requirements.txt`

### "API Error"
- Check your internet connection
- Verify API key is valid
- Check your Gemini API quota

## 📚 Resources

- [Google Generative AI Documentation](https://ai.google.dev)
- [Gemini API Guide](https://ai.google.dev/docs)
- [Python Dotenv Documentation](https://python-dotenv.readthedocs.io)

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created by Brave-herart

---

**Happy Chatting! 🚀**
