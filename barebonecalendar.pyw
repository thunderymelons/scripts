import tkinter as tk
import pickle
from tkinter import messagebox

MAX_EVENTS_DISPLAYED = 5  # Maximum number of events to display for each date

def add_event():
    selected_date = calendar.get()
    event_text = event_entry.get()
    if selected_date not in events:
        events[selected_date] = []
    events[selected_date].append(event_text)
    update_event_listbox()
    save_events()
    update_event_dates()

def delete_event():
    selected_date = calendar.get()
    selected_event = event_listbox.get(tk.ACTIVE)
    if selected_date in events and selected_event in events[selected_date]:
        events[selected_date].remove(selected_event)
        update_event_listbox()
        save_events()
        update_event_dates()

    # Delete the selected date from the "Dates with Events" list
    selected_date_with_event = dates_with_events.get(tk.ACTIVE)
    if selected_date_with_event:
        selected_date = selected_date_with_event.split(" - ")[0]
        if selected_date in events:
            del events[selected_date]
            update_event_dates()
            save_events()

def update_event_listbox():
    event_listbox.delete(0, tk.END)
    selected_date = calendar.get()
    if selected_date in events:
        for event in events[selected_date]:
            event_listbox.insert(tk.END, event)

def update_event_dates():
    dates_with_events.delete(0, tk.END)
    sorted_dates = sorted(events.keys())  # Sort dates in numerical order
    for date in sorted_dates:
        event_list = events[date]
        if event_list:
            events_to_display = ", ".join(event_list[:MAX_EVENTS_DISPLAYED])
            dates_with_events.insert(tk.END, f"{date} - {events_to_display}")

def show_events():
    selected_item = dates_with_events.get(tk.ACTIVE)
    if selected_item:
        selected_date = selected_item.split(" - ")[0]
        event_text = "\n".join(events[selected_date])
        messagebox.showinfo("Events for " + selected_date, event_text)

def save_events():
    with open('events.pkl', 'wb') as file:
        pickle.dump(events, file)

def load_events():
    try:
        with open('events.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

# Create the main application window
root = tk.Tk()
root.title("Calendar App")

# Create a label to display the selected date
calendar_label = tk.Label(root, text="Selected Date (mm/dd): ")
calendar_label.pack()

# Create a calendar widget (using StringVar to store the selected date)
selected_date = tk.StringVar()
calendar = tk.Entry(root, textvariable=selected_date)
calendar.pack(pady=10)

# Create an entry for adding events
event_entry = tk.Entry(root, width=30)
event_entry.pack()

# Buttons to add and delete events
add_button = tk.Button(root, text="Add Event", command=add_event)
delete_button = tk.Button(root, text="Delete Event", command=delete_event)
add_button.pack()
delete_button.pack()

# Listbox to display events for the selected day
event_listbox = tk.Listbox(root, width=30)
event_listbox.pack()

# Listbox to display dates with events and their first 5 events
dates_with_events_label = tk.Label(root, text="Dates with Events:")
dates_with_events_label.pack()
dates_with_events = tk.Listbox(root, width=80)
dates_with_events.pack()

# Button to show events for the selected day or selected date from the list
show_button = tk.Button(root, text="Show Events", command=show_events)
show_button.pack()

# Load events from a file or initialize an empty dictionary
events = load_events()

# Update the listboxes with loaded events
update_event_listbox()
update_event_dates()

root.mainloop()
