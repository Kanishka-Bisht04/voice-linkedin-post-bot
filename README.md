# voice-linkedin-post-bot
Telegram bot that converts voice notes into LinkedIn-ready posts using Groq API.


# Voice-to-LinkedIn Post Generator Bot  
A Telegram bot that turns voice notes into professionally written LinkedIn posts using the Groq LLaMA 3.1 model.  
It transcribes audio, generates a polished LinkedIn post, includes hashtags, shows character count, and allows users to confirm, regenerate, or discard — all without posting on LinkedIn (simulated only).

Features

Voice → Text (Transcription)
Uses Groq Whisper Large V3 for fast and accurate transcription of Telegram `.oga` / `.ogg` voice notes.

AI-Generated LinkedIn Posts  
Automatically creates a high-quality LinkedIn post with:
- A strong hook  
- 3–4 short points in the body  
- A clear call-to-action  
- 3–5 relevant hashtags  
- Character count (≤1300 chars)

Interactive Options  
After generating the draft, the bot provides:
- Yes → Mark as “Posted (simulated)”  
- Regenerate → Produce a new version  
- No → Discard the draft  

Powered By  
- Groq LLaMA 3.1 8B Instant** (FREE, ultra-fast)  
- Groq Whisper V3** for transcription  
- Python Telegram Bot 21.x**  
- Python 3.10+

Project Structure

```

voice-linkedin-post-bot/
│
├── bot.py              # Main bot source code
├── README.md           # Documentation
├── .gitignore          # Prevents venv & secrets from uploading
└── venv/               # Virtual environment (ignored)

````

Installation Guide

Clone the Repository
```bash
git clone https://github.com/Kanishka-Bisht04/voice-linkedin-post-bot.git
cd voice-linkedin-post-bot
````

Create Virtual Environment

```bash
python -m venv venv
```

Activate on Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

Install Dependencies

```bash
pip install groq python-telegram-bot==21.10
```

Add Your API Keys (Environment Variables)

Replace text with your keys:

```bash
$env:GROQ_API_KEY="your_groq_key_here"
$env:TELEGRAM_TOKEN="your_telegram_bot_token_here"
```

Running the Bot

After activating the virtual environment:

```bash
.\venv\Scripts\python.exe bot.py
```

If everything is correct, you will see:

```
Bot running...
```

Open Telegram → Search your bot → send `/start`.

Usage (User Flow)

1. User sends a **voice note**
2. Bot → *“Transcribing your voice…”*
3. Speech → Text using Groq Whisper
4. Bot → *“Creating your LinkedIn draft…”*
5. AI generates:

   * Hook
   * Body points
   * CTA
   * Hashtags
   * Character count
6. Bot shows: Yes / No / Regenerate
7. “Yes” → Bot replies: *“Posted (simulated).”

Example Output

```
3 Simple Habits to Stay Motivated Every Day

• Start with one small task  
• Track your tiny progress  
• Remove distractions for 30 minutes  

Try these today—your future self will thank you!

#motivation #selfgrowth #productivity
Character count: 241
```

Tech Stack

| Component       | Technology Used      |
| --------------- | -------------------- |
| Transcription   | Groq Whisper V3      |
| Text Generation | LLaMA 3.1 8B Instant |
| Framework       | python-telegram-bot  |
| Language        | Python 3.10+         |

Security

* No data stored on the server
* Tokens stored in environment variables
* Virtual environment excluded via `.gitignore`
* No real LinkedIn posting (simulated only)

Known Limitations

* Very unclear audio may reduce transcription accuracy
* Depends on internet speed
* Long audio may take slightly longer to process

Author
Kanishka Bisht
AI • Automation • Python • Telegram Bots
GitHub: *github.com/Kanishka-Bisht04*

Support

If this project helped you, please star ⭐ the repository                                !
