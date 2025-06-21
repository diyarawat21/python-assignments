import csv
import os

def load_scores(path: str) -> list[tuple[str, int]]:
    records = []
    if not os.path.exists(path):
        print(f"File '{path}' not found. Starting with empty scores.")
        return records
    try:
        with open(path, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 2:
                    print(f"Skipping bad row: {row}")
                    continue
                name, score_str = row
                try:
                    score = int(score_str)
                    records.append((name, score))
                except ValueError:
                    print(f"Skipping row with bad score: {row}")
    except Exception as e:
        print(f"Error reading file: {e}")
    return records

def add_score(records: list[tuple[str, int]], name: str, score: int) -> None:
    records.append((name, score))

def save_scores(path: str, records: list[tuple[str, int]]) -> None:
    try:
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            for name, score in records:
                writer.writerow([name, score])
    except Exception as e:
        print(f"Error saving scores: {e}")

def top_n(records: list[tuple[str, int]], n: int) -> list[tuple[str, int]]:
    sorted_records = sorted(records, key=lambda x: x[1], reverse=True)
    return sorted_records[:n]

def menu():
    print("\n--- Score Keeper ---")
    print("1. Show Top N Scores")
    print("2. Add New Score")
    print("3. Exit")

def main():
    path = "scores.csv"
    records = load_scores(path)

    while True:
        menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number (1-3).")
            continue

        if choice == 1:
            try:
                n = int(input("How many top scores would you like to see? "))
                if n <= 0:
                    print("Please enter a positive number.")
                    continue
                top_scores = top_n(records, n)
                if top_scores:
                    print("\nTop Scores:")
                    for name, score in top_scores:
                        print(f"{name}: {score}")
                else:
                    print("No scores to display.")
            except ValueError:
                print("Please enter a valid number for N.")
        elif choice == 2:
            name = input("Enter name: ").strip()
            try:
                score = int(input("Enter score (integer): "))
                add_score(records, name, score)
                save_scores(path, records)
                print(f"Added {name} with score {score}.")
            except ValueError:
                print("Score must be a number.")
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
