from app.models.book_model import Book


BOOKS = [
	Book(1, "Harry Potter", "JK Rowling"),
	Book(2, "ça", "Stephen King"),
	Book(3, "La Bible", "Dieu")
]

def get_all() -> list[Book]:
	"""Retourne une liste complète des livres"""
	return BOOKS

def get_book_by_id(book_id : int) -> Book | None:
	"""Retourne un livre par son identifiant, sinon None."""
	return next((b for b in BOOKS if b.id == book_id), None)