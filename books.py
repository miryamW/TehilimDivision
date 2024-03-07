import itertools as it
from manage import Manage
from dividing import Dividing


class Books(Dividing):
    """מחלקה שאחראית על חלוקה לפי ספרים בתהילים"""
    books = ['א', 'ב', 'ג', 'ד', 'ה']

    def __init__(self, name):
        """פונקציה בונה מאתחלת את הנתונים לפי הנתונים בקובץ המתאים"""
        Dividing.__init__(self, name)
        file = open(Manage.dividers[name], 'r')
        self.current_book = file.readlines()[2].split(':')[1].split('\n')[0]
        file.close()

    def divide_books(self):
        """גנרטור שעובר על הספרים שבתהילים, כשמגיע לספר החמישי חוזר להתחלה ומעדכן את כמות הספרים שנגמרו"""
        for i in it.count():
            while self.books.index(self.current_book) < 29:
                temp = self.current_book
                self.current_book = self.books[self.books.index(self.current_book) + 1]
                yield temp
            self.current_book = self.books[0]
            self.count_books += 1
            yield self.current_book

    def get_book(self):
        """פונקציה שמבצעת בפועל את חלוקת הספרים על פי קלט מהמשתמש וכן מפרטת למשתמש את הפרקים שעליו לאמר"""
        try:
            dividing_books = self.divide_books()
            ifMore = 'yes'
            while ifMore == 'yes':
                self.num_books()
                this_book = next(dividing_books)
                print(f"the book you recive:{this_book}")
                print_chapters = input('enter yes if you want to see which chapters are include at the book you '
                                       'reseived')
                if ifMore != 'yes' and ifMore != 'no':
                    raise ValueError
                if print_chapters == 'yes':
                    for chapter in Manage.tehilim.keys():
                        if Manage.tehilim[chapter]['book'] == this_book:
                            print(chapter, end=',')
                    print()
                ifMore = input('enter yes for more book and no if you dont want any more')
                if ifMore != 'yes' and ifMore != 'no':
                    raise ValueError
            self.updateFile()
        except ValueError:
            print('Error:input is not valid')
            self.updateFile()
        except Exception as e:
            print(f"Error:{e}")

    def updateFile(self):
        """עדכון הקובץ של החלוקה בנתונים החדשים לאחר הפסקת החלוקה"""
        file = open(Manage.dividers[self.name], 'r')
        file_content = file.readlines()
        file.close()
        file_content[1] = f"count books:{self.count_books}\n"
        file_content[2] = f"current book:{self.current_book}\n"
        file = open(Manage.dividers[self.name], 'w')
        for i in file_content:
            file.write(i)
        file.close()
