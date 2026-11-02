def calculate_average(scores):
    """Return the average of nonnegative integer scores.

    Return None for an empty list.
    Raise ValueError for invalid input.
    """
    if not isinstance(scores, list):
        raise ValueError("Scores must be provided as a list.")

    if not scores:
        return None

    for score in scores:
        if type(score) is not int or score < 0:
            raise ValueError(
                "Every score must be a nonnegative integer."
            )

    return sum(scores) / len(scores)

if __name__ == "__main__":
    print(calculate_average([10, 20, 30]))
    print(calculate_average([5, 15]))
    print(calculate_average([]))