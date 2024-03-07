from books import Books
from days import Days
from dates import Dates
from chapters import Chapters


print("hello! welcome to the תהילים company")
name=input("enter name you want to pray for")
if_continue='continue'
while if_continue != 'finish':
    try:
        type=input('enter part you want to say:book/day/date/chapter from the ספר תהילים.')
        if type !='book' and type !='day' and type !='date' and type !='chapter':
            raise ValueError
        if type=='book':
            book=Books(name)
            book.get_book()
        if type=='day':
            day=Days(name)
            day.get_day()
        if type == 'date':
            date = Dates(name)
            date.get_date()
        if type == 'chapter':
            chapter = Chapters(name)
            chapter.get_chapter()
        input('enter finish or continue')
    except ValueError:
        print('Error: input is not valid')
    except Exception as e:
        print(e)