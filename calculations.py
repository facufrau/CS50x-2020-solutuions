# Calculations functions

def average_male_calc(drink_type, drink_abv, drink_volume):
    male = {"r": 0.68, "weight": 80}
    rate = 0.15
    density = 0.789
    alcohol_g = round((drink_abv * drink_volume * density) / 100, 3)

    bac_male = alcohol_g / (male["weight"] * male["r"])
    male_timelapse = [round(bac_male,2),]
    while True:
        bac_male -= rate
        if bac_male < 0:
            male_timelapse.append(round(bac_male,2))
            break
        else:
            male_timelapse.append(round(bac_male,2))
    return male_timelapse

def average_female_calc(drink_type, drink_abv, drink_volume):
    female = {"r": 0.55, "weight": 70}
    rate = 0.15
    density = 0.789
    alcohol_g = round((drink_abv * drink_volume * density) / 100, 3)

    bac_female = alcohol_g / (female["weight"] * female["r"])
    female_timelapse = [round(bac_female,2),]
    while True:
        bac_female -= rate
        if bac_female < 0:
            female_timelapse.append(round(bac_female,2))
            break
        else:
            female_timelapse.append(round(bac_female,2))
    return female_timelapse

def custom_person_calc(person_dict, drink_type, drink_abv, drink_volume):
    rate = 0.15
    density = 0.789

    alcohol_g = round((drink_abv * drink_volume * density) / 100, 3)
    bac_custom = alcohol_g / (person_dict["weight"] * person_dict["r"])

    person_timelapse = [round(bac_custom,2),]
    while True:
        bac_custom -= rate
        if bac_custom < 0:
            person_timelapse.append(round(bac_custom,2))
            break
        else:
            person_timelapse.append(round(bac_custom,2))
    return person_timelapse