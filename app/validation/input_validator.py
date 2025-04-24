from app.models.calculator_input import DriverInput

def validate_driver_input(input_driver_data:DriverInput):
    errors = []

    # Drive name exists & contains alphabetical characters only
    if not input_driver_data.name.strip():
        errors.append("Driver name is required.")
    elif not input_driver_data.name.replace(" ", "").isalpha():
        errors.append("Driver name must only contain letters.")

    try: # Horsepower boundary validation
        if input_driver_data.horsepower < 0:
            errors.append("Horsepower must be a positive number.")
    except ValueError:
        errors.append("Horsepower must be a number.")

    try: # Coaching hours boundary validation
        if input_driver_data.coaching_hours < 0 or input_driver_data.coaching_hours > 5:
            errors.append("Coaching hours must be between 0 and 5.")
    except ValueError:
        errors.append("Coaching hours must be a number.")

    try: # Race entry boundary validation
        if input_driver_data.race_entries < 0:
            errors.append("Race entries must be 0 or more.")
    except ValueError:
        errors.append("Race entries must be a number.")

    return errors
