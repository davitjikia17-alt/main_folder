import random
import json
import os

# שם הקובץ שבו נשמרים הנתונים
DATA_FILE = "trivia_data.json"

# טעינת הנתונים אם הקובץ קיים
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        accounts_lst = data.get("accounts", [])
        password_lst = data.get("passwords", [])
        points_lst = data.get("points", [])
else:
    accounts_lst = []
    password_lst = []
    points_lst = []

# פונקציה לשמירת הנתונים לקובץ
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump({
            "accounts": accounts_lst,
            "passwords": password_lst,
            "points": points_lst
        }, f)

# פונקציות המשחק נשארות כפי שהן
def show_points(name , points_lst):
    index = accounts_lst.index(name)
    print(f"Hi {name} your points count is: {points_lst[index]}")
    return 0

def game(accounts_lst, name ,points_lst):
    index = accounts_lst.index(name)
    points = points_lst[index]
    questions = [
        ("כמה זה 2+2?", "4"),
        ("בירת ישראל?", "ירושלים"),
        ("כמה ימים יש בשבוע?", "7"),
        ("כמה צבעים יש בקשת?", "7"),
        ("כמה רגליים יש לחתול?", "4"),
        ("מהו החיה הגדולה ביותר בעולם?", "לוויתן כחול"),
        ("כמה שעות יש ביום?", "24"),
        ("כמה דקות יש בשעה?", "60"),
        ("כמה חודשים יש בשנה?", "12"),
        ("מהי העיר הכי גדולה בישראל?", "תל אביב"),
        ("כמה כוכבים יש במערכת השמש?", "1"),
        ("איזה חומר נמצא במים במצב מוצק?", "קרח"),
        ("איזה צבעי דגל ישראל?", "כחול ולבן"),
        ("מי כתב את ״הארי פוטר״?", "ג׳יי קיי רולינג"),
        ("מהי המדינה הכי גדולה בעולם?", "רוסיה"),
        ("כמה קצות יש למשולש?", "3"),
        ("כמה צלעות יש למרובע?", "4"),
        ("מהו היבשת הקטנה ביותר?", "אוסטרליה"),
        ("כמה שחקנים יש בקבוצה בכדורגל?", "11"),
        ("מהו המספר הגדול ביותר בין 10, 12 ו-9?", "12"),
        ("מהו היסוד הכימי שמסומן ב-O?", "חמצן"),
        ("כמה שבועות יש בשנה?", "52"),
        ("מי גילה את אמריקה?", "כריסטופר קולומבוס"),
        ("מהי העיר הכי צפונית בעולם?", "סברבארד"),
        ("מהו ההר הגבוה ביותר בעולם?", "איוורסט"),
        ("כמה סנטימטרים יש במטר?", "100"),
        ("מהי השפה המדוברת ביותר בעולם?", "סינית מנדרינית"),
        ("מהו הים הגדול ביותר בעולם?", "הים הפיליפיני"),
        ("כמה כוכבים יש בדגל ארצות הברית?", "50"),
        ("מהי המילה הארוכה ביותר בעברית?", "וכשבהשתעשעויותיכם"),
        ("מהו הירח של כדור הארץ?", "ירח"),
        ("מי המציא את החשמל?", "תומאס אדיסון"),
        ("מהי מערכת הדם בגוף האדם?", "הלב וכלי הדם"),
        ("כמה עצמות יש בגוף האדם?", "206"),
        ("מהו הכוכב הקרוב ביותר לשמש?", "חמה"),
        ("איזה עץ נותן אצטרובל?", "אורן"),
        ("כמה צבעים יש בדגל גרמניה?", "3"),
        ("מהי החיה המהירה ביותר?", "צ׳יטה"),
        ("כמה ימים יש בפברואר בשנה רגילה?", "28"),
        ("כמה ימים יש בפברואר בשנה מעוברת?", "29"),
        ("מי היה ראש הממשלה הראשון של ישראל?", "דוד בן גוריון"),
        ("מהי הבירה של צרפת?", "פריז"),
        ("כמה מדינות יש באירופה?", "44"),
        ("מהי החיה הלאומית של ישראל?", "היעל"),
        ("מהו המאכל הלאומי של יפן?", "סושי"),
        ("מהו היסוד הכימי שמסומן ב-Fe?", "ברזל"),
        ("מהו האי הגדול ביותר בעולם?", "גרינלנד"),
        ("מי כתב את ״האודיסאה״?", "הומרוס"),
        ("מהו הכוח שמושך חפצים כלפי מטה?", "כבידה"),
        ("כמה קילומטרים יש בקילומטר מרובע?", "1000000"),
        ("מי צייר את המונה ליזה?", "לאונרדו דה וינצ׳י"),
        ("מהו הממלכה הגדולה ביותר בעולם?", "בריטניה"),
        ("מהו כלי הנשיפה?", "חצוצרה"),
        ("מהי התקופה בה חיו הדינוזאורים?", "המזוזואיקון"),
        ("מי גילה את הכבידה?", "אייזק ניוטון"),
        ("מהו הרכב האוויר שאנחנו נושמים?", "חנקן וחמצן"),
        ("מהו המטבע של ארצות הברית?", "דולר"),
    ]
    while True:
        if not questions:
            print("No more questions!")
            break
        random_num = random.randint(0, len(questions) - 1)
        print("the question is", questions[random_num][0],"תשובות בעברית בלבד!!!")
        answer = input("Enter your answer: ").strip()
        if answer == questions[random_num][1]:
            points += 1
            print("your answer is right")
        else:
            print("the answer real is", questions[random_num][1])
        questions.pop(random_num)
        play = input("Do you want to exit? (y/n)")
        if play.lower() == "y":
            points_lst[index] = points
            save_data()  # שמירה אחרי המשחק
            return points_lst

