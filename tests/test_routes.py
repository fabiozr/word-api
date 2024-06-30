import unittest
from unittest.mock import patch
from app.routes import register_routes
from flask import Flask


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        register_routes(self.app)
        self.client = self.app.test_client()

    def test_vowel_count_route(self):
        # Arrange
        data = {"words": ["batman", "robin", "coringa"]}
        expected = {"batman": 2, "robin": 2, "coringa": 3}

        # Act
        response = self.client.post("/vowel_count", json=data)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_vowel_count_route_invalid_input(self):
        # Arrange
        data = {"words": ["batman", 123, "coringa"]}

        # Act
        response = self.client.post("/vowel_count", json=data)

        # Assert
        self.assertEqual(response.status_code, 400)

    def test_vowel_count_route_empty_input(self):
        # Arrange
        data = {}

        # Act
        response = self.client.post("/vowel_count", json=data)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {})

    def test_sort_route_asc(self):
        # Arrange
        data = {"words": ["batman", "robin", "coringa"], "order": "asc"}
        expected = ["batman", "coringa", "robin"]

        # Act
        response = self.client.post("/sort", json=data)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_sort_route_desc(self):
        # Arrange
        data = {"words": ["batman", "robin", "coringa"], "order": "desc"}
        expected = ["robin", "coringa", "batman"]

        # Act
        response = self.client.post("/sort", json=data)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_sort_route_invalid_order(self):
        # Arrange
        data = {"words": ["batman", "robin", "coringa"], "order": "invalid"}

        # Act
        response = self.client.post("/sort", json=data)

        # Assert
        self.assertEqual(response.status_code, 400)

    def test_sort_route_empty_input(self):
        # Arrange
        data = {}

        # Act
        response = self.client.post("/sort", json=data)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_method_not_allowed_route(self):
        # Act
        response = self.client.get("/vowel_count")

        # Assert
        self.assertEqual(response.status_code, 405)

    def test_not_found_route(self):
        # Act
        response = self.client.get("/invalid_route")

        # Assert
        self.assertEqual(response.status_code, 404)

    def test_unsupported_media_type_route(self):
        # Act
        response = self.client.post(
            "/vowel_count", data="invalid", content_type="text/plain"
        )

        # Assert
        self.assertEqual(response.status_code, 415)
