from speech import listen
from translator import translate_text,translate_summary
from summarization import summarize

#while True:
input = listen()
translate_text(input)

summary = summarize()
translate_summary(summary)
