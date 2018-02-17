# The moon goes through phases because it orbits the earth and the sun hits it differently at different places in its orbit. This means that, depending on where it is in its orbit, you might see a full moon, right quarter moon, or even "no" moon (new moon) at all. It takes 27.3 days for the moon to orbit the Earth, but the actual phase difference from one full moon to the next is 29.5 days because the earth cruises a cool 45 million miles around the sun in that 27.3 days. It takes 2.2 days for the the moon to make up for that distance and get all the way back to where you last saw a full moon.

# Whenever the moon is full twice in one month, the second one is called a "blue moon." This last happened in July of 2015 on the 1st and 31st. The next time is January of 2018 (same days). You can research the timing, otherwise you can assume midnight. Write a program that determines how many "blue moons" there will be in third milenia (2000-2999)?

# If you want to be really, really specific, the lunar month is actually 29 days, 12 hours, and 44 minutes.
import math
def get_first_moon(year):
    days = 0.0
    if year > 2018:
        for i in range(2018, year):
            if i % 4 == 0:
                days += 366.0
            else:
                days += 365.0
    else:
        for i in range(year, 2018):
            if i % 4 == 0:
                days += 366.0
            else:
                days += 365.0
    return days % 29.5


def lunar(start_date, end_date):
    leap_year = [0.0, 31.0, 60.0, 91.0, 121.0, 152.0, 182.0, 213.0, 244.0, 274.0, 305.0, 335.0, 366.0]
    reg_year = [0.0, 31.0, 59.0, 90.0, 120.0, 151.0, 181.0, 212.0, 243.0, 273.0, 304.0, 334.0, 365.0]
    cycle_counter = get_first_moon(start_date) + 1
    days = 0
    blue_moons = 0
    luner_phase = 29.5
    
    for i in range(int(start_date), int(end_date) + 1):
        if i % 4 == 0 and i % 100 != 0:
            while cycle_counter - days <= 366:
                for j in range(0, len(leap_year)):
                    if (leap_year[j] < (cycle_counter - days) <= leap_year[j + 1]) and (leap_year[j] < ((cycle_counter + luner_phase) - days) <= leap_year[j + 1]):
                        blue_moons += 1
                cycle_counter += luner_phase
            days += 366
        else:
            while cycle_counter - days <= 365:
                for j in range(0, len(reg_year)):
                    if reg_year[j] < cycle_counter - days <= reg_year[j + 1] and reg_year[j] < (cycle_counter + luner_phase) - days <= reg_year[j + 1]:
                        blue_moons += 1
                        print reg_year[j]
                cycle_counter += luner_phase
            days += 365
    return blue_moons, cycle_counter, days

print lunar(2000, 2999)

print get_first_moon(2018)