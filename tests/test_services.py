import unittest
from app.services import WordService


class TestWordService(unittest.TestCase):
    def setUp(self):
        self.service = WordService()

    def test_count_vowels(self):
        # Arrange
        words = ["batman", "robin", "coringa"]
        expected = {"batman": 2, "robin": 2, "coringa": 3}

        # Act
        result = self.service.count_vowels(words)

        # Assert
        self.assertEqual(result, expected)

    def test_count_vowels_empty_list(self):
        # Arrange
        words = []
        expected = {}

        # Act
        result = self.service.count_vowels(words)

        # Assert
        self.assertEqual(result, expected)

    def test_count_vowels_uppercase(self):
        # Arrange
        words = ["BATMAN", "ROBIN", "CORINGA"]
        expected = {"BATMAN": 2, "ROBIN": 2, "CORINGA": 3}

        # Act
        result = self.service.count_vowels(words)

        # Assert
        self.assertEqual(result, expected)

    def test_count_vowels_in_words_with_no_vowels(self):
        # Arrange
        words = ["xyz", "123", "bcdfgh"]
        expected = {"xyz": 0, "123": 0, "bcdfgh": 0}

        # Act
        result = self.service.count_vowels(words)

        # Assert
        self.assertEqual(result, expected)

    def test_count_vowels_mixed_case(self):
        # Arrange
        words = ["BaTmAn", "rObIn", "CoRiNgA"]
        expected = {"BaTmAn": 2, "rObIn": 2, "CoRiNgA": 3}
        # Act
        result = self.service.count_vowels(words)
        # Assert
        self.assertEqual(result, expected)

    def test_sort_words_asc(self):
        # Arrange
        words = ["batman", "robin", "coringa"]
        order = "asc"
        expected = ["batman", "coringa", "robin"]

        # Act
        result = self.service.sort_words(words, order)

        # Assert
        self.assertEqual(result, expected)

    def test_sort_words_desc(self):
        # Arrange
        words = ["batman", "robin", "coringa"]
        order = "desc"
        expected = ["robin", "coringa", "batman"]

        # Act
        result = self.service.sort_words(words, order)

        # Assert
        self.assertEqual(result, expected)

    def test_sort_words_empty_list(self):
        # Arrange
        words = []
        order = "asc"
        expected = []

        # Act
        result = self.service.sort_words(words, order)

        # Assert
        self.assertEqual(result, expected)

    def test_sort_words_case_insensitive(self):
        # Arrange
        words = ["Banana", "apple", "Cherry"]
        order = "asc"
        expected = ["apple", "Banana", "Cherry"]

        # Act
        result = self.service.sort_words(words, order)

        # Assert
        self.assertEqual(result, expected)

    def test_sort_words_duplicate_words(self):
        # Arrange
        words = ["batman", "robin", "batman", "coringa", "robin"]
        order = "asc"
        expected = ["batman", "batman", "coringa", "robin", "robin"]

        # Act
        result = self.service.sort_words(words, order)

        # Assert
        self.assertEqual(result, expected)
