title = input()

# TODO: keep only letters, digits and spaces, lowercase them,
# and join the words with single hyphens.

clean_title = ""

for letter in title:
    if letter.isalnum() or letter == " ":
        clean_title += letter
        continue
    else:
        continue

clean_title = clean_title.lower().strip()
    
clean_title = clean_title.split()

clean_title = "-".join(clean_title)

print(clean_title)