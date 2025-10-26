class Book:
    def __init__(self, udk, author, title, year, quantity):
        self.udk = udk
        self.author = author
        self.title = title
        self.year = year
        self.quantity = quantity
        self.left = None
        self.right = None

library_root = None

def add_book_linear(udk, author, title, year, quantity):
    global library_root
    new_book = Book(udk, author, title, year, quantity)
    
    if library_root is None:
        library_root = new_book
        print("Книга добавлена!")
        return
    
    current = library_root
    while True:
        if udk < current.udk:
            if current.left is None:
                current.left = new_book
                print("Книга добавлена!")
                return
            else:
                current = current.left
        else:
            if current.right is None:
                current.right = new_book
                print("Книга добавлена!")
                return
            else:
                current = current.right

def remove_book_linear(udk):
    global library_root
    library_root = remove_node_linear(library_root, udk)

def remove_node_linear(node, udk):
    if node is None:
        print("Книга не найдена!")
        return None
    
    if udk < node.udk:
        node.left = remove_node_linear(node.left, udk)
    elif udk > node.udk:
        node.right = remove_node_linear(node.right, udk)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        
        min_node = find_min_linear(node.right)
        node.udk = min_node.udk
        node.author = min_node.author
        node.title = min_node.title
        node.year = min_node.year
        node.quantity = min_node.quantity
        node.right = remove_node_linear(node.right, min_node.udk)
    
    return node

def find_min_linear(node):
    while node.left is not None:
        node = node.left
    return node

def find_book_linear(udk):
    return search_node_linear(library_root, udk)

def search_node_linear(node, udk):
    if node is None or node.udk == udk:
        return node
    
    if udk < node.udk:
        return search_node_linear(node.left, udk)
    else:
        return search_node_linear(node.right, udk)

def display_books_linear():
    books = collect_books_linear(library_root)
    books_sorted = sorted(books, key=lambda x: x.year)
    
    for book in books_sorted:
        print(f"УДК: {book.udk}, Автор: {book.author}, Название: {book.title}, Год: {book.year}, Кол-во: {book.quantity}")

def collect_books_linear(node):
    books = []
    if node:
        books.append(node)
        books.extend(collect_books_linear(node.left))
        books.extend(collect_books_linear(node.right))
    return books

def main_linear():
    global library_root
    
    add_book_linear("001.1", "Иванов И.И.", "Основы программирования", 2020, 5)
    add_book_linear("002.2", "Петров П.П.", "Алгоритмы", 2019, 3)
    add_book_linear("003.3", "Сидоров С.С.", "Базы данных", 2021, 4)
    
    print("Все книги:")
    display_books_linear()
    
    book = find_book_linear("002.2")
    if book:
        print(f"\nНайдена: {book.title}")
    
    remove_book_linear("001.1")
    print("\nПосле удаления:")
    display_books_linear()

if __name__ == "__main__":
    main_linear()