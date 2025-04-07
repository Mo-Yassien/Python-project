import tkinter as tk
from tkinter import ttk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Configure the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Create main container
        main_container = ttk.Frame(self, padding=20)
        main_container.grid(row=0, column=0, sticky="nsew")
        
        # Title
        title_label = ttk.Label(main_container, 
                              text="Flight Reservation System",
                              font=("Arial", 24, "bold"))
        title_label.grid(row=0, column=0, pady=20)
        
        subtitle_label = ttk.Label(main_container,
                                 text="Book and manage your flight reservations",
                                 font=("Arial", 12))
        subtitle_label.grid(row=1, column=0, pady=10)
        
        # Buttons container
        buttons_frame = ttk.Frame(main_container)
        buttons_frame.grid(row=2, column=0, pady=20)
        
        # Book Flight button
        book_button = ttk.Button(buttons_frame,
                               text="Book a Flight",
                               command=lambda: controller.show_frame("BookingPage"))
        book_button.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=10)
        
        # View Reservations button
        view_button = ttk.Button(buttons_frame,
                               text="View Reservations",
                               command=lambda: controller.show_frame("ReservationsPage"))
        view_button.grid(row=1, column=0, padx=10, pady=10, ipadx=20, ipady=10) 