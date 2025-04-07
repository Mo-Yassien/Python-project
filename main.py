import tkinter as tk
from tkinter import ttk
import database
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

class FlightReservationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configure the main window
        self.title("Flight Reservation System")
        self.geometry("800x600")
        self.resizable(True, True)
        
        # Create container frame
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Initialize database
        database.initialize_database()
        
        # Dictionary to hold all frames
        self.frames = {}
        
        # Create and store all pages
        for F in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Show the home page
        self.show_frame("HomePage")
    
    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()

def main():
    app = FlightReservationApp()
    app.mainloop()

if __name__ == "__main__":
    main() 