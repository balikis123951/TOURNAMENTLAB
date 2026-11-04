import unittest
from lesson8 import sort_standings


class TestSortStandings(unittest.TestCase):

    def setUp(self):
        self.teams = [
            {"name": "Falcons", "points": 9, "goal_difference": 4, "goals_for": 10},
            {"name": "Eagles", "points": 12, "goal_difference": 2, "goals_for": 8},
            {"name": "bears", "points": 9, "goal_difference": 4, "goals_for": 12},
            {"name": "Cheetahs", "points": 9, "goal_difference": 4, "goals_for": 12},
        ]

    def test_points_have_highest_priority(self):
        result = sort_standings(self.teams)
        self.assertEqual(result[0]["name"], "Eagles")

    def test_goals_for_breaks_a_tie(self):
        result = sort_standings(self.teams)
        names = [team["name"] for team in result]
        self.assertLess(names.index("bears"), names.index("Falcons"))

    def test_alphabetical_order_breaks_remaining_tie(self):
        result = sort_standings(self.teams)
        names = [team["name"] for team in result]
        self.assertLess(names.index("bears"), names.index("Cheetahs"))

    def test_original_list_is_not_reordered(self):
        original_names = [team["name"] for team in self.teams]
        sort_standings(self.teams)
        self.assertEqual(
            [team["name"] for team in self.teams],
            original_names,
        )


if __name__ == "__main__":
    unittest.main()
