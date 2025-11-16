import os
import logging
import asyncio
from io import BytesIO
from groq import Groq
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters

# Load environment variables
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")  # FREE Groq API

# Groq client
groq_client = Groq(api_key=GROQ_API_KEY)

logging.basicConfig(level=logging.INFO)


# -------------------- TRANSCRIBE AUDIO --------------------
async def transcribe(audio_bytes):
    bio = BytesIO(audio_bytes)
    bio.name = "audio.ogg"

    response = groq_client.audio.transcriptions.create(
        model="whisper-large-v3",
        file=(bio.name, bio, "audio/ogg")
    )

    return response.text


# -------------------- GENERATE LINKEDIN POST --------------------
async def generate_post(topic):
    prompt = f"""
Write a LinkedIn-style post (under 1300 characters) about:

"{topic}"

Include:
- A strong hook
- 3–4 short points in the body
- A simple CTA
- 3–5 non-spammy hashtags
- At the END add this: Character count: <count>

Write in a friendly, clear LinkedIn tone.
"""

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )

    post = response.choices[0].message.content

    # Add character count automatically
    count = len(post)
    post = post.replace("<count>", str(count))

    return post


# -------------------- /start --------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Send a voice note with your topic for a LinkedIn post.")


# -------------------- HANDLE VOICE NOTE --------------------
async def voice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    await msg.reply_text("Transcribing your voice...")

    # Download voice file
    file = await context.bot.get_file(msg.voice.file_id)
    bio = BytesIO()
    await file.download_to_memory(out=bio)

    # Transcription
    text = await transcribe(bio.getvalue())

    if not text.strip():
        await msg.reply_text("I couldn’t understand your voice. Please try again.")
        return

    await msg.reply_text("Creating your LinkedIn draft...")

    # Generate LinkedIn Post
    post = await generate_post(text)

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Yes", callback_data=f"yes|||{text}"),
            InlineKeyboardButton("Regenerate", callback_data=f"regen|||{text}"),
            InlineKeyboardButton("No", callback_data="no")
        ]
    ])

    await msg.reply_text(post, reply_markup=keyboard)


# -------------------- HANDLE BUTTONS --------------------
async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("yes"):
        await query.edit_message_text("✅ Marked as Posted (simulated).")
    elif data.startswith("regen"):
        topic = data.split("|||")[1]
        new_post = await generate_post(topic)
        await query.edit_message_text(new_post)
    else:
        await query.edit_message_text("Draft discarded.")


# -------------------- MAIN --------------------
def main():
    if not TELEGRAM_TOKEN:
        print("❌ ERROR: TELEGRAM_TOKEN not set")
        return

    if not GROQ_API_KEY:
        print("❌ ERROR: GROQ_API_KEY not set")
        return

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.VOICE, voice_handler))
    app.add_handler(CallbackQueryHandler(callback_handler))

    print("Bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()
