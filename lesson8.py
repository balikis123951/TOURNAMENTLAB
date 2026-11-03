def sort_standings(teams):
    return sorted(
        teams,
        key=lambda team: (
            -team["points"],
            -team["goal_difference"],
            -team["goals_for"],
            team["name"].casefold(),
        )
    )
