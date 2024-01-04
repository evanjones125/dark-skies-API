from main import find_dark_windows
import unittest


class AstronomyAPITests(unittest.TestCase):
    def test_dark_window_between_sunset_and_moonrise1(self):
        result = find_dark_windows("18:00", "23:00", "08:00", "06:05", "23:50", "8:50")
        self.assertEqual(result, [("6:00pm", "11:00pm")])

    def test_dark_window_between_sunset_and_moonrise2(self):
        result = find_dark_windows("17:19", "05:33", "16:08", "07:25", "06:44", "16:44")
        self.assertEqual(result, [("5:19pm", "6:44am")])

    def test_dark_window_between_moonset1_and_moonrise2(self):
        result = find_dark_windows("17:19", "07:33", "18:08", "07:25", "06:44", "16:44")
        self.assertEqual(result, [("6:08pm", "6:44am")])

    def test_dark_window_between_moonset1_and_sunrise(self):
        result = find_dark_windows("17:19", "07:33", "18:08", "07:25", "07:44", "17:44")
        self.assertEqual(result, [("6:08pm", "7:25am")])

    def test_dark_window_between_moonset2_and_sunrise(self):
        result = find_dark_windows("17:19", "16:08", "05:33", "07:25", "16:44", "06:44")
        self.assertEqual(result, [("6:44am", "7:25am")])

    def test_no_dark_window(self):
        result = find_dark_windows("18:00", "17:00", "06:10", "06:05", "07:00", "19:20")
        self.assertEqual(result, [])

    def test_complete_darkness(self):
        result = find_dark_windows("18:00", "08:05", "17:55", "06:05", "07:00", "17:20")
        self.assertEqual(result, [("6:00pm", "6:05am")])

    def test_multiple_windows(self):
        result = find_dark_windows("17:30", "18:00", "07:10", "07:40", "15:45", "06:45")
        self.assertEqual(result, [("5:30pm", "6:00pm"), ("6:45am", "7:40am")])

    def test_no_moonrise1(self):
        result = find_dark_windows("17:30", "-:-", "12:57", "07:40", "00:10", "13:19")
        self.assertEqual(result, [("5:30pm", "12:10am")])

    def test_no_moonrise2(self):
        result = find_dark_windows("17:30", "23:11", "12:32", "07:40", "-:-", "12:57")
        self.assertEqual(result, [("5:30pm", "11:11pm")])

    def test_no_moonset1(self):
        result = find_dark_windows("17:30", "12:43", "-:-", "07:40", "13:08", "00:59")
        self.assertEqual(result, [("12:59am", "7:40am")])

    def test_no_moonset2(self):
        result = find_dark_windows("17:30", "12:16", "23:50", "07:40", "12:43", "-:-")
        self.assertEqual(result, [("11:50pm", "7:40am")])


if __name__ == "__main__":
    unittest.main()
