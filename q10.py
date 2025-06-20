input_sentence = "Hello, World! Welcome to Nirvana."
words = input_sentence.split()

reversed_words = words[::-1]

output_sentence = " ".join(reversed_words)
print("Output after reverse =", output_sentence)
