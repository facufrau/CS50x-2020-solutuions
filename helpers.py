# Helpers functions
import matplotlib.pyplot as plt
import sqlite3


def load_drinks(txt_file):
    """
    Load the drinks txt file, processes it and returns a dictionary.
    """
    with open(txt_file) as f:
        drinks = {}
        for line in f.read().split("\n"):
            line = line.split(":")
            drink = line[0]
            alcohol = float(line[1])
            drinks[drink] = alcohol
    return drinks


def main_menu():
    """
    Prints the main menu and asks user for options.
    """
    options = ["------------------------------------------",
        "1 -> Calculate for an average person (anonymous)",
        "2 -> Calculate for a custom person (anonymous)",
        "3 -> Calculate with registered user data",
        "4 -> Register user data",
        "5 -> Exit",
        "------------------------------------------"]
    while True:
        print("\n".join(options))
        option = input("Select an option: ")
        try:
            option = int(option)
        except:
            print("Please enter only numbers 1,2,3,4 or 5")

        if option in [1,2,3,4,5]:
            return option


def connect_database(database_path):
    try:
        conection = sqlite3.connect(database_path)
        return conection
    except:
        print("Error connecting with database")


def log_in(cursor_database):
    """
    Logs in the user and returns a dictionary with user data.
    """
    while True:
        username = input("Enter your username for calculate or 'q' to exit to main menu: \n").lower()
        if username == 'q':
            break
        else:
            results = cursor_database.execute("SELECT * FROM users WHERE username=?", (username,))
            try:
                raw_data = results.fetchall()[0]
                user_data = {'username': raw_data[0], 'gender': raw_data[1],
                'height': raw_data[2], 'weight': raw_data[3], 'r': raw_data[4]}
                print(f"Username {username} succesfully loaded!")
                return user_data
            except:
                print("Username not registered or not valid.")


def check_if_registered(cursor_database, name):
    check_user = cursor_database.execute("SELECT username FROM users WHERE username=?", (name,))
    if check_user.fetchall():
        return True
    else:
        return False

def register_user(name, person_data, cursor_database):
    data = (name, person_data["gender"], person_data["height"], person_data["weight"], person_data["r"])
    cursor_database.execute("INSERT INTO users VALUES (?,?,?,?,?)", data)
    return 1


def choose_drinks(drinks_dict):
    """
    Show the available drinks and returns the chosen by user.
    """
    while True:
        print("Drinks available: ")
        print(" - ".join(drinks_dict.keys()))
        drink_pick = input("Select a drink: ").lower()
        try:
            abv_pick = drinks_dict[drink_pick]
            return drink_pick, abv_pick
        except KeyError:
            print("Please enter a drink stored in database.\n\n")


def get_volume():
    """
    Asks the user for the volume of alcohol taken.
    """
    while True:
        volume = input("Volume in mL of the drink taken: ")
        try:
            volume = int(volume)
            if volume > 0:
                return volume
        except:
            print("Please enter a number.\n")


def get_person_data():
    """
    Get gender, height, weight, returns a dict with data and r factor.
    """
    person = {}
    while True:
        gender = input("Enter 'm' for male and 'f' for female: ")
        if gender.lower() in ['m', 'f']:
            person["gender"] = gender
            break
        else:
            print("Please enter only 'm' or 'f'\n")

    while True:
        height = input("Enter your height in cm: ")
        try:
            height = int(height)
            if 250 > height > 50:
                person["height"] = height / 100
                break
        except:
            print("Please enter a height between 50 and 250 cm.\n")

    while True:
        weight = input("Enter your weight in kg: ")
        try:
            weight = int(weight)
            if 300 > weight > 30:
                person["weight"] = weight
                break
        except:
            print("Please enter a weight between 30 and 300 kg.\n")

    bmi_calculated = round((person["weight"] / (person["height"]**2)), 2)
    if gender == 'm':
        r_factor = 1.0181 - (0.01213 * bmi_calculated)
    elif gender == 'f':
        r_factor = 0.9367 - (0.01240 * bmi_calculated)
    person["r"] = round(r_factor, 2)

    return person


def calculate_again():
    while True:
        try:
            again = int(input('Enter 1 to calculate again or 2 to exit to main menu: \n'))
            if again in (1,2):
                return again
            else:
                print("Please enter numbers 1 or 2.")
        except:
            print("Please enter numbers 1 or 2.")


def plot_data_average(male_data, female_data):
        plt.plot(male_data, label='male')
        plt.plot(female_data, label='female')
        plt.ylabel('Blood alcohol content g/L')
        plt.xlabel('Hours passed')
        plt.ylim(0.0,)
        plt.xlim(1,)
        plt.legend()
        plt.show()


def plot_data_custom(person_data, label_name = False):
        try:
            label_name = person_data['username']
        except:
            pass

        if label_name:
            plt.plot(person_data, label=label_name)
        else:
            plt.plot(person_data, label='Custom person')

        plt.ylabel('Blood alcohol content g/L')
        plt.xlabel('Hours passed')
        plt.ylim(0.0,)
        plt.xlim(1,)
        plt.legend()
        plt.show()