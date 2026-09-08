import unittest

from src.backend.database import initial_activities


class InitialActivitiesTest(unittest.TestCase):
    def test_manga_maniacs_activity_is_seeded(self):
        activity = initial_activities["Manga Maniacs"]

        self.assertEqual(
            activity["description"],
            "Dive into action-packed worlds, unforgettable heroes, and epic adventures inspired by Japanese Manga.",
        )
        self.assertEqual(activity["schedule"], "Tuesdays, 5:00 PM")
        self.assertEqual(activity["schedule_details"]["days"], ["Tuesday"])
        self.assertEqual(activity["schedule_details"]["start_time"], "17:00")
        self.assertEqual(activity["max_participants"], 25)
        self.assertEqual(activity["participants"], [])


if __name__ == "__main__":
    unittest.main()
