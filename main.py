class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class Movie:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class Ticket:
    def __init__(self, userId, movieId, id):
        self.userId = userId
        self.movieId = movieId
        self.id = id

class CinemaTicketSystem:
    def __init__(self):
        self.movies = []
        self.users = []
        self.tickets = []
    def addUser(self, userName):
        userId = len(self.users)
        self.users.append(User(userName, userId))
        print(f"Идентификатор пользователя: {userId}")
    def addMovie(self, movieName):
        movieId = len(self.movies)
        self.movies.append(Movie(movieName, movieId))
        print(f"Идентификатор фильма: {movieId}")
    def showAllMovies(self):
        for movie in self.movies:
            print(f"Название фильма: {movie.name}, Идентификатор фильма: {movie.id}")
    def buyTicket(self, userId, movieId):
        ticketId = len(self.tickets)
        self.tickets.append(Ticket(userId, movieId, ticketId))
        print(f"Идентификатор билета: {ticketId}")

    def cancelTicket(self, ticketId):
        for ticket in self.tickets:
            if ticket.id == ticketId:
                self.tickets.remove(ticket)
                print("True")
                return
        print("False")

    def run(self):
        while True:
            print("\nЗдравствуйте, у вас есть следующие доступные функции:")
            print("1. Добавить новый фильм")
            print("2. Показать все доступные фильмы")
            print("3. Добавить нового пользователя")
            print("4. Купить билет")
            print("5. Отменить покупку билета")
            print("6. Выйти")
            choice = input("Введите номер функции: ")
            if choice == '1':
                movieName = input("Введите название фильма: ")
                self.addMovie(movieName)
                giveUserSometime = input("Введите что угодно чтобы продолжить: ")
            elif choice == '2':
                self.showAllMovies()
                giveUserSometime = input("Введите что угодно чтобы продолжить: ")
            elif choice == '3':
                userName = input("Введите имя пользователя: ")
                self.addUser(userName)
                giveUserSometime = input("Введите что угодно чтобы продолжить: ")
            elif choice == '4':
                userId = int(input("Введите идентификатор пользователя: "))
                movieId = int(input("Введите идентификатор фильма: "))
                self.buyTicket(userId, movieId)
                giveUserSometime = input("Введите что угодно чтобы продолжить: ")
            elif choice == '5':
                ticketId = int(input("Введите идентификатор билета: "))
                self.cancelTicket(ticketId)
                giveUserSometime = input("Введите что угодно чтобы продолжить: ")
            elif choice == '6':
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
                giveUserSometime = input("Введите что угодно чтобы продолжить: ")

cinema_system = CinemaTicketSystem()
cinema_system.run()
