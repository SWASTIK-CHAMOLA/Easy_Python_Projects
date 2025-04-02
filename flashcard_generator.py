import json     # importing json file for storing and recording data
import random   # to randomize the flashcards generated
FLASHCARD_FILE = "flashcards.json"

with open(FLASHCARD_FILE, "r") as file:
    flashcards = json.load(file) if file.read() else {}

while True:
    choice = input("\n1. Add Flashcard\n2. Quiz Yourself\n3. Exit\nChoose an option: ")
    if choice == "1":
        flashcards[input("Enter the question: ")] = input("Enter the answer: ")
        with open(FLASHCARD_FILE, "w") as file:
            json.dump(flashcards, file, indent=4)
        print("Flashcard added!\n")
    elif choice == "2":
        if not flashcards:
            print("No flashcards found!\n")
            continue
        
        score = 0
        for question in random.sample(flashcards.keys(), len(flashcards)):
            user_answer = input(f"{question}: ").strip()
            correct_answer = flashcards[question].strip()

            if user_answer == correct_answer:  # Case-sensitive comparison
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Answer: {correct_answer}\n")
        
        print(f"Quiz finished! Score: {score}/{len(flashcards)}\n")
    
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
