from tabulate import tabulate
#list of patients
patient_list = [{'name': 'aunike', 'gender': 'female', 'age': 30, 'address': 'alam sutera, tangerang', 'medical record': 10001},
               {'name': 'gilang', 'gender': 'male', 'age': 29, 'address': 'gatot subroto, jakarta selatan', 'medical record': 10002},
               {'name': 'rizky', 'gender': 'male', 'age': 28, 'address': 'tebet, jakarta selatan', 'medical record': 10003},
               {'name': 'shapna', 'gender': 'female', 'age': 30,'address':'setiabudi, jakarta selatan', 'medical record': 10004}] 
#list of doctor
doctor_list = [{'name': 'drg. renny lia', 'specialist': 'conservation', 'schedule': 'monday','daily quota': 8},
                {'name': 'drg. nurul aprilia', 'specialist': 'periodontia', 'schedule': 'tuesday', 'daily quota': 10}, 
                {'name': 'drg. octa pratiwi', 'specialist': 'ortodontia', 'schedule': 'wednesday','daily quota': 9},
                {'name': 'drg. natalia astrid', 'specialist': 'prostodontia', 'schedule': 'thursday','daily quota':6},
                {'name': 'drg. mutiara', 'specialist':'oral surgery', 'schedule': 'friday', 'daily quota': 3},
                {'name': 'drg. tiffany', 'specialist':'periodontia', 'schedule': 'monday', 'daily quota': 5},
                {'name': 'drg. saras', 'specialist':'ortodonti', 'schedule': 'tuesday', 'daily quota': 6},
                {'name': 'drg. becky', 'specialist':'prostodonti', 'schedule': 'wednesday', 'daily quota': 4},
                {'name': 'drg. tiara', 'specialist':'conservation', 'schedule': 'thursday', 'daily quota': 7},
                {'name': 'drg. charlotte', 'specialist':'endodontics', 'schedule': 'friday', 'daily quota': 3}
                ]
#list of treatment
treatment_list = [{'treatment':'intraoral examination', 'price': 100000},
                  {'treatment':'composite filling', 'price': 200000}, 
                  {'treatment':'scalling', 'price': 150000}, 
                  {'treatment':'bleaching', 'price': 1500000}, 
                  {'treatment':'tooth extraction','price':200000}, 
                  {'treatment':'veneers','price': 2000000}, 
                  {'treatment':'braces','price':6000000}, 
                  {'treatment':'root canal','price':3000000},
                  {'treatment':'control visit', 'price':150000}]

table_patient = []
def display_patient():
    table_patient.clear()
    for data in patient_list:
        table_patient.append([
            data["name"].capitalize(),
            data["gender"].capitalize(),
            data["age"],
            data["address"].capitalize(),
            data["medical record"]
        ])
    print(tabulate(table_patient, headers=["Name", "Gender", "Age","Address","Medical Record"], tablefmt="grid"))
    
def display_doctors():
    table_doctors = []
    for data in doctor_list:
        table_doctors.append([
            data["name"].title(),
            data["specialist"].capitalize(),
            data["schedule"],
            data["daily quota"]
        ])
    print(tabulate(table_doctors, headers=["Name", "Specialist", "Schedule", "Daily Quota"], tablefmt="grid"))
    

def display_treatments():
    table_treatment = []
    for data in treatment_list:
        table_treatment.append([
            data["treatment"],
            data ["price"]
        ])
    print(tabulate(table_treatment, headers=["Treatment", "price"], tablefmt="grid"))

def search_patient(table_patient):
    headers = ["Nama", "Gender", "Age", "Address", "Medical Record"]
    while True:
        try:
            user_input_search_word = input("Enter any word(s) to search: (or 'exit' to quit) ").lower()
            if user_input_search_word == "exit":
                break
            words_filter = [item for item in table_patient if any(user_input_search_word in str(attr).lower() for attr in item)]
            print(tabulate(words_filter, headers=headers, tablefmt="grid"))
        except ValueError:
            print("Enter a valid input. Please try again!")


