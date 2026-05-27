import shelve
import random

def add_to_flashcards():
    while True:
        term = input("Enter the term of the card you want to add: ").lower()
        definition = input("Enter the definition of the term: ")
        with shelve.open('flashcards') as flashcards:
            flashcards[term] = definition
        done = input("Do you want to add another card (yes/no)? ")
        if done.lower() != 'yes':
            break

def remove_from_flashcards():
    while True:
        term = input("Enter the term of the card you want to remove: ").lower()
        with shelve.open('flashcards') as flashcards:
            if term in flashcards:
                del flashcards[term]
                print(f"Card with term '{term}' has been removed.")
            else:
                print(f"No card found with term '{term}'.")
                print(f"Current terms: {list(flashcards.keys())}")
        done = input("Do you want to remove another card (yes/no)? ")
        if done.lower() != 'yes':
            break

def test_flashcards(flashcards):
    while True:
        definitions = list(flashcards.values())
        random.shuffle(definitions)
        terms = list(flashcards.keys())
        correct_count = 0
        num = int(input(f"How many flashcards do you want to be tested on (1-{len(definitions)})? "))
        if num < 1 or num > len(definitions):
            print(f"Please enter a number between 1 and {len(definitions)}.")
            continue
        for definition in definitions[:num]:
            answer = input(f"What term matches the definition '{definition}'? ").lower()
            for term in terms:
                if flashcards[term] == definition:
                     correct_term = term
            if answer == correct_term:
                print("Correct!")
                correct_count += 1
            else:
               print(f"Wrong! The correct term is '{correct_term}'.")
        print(f"Out of the {num} flashcards tested, you got {correct_count} correct.")
        done = input("Do you want to test yourself again (yes/no)? ")
        if done.lower() != 'yes':
            break

def view_flashcards():
    with shelve.open('flashcards') as flashcards:
        if flashcards:
            print("Current flashcards:")
            for term, definition in flashcards.items():
                print(f"{term}: {definition}")
        else:
            print("No flashcards found. Please add some first.")

def main():
    while True:
        choice = input("Do you want to add flashcards, remove flashcards, view current flashcards, or test yourself (add/remove/view/test)? ")
        if choice.lower() == 'add':
            add_to_flashcards()
        elif choice.lower() == 'remove':
            remove_from_flashcards()
        elif choice.lower() == 'view':
            view_flashcards()
        elif choice.lower() == 'test':
            with shelve.open('flashcards') as flashcards:
                if flashcards:
                   test_flashcards(flashcards)
                else:
                    print("No flashcards found. Please add some first.")
        else:
            print("Invalid choice.")
        more = input("Is there anything else you want to do (yes/no)? ")
        if more.lower() != 'yes':
            break

main()