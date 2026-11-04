def compute_standings(teams, matches):
    standings = {}

    # Step 1: Initialize statistics for every team.
    for team in teams:
        standings[team] = {
            "played": 0,
            "wins": 0,
            "draws": 0,
            "losses": 0,
            "goals_for": 0,
            "goals_against": 0,
            "goal_difference": 0,
            "points": 0,
        }

    # Step 2: Process every completed match.
    for match in matches:
        home = match["home"]
        away = match["away"]
        home_score = match["home_score"]
        away_score = match["away_score"]

        home_stats = standings[home]
        away_stats = standings[away]

        # Update matches played.
        home_stats["played"] += 1
        away_stats["played"] += 1

        # Update goals scored and conceded.
        home_stats["goals_for"] += home_score
        home_stats["goals_against"] += away_score

        away_stats["goals_for"] += away_score
        away_stats["goals_against"] += home_score

        # Calculate wins, draws, losses, and points.
        if home_score > away_score:
            home_stats["wins"] += 1
            away_stats["losses"] += 1
            home_stats["points"] += 3

        elif home_score < away_score:
            away_stats["wins"] += 1
            home_stats["losses"] += 1
            away_stats["points"] += 3

        else:
            home_stats["draws"] += 1
            away_stats["draws"] += 1
            home_stats["points"] += 1
            away_stats["points"] += 1

    # Step 3: Calculate goal difference.
    for stats in standings.values():
        stats["goal_difference"] = (
            stats["goals_for"] - stats["goals_against"]
        )

    return standings


if __name__ == "__main__":
    teams = ["Falcons", "Eagles", "Bears"]

    matches = [
        {
            "home": "Falcons",
            "away": "Eagles",
            "home_score": 2,
            "away_score": 0,
        },
        {
            "home": "Falcons",
            "away": "Bears",
            "home_score": 1,
            "away_score": 1,
        },
        {
            "home": "Eagles",
            "away": "Bears",
            "home_score": 3,
            "away_score": 1,
        },
    ]

    standings = compute_standings(teams, matches)

    for team, stats in standings.items():
        print(f"\n{team}")
        for statistic, value in stats.items():
            print(f"  {statistic}: {value}")