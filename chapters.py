import itertools as it
from manage import Manage
from dividing import Dividing


class Chapters(Dividing):
    """מחלקה שאחראית על חלוקה לפי פרקים בודדים"""
    chapters = list(Manage.tehilim.keys())

    def __init__(self,name):
        """פונקציה בונה מאתחלת את הנתונים לפי הנתונים בקובץ המתאים"""
        Dividing.__init__(self, name)
        file = open(Manage.dividers[name], 'r')
        self.current_chapter = file.readlines()[5].split(':')[1].split('\n')[0]
        file.close()


    def divide_chapters(self):
        """גנרטור שעובר על הפרקים, כשמגיע לפרק האחרון חוזר להתחלה ומעדכן את כמות הספרים שנגמרו"""
        for i in it.count():
            while self.chapters.index(self.current_chapter)<149:
                temp=self.current_chapter
                self.current_chapter=self.chapters[self.chapters.index(self.current_chapter)+1]
                yield temp
            self.current_chapter = self.chapters[0]
            self.count_chapters+=1
            yield self.current_chapter

    def get_chapter(self):
        """פונקציה שמבצעת בפועל את חלוקת הפרקים על פי קלט מהמשתמש וכן מפרטת למשתמש פרטים אודות הפרק שקיבל"""
        try:
            dividing_chapters = self.divide_chapters()
            ifMore = 'yes'
            while ifMore == 'yes':
                self.num_books()
                this_chapter = next(dividing_chapters)
                print(f"the chapter you recive:{this_chapter}")
                print_chapters = input('enter yes if you want to see details about this chapter')
                if ifMore != 'yes' and ifMore != 'no':
                    raise ValueError
                if print_chapters == 'yes':
                   print(Manage.tehilim[this_chapter])
                ifMore = input('enter yes for more chapter and no if you dont want any more')
                if ifMore is not 'yes' and ifMore is not 'no':
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
        file_content=file.readlines()
        file.close()
        file_content[1]=f"count books:{self.count_books}\n"
        file_content[5]=f"current date:{self.current_chapter}\n"
        file = open(Manage.dividers[self.name], 'w')
        for i in file_content:
            file.write(i)
        file.close()