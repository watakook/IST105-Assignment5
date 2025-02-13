import cgi
import math
import random

form = cgi.FieldStorage()
number = int(form.getvalue("number", 0))
text = form.getvalue("text", "")

if number % 2 == 0:
    number_result = f"The number {number} is even. Its square root is {math.sqrt(number):.2f}."
else:
    number_result = f"The number {number} is odd. Its cube is {number ** 3}."

binary_text = " ".join(format(ord(char), "08b") for char in text)
vowel_count = sum(1 for char in text if char.lower() in "abcdefghijklmnopqrstuvwxyz" and char.lower() in "abcdefghijklmnopqrstuvwxyz")

secret_number = random.randint(1, 100)
attempts = []
guess = random.randint(1, 100)

for i in range(5):
    if guess == secret_number:
        attempts.append(f"Attempt {i+1}: {guess} (Correct!)")
        break
    elif guess > secret_number:
        attempts.append(f"Attempt {i+1}: {guess} (Too high!)")
    else:
        attempts.append(f"Attempt {i+1}: {guess} (Too low!)")
    guess = random.randint(1, 100)

print("Content-type: text/html\n")
print("<html><body>")
print(f"<h2>Number Puzzle:</h2><p>{number_result}</p>")
print(f"<h2>Text Puzzle:</h2><p>Binary: {binary_text}</p><p>Vowel Count: {vowel_count}</p>")
print(f"<h2>Treasure Hunt:</h2><p>Secret number: {secret_number}</p>")
print("<p>" + "<br>".join(attempts) + "</p>")
print("</body></html>")