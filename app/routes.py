from flask import Flask, request, jsonify, abort
from .services import WordService


def register_routes(app: Flask):
    word_service = WordService()

    def validate_words_input(words):
        if isinstance(words, list) and all(isinstance(word, str) for word in words):
            return words
        else:
            abort(400, "Invalid input: 'words' must be a list of strings")

    def validate_order_input(order):
        if isinstance(order, str) and order.lower() in ["asc", "desc"]:
            return order
        else:
            abort(400, "Invalid order: must be 'asc' or 'desc")

    @app.route("/vowel_count", methods=["POST"])
    def vowel_count():
        data = request.get_json()
        words = validate_words_input(data.get("words", []))
        response = word_service.count_vowels(words)
        return jsonify(response)

    @app.route("/sort", methods=["POST"])
    def sort():
        data = request.get_json()
        words = validate_words_input(data.get("words", []))
        order = validate_order_input(data.get("order", "asc"))
        response = word_service.sort_words(words, order)
        return jsonify(response)
