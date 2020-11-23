import os
import shutil



lib = []

class Books:
    
    def __init__(self, book_name, ID, chapters):
        self.book_name = book_name
        self.ID = ID
        self.chapters = chapters
   
    def add_chapters(self, book_name, chapter_name):#добавляет главы
            book = open(book_name + '/' + chapter_name,'w', encoding='utf-8')
            book.close()

    def add_book(self, book_name, ID, chapters):#добавляет книгу
        
        path = r'C:\Users\Nick\Desktop\python'
        if book_name in path:
            print('Такая книга уже есть, но вы можете добавить к ней глав, вызвав функцию add_chapters')
        else:
            lib.append(book_name)
            lib.append(ID)
            lib.append(chapters)
            os.mkdir(book_name)
            book = open(book_name + '/info.txt', 'w', encoding='utf-8')
            book.write(book_name + '\n')
            book.write(str(ID) + '\n')
            book.write(str(chapters))
            book.close()
        
    def delete_book(self, book_name):#удаляет книгу
        shutil.rmtree(book_name)
        
    def change_book_name(self, book_name, new_book_name):#меняет название книги
        os.rename(book_name, new_book_name)

    def print_all_books(self):#показывает информацию обо всех книгах
            print(lib)

class Chapters(Books):
    
    def __init__(self, book_name, chapter_name):
        self.book_name =  book_name
        self.chapter_name = chapter_name


    def text_in_chapter(self, book_name, chapter_name):#Перезаписывает главу
        content = input(' ')
        text = open(book_name + '/' + chapter_name, 'w', encoding='utf-8')
        text.write(content)
        text.close()

        
    def add_chapters(self, book_name, chapter_name):#добавляет главы
            book = open(book_name + '/' + chapter_name,'w', encoding='utf-8')
            book.close()
    
    def change_chapter_name(self, book_name, chapter_name, new_chapter_name):#изменяет название главы
            os.rename(book_name + '/' + chapter_name, new_chapter_name)
            
    def delete_chapter(self, book_name, chapter_name):#удаляет главу
            os.remove(book_name + '/' + chapter_name)

chapter = Chapters('Мартин Иден', "Глава первая")
book = Books('100 лет Одиночества', 2, 50)

book.add_book('Великий Гэтсби', 2, 18)
