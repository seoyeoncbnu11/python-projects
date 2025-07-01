import googletrans

translator = googletrans.Translator()

str1 = "행복하세요."
result1 = translator.translate(str1, dest="en", src="auto")
print(f"행복하세요. => {result1.text}")

str2 = "I am happy"
result2 = translator.translate(str2, dest="ko", src="en")
print(f"I am happy => {result2.text}")

# lang = googletrans.LANGUAGES
# print(lang)

read_file_path = "./04-auto-projects/영어파일.txt"
write_file_path = "./04-auto-projects/한글파일.txt"

with open(read_file_path, "r") as f:
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest="ko")
    print(result1.text)

    with open(write_file_path, "a", encoding="UTF8") as f:
        f.write(result1.text + "\n")
