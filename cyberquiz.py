print(" Welcome to the Cybersecurity Quiz!")
print("Answer the following questions to test your cyber awareness.\n")

score = 0

# Question 1
print("1 What does 'https' stand for?")
answer = input("Your answer: ").strip().lower()

if "secure" in answer and "http" in answer:
    print(" Correct!\n")
    score += 1
else:
    print(" Incorrect. It stands for Hypertext Transfer Protocol Secure.\n")

# Question 2
print("2 What is phishing?")
answer = input("Your answer: ").strip().lower()

if "fake" in answer or "scam" in answer or "steal" in answer:
    print(" Correct!\n")
    score += 1
else:
    print(" Incorrect. It's a fake message used to steal info.\n")

# Question 3
print("3 What is a strong password?")
answer = input("Your answer: ").strip().lower()

if "uppercase" in answer or "special" in answer or "numbers" in answer:
    print(" Correct!\n")
    score += 1
else:
    print(" Incorrect. A strong password includes symbols, numbers, and both upper/lowercase letters.\n")

# Final Score
print(f" You scored {score}/3")

if score == 3:
    print(" Excellent! You're a cyber star.")
elif score == 2:
    print(" Good job! You know your basics.")
else:
    print(" Keep learning — cybersecurity is important!")

