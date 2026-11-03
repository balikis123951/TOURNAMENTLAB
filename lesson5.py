def validate_score(score):
    if type(score) is not int:
        raise ValueError("Score must be a whole integer.")

    if score < 0:
        raise ValueError("Score cannot be negative.")

    return score


def get_score(prompt):
    raw_value = input(prompt).strip()

    try:
        score = int(raw_value)
    except ValueError:
        raise ValueError("Please enter a valid whole number.")

    return validate_score(score)


def main():
    try:
        team_a_score = get_score("Enter Team A's score: ")
        team_b_score = get_score("Enter Team B's score: ")

        print(f"Final score: {team_a_score} - {team_b_score}")

    except ValueError as error:
        print(f"Invalid score: {error}")


if __name__ == "__main__":
    main()