def add_doctors():
    while True:
        try:
            found = False
            admin_input_name_doctor = input("enter doctor name: ").strip().lower()
            admin_input_specialist = input("enter specialist: ").strip().lower()

            # Quota input with retry loop for correct integer input
            while True:
                try:
                    admin_input_Quota = int(input("enter daily quota: "))
                    break  # Exit loop if successful integer conversion
                except ValueError:
                    print("Fill the daily quota with numbers!")

            # Check if doctor already exists
            for doctor in doctor_list:
                if doctor["name"] == admin_input_name_doctor:
                    doctor["daily quota"] += admin_input_Quota
                    found = True
                    print("Doctor's quota has been successfully updated.")
                    break

            if not found:
                # schedule input with validation
                while True:
                    admin_input_schedule = input("enter schedule (monday-saturday): ").strip().lower()
                    if admin_input_schedule in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]:
                        break
                    else:
                        print("Please fill in the schedule from Monday to Saturday.")

                # Create new doctor entry if not found
                dict_doctor = {
                    "name": admin_input_name_doctor,
                    "specialist": admin_input_specialist,
                    "schedule": admin_input_schedule,
                    "daily quota": admin_input_Quota
                }
                doctor_list.append(dict_doctor)
                print("New doctor successfully added.")

            display_doctors()

            # Ask if the user wants to continue adding doctors
            while True:
                    admin_input_confirm = input(" do you want to add new doctor? type 'yes' to continue or 'no' to quit: ").lower()
                    if admin_input_confirm == "no":
                        display_doctors()
                        return
                    elif admin_input_confirm == "yes":
                        display_doctors()
                        break
                    else:
                        print("please type 'yes' or 'no' ")
        except ValueError:
            print('invalid input')


def remove_doctors():
    while True:
        display_doctors()
        try:
            found = False
            admin_input_name_doctor = input("enter name: ").strip().title()
            for doctor in doctor_list:
                if doctor["name"] == admin_input_name_doctor.lower():
                    admin_input_Quota = int(input("enter daily quota: "))
                    doctor['daily quota'] = doctor['daily quota'] - admin_input_Quota 
                    if doctor["daily quota"] <= 0:
                        doctor_list.remove(doctor)
                    found = True
                    break
            if not found:    
                print("Please fill in according to what is on the doctor list")
            while True:
                admin_input_confirm = input("type 'next' to continue or 'exit' to quit: ").lower()
                if admin_input_confirm == "exit":
                    display_doctors()
                    return
                elif admin_input_confirm == "next":
                    # display_doctors()
                    break
                else:
                    print("invalid input")
        except ValueError:
            print('invalid input') 

def add_edit_treatment():
    while True:
        try:
            display_treatments()  # Display current treatments and prices
            found = False
            admin_input_treatment = input("enter treatment: ").strip().lower()  # Normalize input

            # Check if the treatment already exists
            for treatment in treatment_list:
                if treatment["treatment"] == admin_input_treatment:
                    found = True
                    # Ask user if they want to update the price
                    update_price = input(f"Treatment already exists with price. {treatment['price']}. Do you want to update the price? (yes/no): ").lower()
                    if update_price == "yes":
                        while True:
                            try:
                                admin_input_price = int(input("enter new price: "))
                                treatment["price"] = admin_input_price
                                print("Treatment price has been updated.")
                                break
                            except ValueError:
                                print("Price must be a number! Please try again.")
                    break

            if not found:  # If treatment doesn't exist, add a new one
                while True:
                    try:
                        admin_input_price = int(input("Enter price for new treatment: "))
                        break
                    except ValueError:
                        print("Price must be a number! Please try again.")

                dict_perawatan = {
                    "treatment": admin_input_treatment,
                    "price": admin_input_price,
                }
                treatment_list.append(dict_perawatan)
                print("New treatment has been added.")

            display_treatments()  # Display updated treatments list

            # User prompt to continue or exit
            while True:
                try:
                    admin_input_confirm = input("type 'next' to continue or 'exit' to quit: ").lower()
                    if admin_input_confirm == "exit":
                        return  # Exit the function
                    elif admin_input_confirm == "next":
                        break
                    else:
                        print("Invalid input. Please type 'next' to continue or 'exit' to quit.")
                except ValueError:
                    print("invalid input")
        except ValueError:
            print("invalid input")
def record_pasien():
    while True:
        try:
            user_input_name = input("Enter your name: ").strip()
            if not user_input_name:  # Ensure name is not empty
                print("Name cannot be empty. Please try again.")
                continue
            user_input_address = input("Enter your address: ").strip()
            if not user_input_address:  # Ensure address is not empty
                print("Address cannot be empty. Please try again.")
                continue

            # Loop specifically for gender input
            while True:
                user_input_gender = input("enter gender your (male/female): ")
                if user_input_gender.lower() in ["male", "female"]:  # Checks if the input is either 'male' or 'female'
                    break
                else:
                    print("Gender must be 'male' or 'female'. Please try again.")
            # Loop specifically for age
            while True:
                try:
                    user_input_age = int(input("enter your age (numbers): "))
                    if user_input_age < 0 or user_input_age > 100:  # Validate age range
                        print("Please enter a valid age between 0 and 100.")
                    else:
                        break
                except ValueError:
                    print("Invalid input! Age must be in numbers. Please try again.")
                
            dict_patient = {
                "name": user_input_name,
                "gender": user_input_gender,
                "age": user_input_age,
                "address": user_input_address,
                "medical record": 10001 + len(patient_list)
            }

            patient_list.append(dict_patient)
            print("Patient successfully registered.")
            break
            # Confirmation to continue or exit
        except Exception as e:
            print(f"An error occurred: {e}")  

