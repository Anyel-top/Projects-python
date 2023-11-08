import spacy

# Load spaCy's natural language processing model
nlp = spacy.load("en_core_web_sm")

def sum_numbers(text):
    # Parse the input text using spaCy
    doc = nlp(text)
    total = 0

    # Iterate through the parsed tokens
    for token in doc:
        if token.is_digit:
            number = float(token.text)
            total += number

    return total

if __name__ == "__main__":
    while True:
        input_text = input("Enter the numbers you want to add (or 'exit' to quit): ")
        
        if input_text.lower() == "exit":
            break

        result = sum_numbers(input_text)
        print(f"Result: {result}")
