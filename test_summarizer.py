from transformers import T5ForConditionalGeneration, T5Tokenizer


model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')

def summary(text):
    tokens = tokenizer.encode(text, 
                            max_length=256,
                            return_tensors='pt',
                            pad_to_max_length=True)

    gen_tokens = model.generate(tokens, max_length = 256)
    return tokenizer.decode(gen_tokens.tolist()[0])


if __name__ == "__main__":
    text = """
    Despite the coronavirus pandemic, which has put off a full national security 
    council (NSC) meeting on the Open Skies Treaty (OST), the secretary of defence, 
    Mark Esper, and secretary of state, Mike Pompeo, have agreed to proceed with a US 
    exit, according to two sources familiar with administration planning.
    US arms control office critically understaffed under Trump, experts say
    Read more

    A statement of intent is expected soon, with a formal notification of 
    withdrawal issued a few months later, possibly at the end of the fiscal year in 
    September. The US would cease to be a party to the treaty six months after that, 
    so if a new president were elected in November, the decision could be reversed 
    before taking effect."""
    print(summary(text))