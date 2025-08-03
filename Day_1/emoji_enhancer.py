emojis = {
  "love": "❤️",
  "happy": "😄",
  "code": "💻",
  "coffee": "☕",
  "music": "🎧",
  "food": "🍉",
}

msg = input("Enter your message: ").strip()

updated_words = []

for word in msg.split():
  cleaned = word.lower().strip('.,!?')
  emoji = emojis.get(cleaned, '')
  if emoji: 
    updated_words.append(f"{word} {emoji}")
  else:
    updated_words.append(word)

updated_message = ' '.join(updated_words)
print('\nEnhanced Message')
print(updated_message)