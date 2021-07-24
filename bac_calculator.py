# Main program
import sqlite3
from helpers import main_menu, load_drinks, choose_drinks
from helpers import log_in, connect_database, check_if_registered, register_user
from helpers import get_volume, calculate_again, plot_data_average
from helpers import get_person_data, plot_data_custom
from calculations import average_male_calc, average_female_calc, custom_person_calc

def main():
    # Load common drinks and data for calculations.
    txt_file = r"drinks.txt"
    database_file = r"database.db"
    drinks = load_drinks(txt_file)

    # Main Menu
    print("Welcome to Blood Alcohol Content Calculator")
    while True:
        option = main_menu()
        if option == 1:
            while True:
                drink, abv_pick = choose_drinks(drinks)
                volume = get_volume()
                male_result = average_male_calc(drink, abv_pick, volume)
                female_result = average_female_calc(drink, abv_pick, volume)
                plot_data_average(male_result, female_result)

                again = calculate_again()
                if again == 1:
                    continue
                elif again == 2:
                    break

        elif option == 2:
            person = get_person_data()
            while True:
                drink, abv_pick = choose_drinks(drinks)
                volume = get_volume()
                person_result = custom_person_calc(person, drink, abv_pick, volume)
                plot_data_custom(person_result)

                again = calculate_again()
                if again == 1:
                    continue
                elif again == 2:
                    break

        elif option == 3:
            conn = connect_database(database_file)
            cursor = conn.cursor()
            user_data = log_in(cursor)
            conn.close()
            if user_data:
                while True:
                    drink, abv_pick = choose_drinks(drinks)
                    volume = get_volume()
                    person_result = custom_person_calc(user_data, drink, abv_pick, volume)
                    plot_data_custom(person_result, user_data['username'])

                    again = calculate_again()
                    if again == 1:
                        continue
                    elif again == 2:
                        break

        elif option == 4:
            registering = True
            conn = connect_database(database_file)
            cursor = conn.cursor()
            while registering:
                username = input("Enter your username for registration or 'q' to exit to main menu: \n").lower()
                registered = check_if_registered(cursor, username)
                if username == 'q':
                    break
                else:
                    if registered:
                        print("Username already registered...")
                    else:
                        person = get_person_data()
                        register_user(username, person, cursor)
                        print(f"{username} Registered successfully!")
                        registering = False
            conn.commit()
            conn.close()

        elif option == 5:
            break



if __name__ == "__main__":
    main()