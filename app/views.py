from app.models import Book


def show_book():
    return {"book": Book()}