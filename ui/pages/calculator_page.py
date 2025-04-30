import logging
from tkinter import ttk, messagebox
from app.constants.training_plans import TRAINING_PLAN_NAMES
from app.calculations.category_resolver import get_category_from_hp
from app.calculations.category_resolver import get_category_feedback
from app.calculations.cost_calculator import itemised_cost_list
from app.validation.input_validator import validate_driver_input
from app.models.calculator_input import DriverInput

class CalculatorPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="Green.TFrame")
        logging.info("Initialising calculator page...")

        self.controller = controller
        
        # Configure grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0) # Page header
        self.rowconfigure(1, weight=0) # User input fields
        self.rowconfigure(2, weight=0) # Output fields
        self.rowconfigure(3, weight=1) # Command buttons

        # Page header
        header_frame = ttk.Frame(self, style="Red.TFrame")
        header_frame.grid(row=0, column=0, sticky="new", padx=10, pady=(10,5))
        header_frame.columnconfigure(0, weight=1)
        header_frame.rowconfigure(0, weight=1)

        page_title_lable = ttk.Label(header_frame, text="Driver Cost Calculator", style="PageTitle.TLabel")
        page_title_lable.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

        # User input form
        user_input_form_frame = ttk.Frame(self, style="Red.TFrame")
        user_input_form_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5,5))
        user_input_form_frame.columnconfigure(0, weight=1)
        user_input_form_frame.columnconfigure(1, weight=1)
        user_input_form_frame.rowconfigure(0, weight=1)
        user_input_form_frame.rowconfigure(1, weight=1)
        user_input_form_frame.rowconfigure(2, weight=1)
        user_input_form_frame.rowconfigure(3, weight=1)
        user_input_form_frame.rowconfigure(4, weight=1)
        user_input_form_frame.rowconfigure(5, weight=1)

        self.user_input_form(user_input_form_frame)

        # Output form
        output_form_frame = ttk.Frame(self, style="Red.TFrame")
        output_form_frame.grid(row=2, column=0, sticky="new", padx=10, pady=(5,5))
        output_form_frame.columnconfigure(0, weight=1)
        output_form_frame.rowconfigure(0, weight=1)

        self.output_label = ttk.Label(output_form_frame)
        self.output_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # Command buttons
        command_buttons_frame = ttk.Frame(self, style="Red.TFrame")
        command_buttons_frame.grid(row=3, column=0, sticky="sew", padx=10, pady=(5,10))
        command_buttons_frame.columnconfigure(0, weight=1) # Clear form button
        command_buttons_frame.columnconfigure(1, weight=1) # Submit form button
        command_buttons_frame.rowconfigure(0, weight=0)

        clear_form_btn = ttk.Button(command_buttons_frame, text="Clear Form", command=self.clear_form)
        clear_form_btn.grid(row=0, column=0, sticky="nse", padx=(10,5), pady=10)

        calculate_btn = ttk.Button(command_buttons_frame, text="Calculate", command=self.calculate_cost)
        calculate_btn.grid(row=0, column=1, sticky="nsw", padx=(5,10), pady=10)

    def user_input_form(self, container):
        # Driver name entry fields
        driver_name_label = ttk.Label(container, text="Driver Name:")
        driver_name_label.grid(row=0, column=0, sticky="w", padx=(10,5), pady=(10,2))
        self.driver_name_entry = ttk.Entry(container)
        self.driver_name_entry.grid(row=0, column=1, sticky="ew", padx=(5,10), pady=(10,2))

        # Training plan entry fields
        training_plan_label = ttk.Label(container, text="Training Plan:")
        training_plan_label.grid(row=1, column=0, sticky="w", padx=(10,5), pady=(2,2))
        self.training_plan_dropdown = ttk.Combobox(container, values=TRAINING_PLAN_NAMES)
        self.training_plan_dropdown.grid(row=1, column=1, sticky="ew", padx=(5,10), pady=(2,2))
        self.training_plan_dropdown.set(TRAINING_PLAN_NAMES[0])  # Default value

        # Horsepower entry fields
        horsepower_label = ttk.Label(container, text="Horsepower (HP):")
        horsepower_label.grid(row=2, column=0, sticky="w", padx=(10,5), pady=(2,2))
        self.horsepower_entry = ttk.Entry(container)
        self.horsepower_entry.grid(row=2, column=1, sticky="ew", padx=(5,10), pady=(2,2))
        self.horsepower_entry.bind("<FocusOut>", self.update_category_field)

        # Add autopopulated category field 
        category_label = ttk.Label(container, text="Category:")
        category_label.grid(row=3, column=0, sticky="w", padx=(10,5), pady=(2,2))
        self.category_entry = ttk.Entry(container, state="readonly")
        self.category_entry.grid(row=3, column=1, sticky="ew", padx=(5,10), pady=(2,2))

        # Coaching hours entry fields
        coaching_hours_label = ttk.Label(container, text="Coaching Hours (0–5):")
        coaching_hours_label.grid(row=4, column=0, sticky="w", padx=(10,5), pady=(2,2))
        self.coaching_hours_entry_spinbox = ttk.Spinbox(container, from_=0, to=5, width=5)
        self.coaching_hours_entry_spinbox.grid(row=4, column=1, sticky="w", padx=(5,10), pady=(2,2))

        # Races entered entry fields
        races_entered_label = ttk.Label(container, text="Races Entered:")
        races_entered_label.grid(row=5, column=0, sticky="w", padx=(10,5), pady=(5,10))
        self.races_entered_entry_spinbox = ttk.Spinbox(container, from_=0, to=10, width=5)
        self.races_entered_entry_spinbox.grid(row=5, column=1, sticky="w", padx=(5,10), pady=(2,10))

    def update_category_field(self, event):
        try: # Identifying category based on HP
            user_input_horsepower_value = int(event.widget.get())
            category = get_category_from_hp(user_input_horsepower_value)
        except ValueError: # Provide user feedback
            logging.error("Auto populate category failed: User horsepower input is not accepted")
            category = "Invalid HP"
            
        # Auto populate category field
        self.category_entry.config(state="!readonly")
        self.category_entry.delete(0, "end")
        self.category_entry.insert(0, category)
        self.category_entry.config(state="readonly")

        # messagebox.showinfo("Incorrect horsepower", "Please enter a whole number greater than zero.")

    def clear_form(self):
        logging.info("Clear input form selected")
        self.driver_name_entry.delete(0, "end")
        self.training_plan_dropdown.set(TRAINING_PLAN_NAMES[0])
        self.horsepower_entry.delete(0, "end")
        self.coaching_hours_entry_spinbox.delete(0, "end")
        self.races_entered_entry_spinbox.delete(0, "end")

        self.category_entry.config(state="!readonly")
        self.category_entry.delete(0, "end")
        self.category_entry.config(state="readonly")

        self.output_label.config(text='')

    def calculate_cost(self):
        logging.info("Calculation input form submitted")

        try: # Grouping user input data
            driver_data = DriverInput(
                name=self.driver_name_entry.get(),
                training_plan=self.training_plan_dropdown.get(),
                horsepower=self.horsepower_entry.get(),
                coaching_hours=self.coaching_hours_entry_spinbox.get(),
                race_entries=self.races_entered_entry_spinbox.get()
            )
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return

        # Validate driver data
        errors = validate_driver_input(input_driver_data=driver_data)
        if errors:
            messagebox.showerror("Input Validation Failed", "\n".join(errors))
            return
        
        if not driver_data.is_race_eligible() and driver_data.race_entries > 0:
            messagebox.showwarning(
                "Eligibility Restriction",
                "Only Intermediate & Elite drivers are allowed to enter races."
            )
            return

        # Perform calculations
        logging.info(f"Calculating costs for: {driver_data}")
        itemised_list = itemised_cost_list(input_driver_data=driver_data)
        category_feedback = get_category_feedback(horsepower=driver_data.horsepower)

        # Provide results to user
        self.output_label.config(
            text=(
                f"Driver: {driver_data.name}\n"
                f"Category: {driver_data.category}\n"
                f"{category_feedback}\n"
                f"{itemised_list}"
            )
        )

    def show(self):
        self.tkraise()
        logging.info("Calculator page loaded")
