import fileinput
from manage import Manage

class Dividing:
    """מחלקה שמייצגת חלוקה עבור שם מסוים"""
    def __init__(self,name):
        """פעולה בונה שיוצרת אוביקט חלוקה אם החלוקה כבר קייצת מעדכנת נתונים מהקובץ המתאים ואם לא-יוצרת קובץ חדש"""
        self.name = name
        if name in Manage.dividers.keys():
            file = open(f"{name}", 'r')
            self.count_books = file.readlines()[1].split(':')[1].split('\n')[0]
            print(self.count_books)
            file.close()
        else:
            print('')
            Manage.dividers[name]=f'{name}'
            file = open("dividers", 'a')
            file.write(f"{name},")
            file.close()
            file = open(Manage.dividers[name], 'w')
            file.write(f"name:{name}\ncount_books:0\ncurrent_book:א\ncurrent_day:ראשון\ncurrent_date:א\ncurrent_chapter:א")
            file.close()
            self.count_books=0

    """למבדה שמדפיסה את כמות הספרים שחולקו"""
    num_books = lambda self: print(f'numbers of finished books:{self.count_books}')
