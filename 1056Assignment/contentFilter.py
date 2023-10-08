class ContentFilter:
    def __init__(self, banned_word):
        self.banned_words = banned_word

    def filter_content(self, content):
        for word in self.banned_words:
            content = content.replace(word, '*' * len(word))
        return content


# create
banned_words = ["bad", "hate", "spam"]
filters = ContentFilter(banned_words)

# filtering
text = "This is a bad example with hate speech and spam content."
filtered_text = filters.filter_content(text)

# test
print("Original Text:")
print(text)
print("Filtered Text:")
print(filtered_text)
