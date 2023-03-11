from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import torch
from langdetect import detect
from translation import translate


device = 'cuda' if torch.cuda.is_available() else 'cpu'
mname = "facebook/blenderbot-3B"
model = BlenderbotForConditionalGeneration.from_pretrained(mname).to(device)
tokenizer = BlenderbotTokenizer.from_pretrained(mname)

while True:
    UTTERANCE = input('UTTERANCE: ')
    # If Korean text, translate to English 
    if detect(UTTERANCE) == 'ko':
        UTTERANCE = translate(UTTERANCE)
    inputs = tokenizer([UTTERANCE], return_tensors="pt").to(device)
    reply_ids = model.generate(**inputs, max_length=1024)
    print('Blenderbot:', tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0])