def Trivia_quiz_menu(name , password , points_lst , accounts_lst):
    print(f"hi {name} you now in the game menu, have fun")
    while True:
        choice = input("Enter your choice: \n1-Enter game \n2-show points \n3-exit\n")
        if choice == '1':
            points_lst = game(accounts_lst, name ,points_lst)
        elif choice == '2':
            if len(points_lst) == 0:
                print("you have no points")
            else:
                show_points(name , points_lst)
        elif choice == '3':
            print("Thank you for playing")
            break
    return points_lst

def login(accounts_lst, password_lst):
    name = input('Please enter your username: ')
    if name not in accounts_lst:
        print("Username not in the system\n try logging in")
        return 0, 0, 0
    password = input('Please enter your password: ')
    if password not in password_lst:
        print("password not in the system")
        return 0, 0, 0
    if password_lst.index(name) != accounts_lst.index(name):
        print("Not your password")
        return 0, 0, 0
    return 1, name, password

def register(accounts_lst, password_lst ,points_lst):
    while True:
        name = input('Please enter your username: ')
        if not name:
            print("wrong username")
            continue
        if name in accounts_lst:
            print("username already taken")
            continue
        break  # עבר את כל הבדיקות

    while True:
        password = input('Please enter your password: ')
        if not password:
            print("wrong password")
            continue
        if password in password_lst:
            print("password already taken")
            continue
        break  # עבר את כל הבדיקות

    # רק עכשיו מוסיפים ושומרים
    accounts_lst.append(name)
    password_lst.append(password)
    points_lst.append(0)
    save_data()  # שמירה רק אחרי שכל הקלט תקין

    print("Registration successful!")
    return accounts_lst, password_lst, points_lst

def menu(accounts_lst, password_lst , points_lst):
    while True:
        choice = input("Enter your choice: \n1-new account \n2-login \n3-exit\n")
        if choice == '1':
            register(accounts_lst , password_lst , points_lst )
        elif choice == '2':
            get, name, password = login(accounts_lst, password_lst)
            if get == 1:
                Trivia_quiz_menu(name ,password , points_lst , accounts_lst)
        elif choice == '3':
            print("Thank you for using this program")
            break

def main(accounts_lst , password_lst , points_lst):
    print("Welcome to the Trivia-quiz")
    menu(accounts_lst , password_lst , points_lst)

if __name__ == '__main__':
    main(accounts_lst , password_lst , points_lst)