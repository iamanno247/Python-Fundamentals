text = input()

# TODO: build a new string whose first and last characters are swapped,
# with every character between them left where it is.
# Remember that a very short string has nothing to swap.

clean_text = text.strip(" ")

if len(clean_text) == 1:
    result = clean_text
else:
    result = clean_text[-1] + clean_text[1:-1] + clean_text[0]
print(result)