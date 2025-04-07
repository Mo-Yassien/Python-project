import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database

class ReservationsPage(tk.Frame):
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
                              text="Your Reservations",
                              font=("Arial", 20, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Create Treeview
        self.tree = ttk.Treeview(main_container, columns=(
            "ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat"
        ), show="headings")
        
        # Configure columns
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Flight", text="Flight Number")
        self.tree.heading("Departure", text="Departure")
        self.tree.heading("Destination", text="Destination")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Seat", text="Seat Number")
        
        # Set column widths
        self.tree.column("ID", width=50)
        self.tree.column("Name", width=150)
        self.tree.column("Flight", width=100)
        self.tree.column("Departure", width=100)
        self.tree.column("Destination", width=100)
        self.tree.column("Date", width=100)
        self.tree.column("Seat", width=100)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Grid the tree and scrollbar
        self.tree.grid(row=1, column=0, sticky="nsew")
        scrollbar.grid(row=1, column=1, sticky="ns")
        
        # Buttons container
        buttons_frame = ttk.Frame(main_container)
        buttons_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        # Edit button
        edit_button = ttk.Button(buttons_frame,
                               text="Edit",
                               command=self.edit_reservation)
        edit_button.grid(row=0, column=0, padx=5, ipadx=20, ipady=10)
        
        # Delete button
        delete_button = ttk.Button(buttons_frame,
                                 text="Delete",
                                 command=self.delete_reservation)
        delete_button.grid(row=0, column=1, padx=5, ipadx=20, ipady=10)
        
        # Refresh button
        refresh_button = ttk.Button(buttons_frame,
                                  text="Refresh",
                                  command=self.refresh_reservations)
        refresh_button.grid(row=0, column=2, padx=5, ipadx=20, ipady=10)
        
        # Back button
        back_button = ttk.Button(buttons_frame,
                               text="Back to Home",
                               command=lambda: controller.show_frame("HomePage"))
        back_button.grid(row=0, column=3, padx=5, ipadx=20, ipady=10)
        
        # Load initial data
        self.refresh_reservations()
    
    def refresh_reservations(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get reservations from database
        conn = database.create_connection()
        if conn is not None:
            reservations = database.get_all_reservations(conn)
            conn.close()
            
            # Add reservations to treeview
            for reservation in reservations:
                self.tree.insert("", "end", values=reservation)
    
    def edit_reservation(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a reservation to edit")
            return
        
        reservation_id = self.tree.item(selected_item[0])["values"][0]
        self.controller.show_frame("EditReservationPage")
        self.controller.frames["EditReservationPage"].load_reservation(reservation_id)
    
    def delete_reservation(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a reservation to delete")
            return
        
        reservation_id = self.tree.item(selected_item[0])["values"][0]
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this reservation?"):
            conn = database.create_connection()
            if conn is not None:
                database.delete_reservation(conn, reservation_id)
                conn.close()
                messagebox.showinfo("Success", "Reservation deleted successfully!")
                self.refresh_reservations()
            else:
                messagebox.showerror("Error", "Could not connect to database") 