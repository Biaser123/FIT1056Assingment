from contentFilter import ContentFilter

# create
banned_words = ["bad", "hate", "spam"]
filters = ContentFilter(banned_words)

# filtering
text = "This is a bad example with hate speech and spam content."
text2 = "Hello world!"
filtered_text = filters.filter_content(text)
filtered_text2 = filters.filter_content(text2)

assert filtered_text == "This is a *** example with **** speech and *** content."
assert filtered_text2 == "Hello world!"