table_billing = []
list_queue_numb = []

def print_booking_appointment(patient_list):
    print("***************************************************")
    print(f"Patient Name: {patient_list[-1]['name']}")
    print(f"Medical Record: {patient_list[-1]['medical record']}")
    print(f"Gender: {patient_list[-1]['gender']}")
    print(f"Age: {patient_list[-1]['age']}")
    print(f"Address: {patient_list[-1]['address']}")
    print("---------------------------------------------------")
    total = 0
    for item in list_queue_numb:
        if "price" in item:
            total += item["price"]
    print(tabulate(table_billing, headers=["schedule", "Queue number", "doctors", "Treatment","price"], tablefmt="grid"))
    print("***************************************************")
    print(f"                                    Total :{total}")
    list_queue_numb.clear()
    table_billing.clear()

def choose_treatment():
    while True:
        try:
            display_treatments()  # Display all available treatments.
            user_input_treatment = input("Enter the treatment you want: ").strip().lower()
            found_treatment = False
            price = None

            # Check if the treatment exists.
            for treatment in treatment_list:
                if treatment["treatment"].lower() == user_input_treatment:
                    price = treatment["price"]
                    found_treatment = True
                    break

            if not found_treatment:
                print("There is no such treatment! Please enter a treatment from the list.")
                continue

            # User selects the day and the function lists available doctors.
            user_input_day = input("Enter the day you choose: ").strip().lower()
            available_doctors = [doc for doc in doctor_list if doc["schedule"].lower() == user_input_day and doc["daily quota"] > 0]

            if not available_doctors:
                print("There is no service available for that day, or all doctors are fully booked.")
                continue

            print("Doctors available on that day:")
            for idx, doc in enumerate(available_doctors, 1):
                print(f"{idx}. {doc['name']} - Quota left: {doc['daily quota']}")

            # Validate user's choice of doctor.
            doctor_index = int(input("Choose a doctor by entering the number: ")) - 1
            if doctor_index not in range(len(available_doctors)):
                raise IndexError("Selection out of range. Please try again.")
            doctor = available_doctors[doctor_index]

            # Decrement the doctor's quota if available.
            if doctor["daily quota"] > 0:
                doctor["daily quota"] -= 1
            else:
                print(f"Quota for {doctor['name']} has run out.")
                continue

            # Booking the appointment.
            queue_number = len([x for x in list_queue_numb if x["doctors"] == doctor["name"]]) + 1
            appointment = {
                "schedule": user_input_day,
                "no_antrian": queue_number,
                "doctors": doctor["name"],
                "treatment": user_input_treatment,
                "price": price
            }
            list_queue_numb.append(appointment)
            table_billing.append([user_input_day, queue_number, doctor["name"], user_input_treatment, price])

            # Ask if the user wants to add more treatments.
            admin_input_confirm = input("Do you want to add more treatments? Type 'yes' to continue or 'no' to exit: ").lower()
            if admin_input_confirm == "no":
                print_booking_appointment(patient_list)
                return
            elif admin_input_confirm != "yes":
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input: Please enter a valid number.")
        except IndexError:
            print("The doctor's selection is not valid. Please select a number from the list.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Admin menu
def admin_menu():
    while True:
        choice = input('''
        Admin Menu:
        1. Display Patients
        2. Display Doctor schedules
        3. Display Treatments
        4. Add New Doctor
        5. Delete Doctor               
        6. Add and Edit Treatment
        7. Exit Admin Menu
        Choose an option: ''').strip()
        
        if choice == '1':
            display_patient()
            search_patient(table_patient)
        elif choice == '2':
            display_doctors()
        elif choice == '3':
            display_treatments()
        elif choice == '4':
            add_doctors()
        elif choice == '5':
            remove_doctors()
        elif choice == '6':
            add_edit_treatment()
        elif choice == '7':
            print("Exiting Admin Menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Patient menu
def patient_menu():
    while True:
        choice = input('''
        Patient Menu:
        1. View schedule Doctor
        2. View Treatment Menu
        3. Register for booking appointment
        4. Exit User Menu
        Choose an option: ''').strip()
        
        if choice == '1':
            display_doctors()
        elif choice == '2':
            display_treatments()
        elif choice == '3':
            record_pasien()
            choose_treatment()
        elif choice == '4':
            print("Thank you for visiting our Dental Clinic Services!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Main menu
def main_menu():
    while True:
        user_type = input("Are you an Admin, a Patient, or would you like to Exit? (Admin/Patient/Exit): ").lower()
        if user_type == "admin":
            admin_menu()
        elif user_type == "patient":
            patient_menu()
        elif user_type == "exit":
            print("Thank you for using our dental clinic service!.")
            break  # Breaks out of the while loop to end the function and thus exit the system
        else:
            print("Invalid selection. Please type 'Admin', 'Patient', or 'Exit'")

if __name__ == "__main__":
    main_menu()