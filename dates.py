import itertools as it
from manage import Manage
from dividing import Dividing


class Dates(Dividing):
    """מחלקה שאחראית על חלוקה לפי תאריכים בשבוע"""
    dates =['א','ב','ג','ד','ה','ו','ז','ח','ט','י','יא','יב','יג','יד','טו',
            'טז','יז','יח','יט','כ','כא','כב','כג','כד','כה','כו','כז','כח','כט','ל']

    def __init__(self,name):
        """פונקציה בונה מאתחלת את הנתונים לפי הנתונים בקובץ המתאים"""
        super(Dates,self).__init__(name)
        # Dividing.__init__(self, name)
        file = open(Manage.dividers[name], 'r')
        self.current_date = file.readlines()[4].split(':')[1].split('\n')[0]
        file.close()

    def divide_dates(self):
        """גנרטור שעובר על התאריכים מהתאריך האחרון שחולק, כשמגיע לסוף החודש חוזר להתחלה ומעדכן את כמות הספרים שנגמרו"""
        for i in it.count():
            while self.dates.index(self.current_date)<29:
                temp=self.current_date
                self.current_date = self.dates[self.dates.index(self.current_date) + 1]
                yield temp
            self.current_date = self.dates[0]
            self.count_books+=1
            yield self.current_date

    def get_date(self):
        """פונקציה שמבצעת בפועל את חלוקת התאריכים על פי קלט מהמשתמש וכן מפרטת למשתמש את הפרקים שעליו לאמר"""
        try:
            dividing_dates = self.divide_dates()
            ifMore = 'yes'
            while ifMore == 'yes':
                self.num_books
                this_date = next(dividing_dates)
                print(f"the day you recive:{this_date}")
                print_chapters = input('enter yes if you want to see which chapters are include at the date you reseived')
                if ifMore != 'yes' and ifMore != 'no':
                    raise ValueError
                if print_chapters == 'yes':
                   for chapter in Manage.tehilim.keys():
                       if Manage.tehilim[chapter]['date'] == this_date:
                           print(chapter,end=',')
                   print()
                ifMore = input('enter yes for more date and no if you dont want any more')
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
        file_content=file.readlines()
        file.close()
        file_content[1]=f"count books:{self.count_books}\n"
        file_content[4]=f"current date:{self.current_date}\n"
        file = open(Manage.dividers[self.name], 'w')
        for i in file_content:
            file.write(i)
        file.close()