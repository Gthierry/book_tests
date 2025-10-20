from app.services.book_service import get_all, get_book_by_id
from flask import jsonify


def get_books():
	"""EndPoint : GET /api/books"""
	books = get_all()
	payload = [book.to_dict() for book in books]
	return jsonify(payload), 200

def get_book(id : int):
	"""EndPoint : GET /api/book/<id>"""
	book = get_book_by_id(id)
	if (book):
		return jsonify(book.to_dict()), 200
	return jsonify({"error" : "Livre non trouvé"}), 404