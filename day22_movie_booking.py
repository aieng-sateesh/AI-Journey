# Day 22 - Movie Ticket Booking System using OOP

# define movie class
class Movie:
    def __init__(self, title, available_seats):  # constructor for movie
        self.title = title
        self.available_seats = available_seats

    def show_info(self):  # show movie info
        print(f'{self.title} | Available Seats: {self.available_seats}')

    def book_seat(self, quantity, name, contact):  # book seat method
        if quantity <= self.available_seats:
            self.available_seats -= quantity
            print(f'{quantity} seats booked for {self.title} by {name} ({contact})')
        else:
            print('Not enough seats available')

    def cancel_seat(self, quantity):  # cancel seat method
        self.available_seats += quantity
        print(f'{quantity} seats cancelled for {self.title}')

# define booking manager class
class BookingManager:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):  # add movie to system
        self.movies.append(movie)

    def show_movies(self):  # show all movies
        print('\nAvailable Movies:')
        for movie in self.movies:
            movie.show_info()

    def book_movie(self, title, quantity):  # book movie seats
        for movie in self.movies:
            if movie.title == title:
                name = input('Enter your name: ')
                contact = input('Enter your contact number: ')
                movie.book_seat(quantity, name, contact)
                return
        print('Movie not found')

    def cancel_booking(self, title, quantity):  # cancel booking
        for movie in self.movies:
            if movie.title == title:
                movie.cancel_seat(quantity)
                return
        print('Movie not found')

# sample usage
m1 = Movie("Avengers", 50)
m2 = Movie("Oppenheimer", 30)

manager = BookingManager()
manager.add_movie(m1)
manager.add_movie(m2)

manager.show_movies()
manager.book_movie("Avengers", 2)
manager.cancel_booking("Oppenheimer", 1)
manager.show_movies()
