import math
import sqlite3
import json
from decimal import Decimal
from math import cos, sin, sqrt
import math
import numpy as np

sensor_type = {"رادار": "radar",
               "جمر": "jammer",
               "آنتن": "antenna"}

sensor_status = {"آفلاین": "0",
                 "آنلاین": "1"}

area = {"شمال": "north",
        "شمال غربی": "north west",
        "شمال شرقی": "north east",
        "شمال میانه": "middle north",
        "جنوب": "south",
        "جنوب غربی": "west south",
        "حنوب شرقی": "east south",
        "جنوب میانه": "middle south",
        "شرق": "east",
        "شرق میانه": "middle east",
        "غرب": "west",
        "غرب میانه": "middle west",
        "مرکز": "center"}

parameter = {
    "توان": "power",
    "فرکانس": "frequency",
    "آزیموت": "azimuth"
}

conn = sqlite3.connect('test.db')
print("database Opened successfully!")


# "چند سنسور از نوع # مربوط به پادگان # وجود دارد؟"
def get_sensor_count_based_on_sensor_type(sensor_type, barracks_ID):
    cursor = conn.cursor()
    if sensor_type == "sensor":
        cursor.execute("select count(*) from sensors \
                 where barracks_ID=?", barracks_ID)
    else:
        cursor.execute("select count(*) from sensors \
                 where type=? and barracks_ID=?", (sensor_type, barracks_ID))

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


# "چند سنسور # مربوط به پادگان # وجود دارد؟"
def get_sensor_count_based_on_sensor_status(sensor_status, barracks_ID):
    cursor = conn.cursor()
    cursor.execute("select count(*) from sensors \
                 where online=? and barracks_ID=?", (sensor_status, barracks_ID))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


# "پادگان # از چه نوع است؟"
def get_type_of_barracks(barracks_ID):
    cursor = conn.cursor()
    cursor.execute("select type from barracks \
                 where ID=?", (barracks_ID,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


# "پادگان # مربوط به دشمن است یا خود؟"
def is_barracks_insider(barracks_ID):
    cursor = conn.cursor()
    cursor.execute("select insider from barracks \
                 where ID=?", (barracks_ID,))
    rows = cursor.fetchall()
    if rows:
        if rows[0][0] == 1:
            print("Barracks " + str(barracks_ID) + " is insider!")
        elif rows[0][0] == 0:
            print("Barracks " + str(barracks_ID) + " is not insider!")
    cursor.close()


# "مختصات جغرافیایی پادگان # چیست؟"
def get_coordinates_of_barracks(barracks_id):
    cursor = conn.cursor()
    cursor.execute("select longitude, latitude from barracks \
                 where ID=?", (barracks_id,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


# "آیپی سنسور # چیست؟"
def get_sensor_IP(sensor_id):
    cursor = conn.cursor()
    cursor.execute("select ip from sensors \
                 where ID=?", (sensor_id,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


# "سنسور # از چه نوع است؟"
def get_sensor_type(sensor_id):
    cursor = conn.cursor()
    cursor.execute("select type from sensors \
                 where ID=?", (sensor_id,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


# "مختصات جفرافیایی سنسور # چیست؟"
def get_coordinates_of_sensor(sensor_id):
    cursor = conn.cursor()
    cursor.execute("select longitude, latitude from sensors \
                 where ID=?", (sensor_id,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


# "پارامترهای مربوط به سنسور # دارای چه مقادیری هستند؟"
def get_all_parameters_of_sensor(sensor_id):
    cursor = conn.cursor()
    cursor.execute("select parameters from sensors \
                 where ID=?", (sensor_id,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


# "پادگان های دشمن کدامند؟"
def get_enemy_barracks():
    cursor = conn.cursor()
    cursor.execute("select ID from barracks \
                 where insider=0")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


# "سنسورهای دشمن در پادگان # کدامند؟"
def get_enemy_sensors_based_on_barracks_id(barracks_id):
    cursor = conn.cursor()
    cursor.execute("select ID from sensors \
                 where barracks_ID=? and insider=0", (barracks_id,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


# "#های # کشور چه وضعیتی دارند؟"
def get_sensors_status_based_on_location_and_sensor_type(area, sensor_type):
    cursor = conn.cursor()
    if sensor_type == "sensor":
        if area == "north":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1")
        elif area == "north east":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1")
        elif area == "north west":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1")
        elif area == "middle north":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1")
        elif area == "south":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1")
        elif area == "south east":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1")
        elif area == "south west":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1")
        elif area == "middle south":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1")
        elif area == "east":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1")
        elif area == "middle east":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1")
        elif area == "west":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1")
        elif area == "middle west":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1")
        elif area == "center":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1")
    else:
        if area == "north":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1 and type=?", (sensor_type,))
        elif area == "north east":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1 and type=?", (sensor_type,))
        elif area == "north west":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1 and type=?", (sensor_type,))
        elif area == "middle north":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1 and type=?", (sensor_type,))
        elif area == "south":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1 and type=?", (sensor_type,))
        elif area == "south east":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1 and type=?", (sensor_type,))
        elif area == "south west":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1 and type=?", (sensor_type,))
        elif area == "middle south":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1 and type=?", (sensor_type,))
        elif area == "east":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1 and type=?", (sensor_type,))
        elif area == "middle east":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1 and type=?", (sensor_type,))
        elif area == "west":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1 and type=?", (sensor_type,))
        elif area == "middle west":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1 and type=?", (sensor_type,))
        elif area == "center":
            cursor.execute("select ID,online from sensors \
                         where longitude > 1 and latitude > 1 and type=?", (sensor_type,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


# "سنسور # با چه #(پارامتر)ی کار میکند؟"
def get_parameter_of_sensor_based_on_parameter_type(sensor_id, parameter, sensor_type):
    cursor = conn.cursor()
    if sensor_type == "sensor":
        cursor.execute("select parameters from sensors \
                     where ID=?", (sensor_id,))
    else:
        cursor.execute("select parameters from sensors \
                     where ID=? and type=?", (sensor_id, sensor_type))
    cursor.execute("select parameters from sensors \
                 where ID=? and", (sensor_id,))
    rows = cursor.fetchall()
    if rows:
        parameter_dict = json.loads(rows[0][0])
        print(parameter_dict[str(parameter)])
    else:
        print("Oops! This sensor doesnt exist")
    cursor.close()


# "حوزه استحفاظی سنسور # با حوزه استحفاظی سنسور # تداخل دارد؟"
def check_if_two_sensors_interfere(sensor_id_1, sensor_id_2, sensor_type_1, sensor_type_2):
    cursor = conn.cursor()
    if sensor_type_1 == "sensor" and sensor_type_2 == "sensor":
        cursor.execute("select longitude, latitude, radius from sensors \
                             where ID=?", (sensor_id_1,))
        rows = cursor.fetchall()
        if rows:
            dict1 = {
                "longitude": rows[0][0],
                "latitude": rows[0][1],
                "radius": rows[0][2]
            }
            # print(dict1)
        else:
            print("This sensor doesnt exist!")
            return
        cursor.execute("select longitude, latitude, radius from sensors \
                             where ID=?", (sensor_id_2,))
        rows = cursor.fetchall()
        if rows:
            dict2 = {
                "longitude": rows[0][0],
                "latitude": rows[0][1],
                "radius": rows[0][2]
            }
            # print(dict2)
        else:
            print("This sensor doesnt exist!")
            return
    else:
        cursor.execute("select longitude, latitude, radius from sensors \
                     where ID=? and type=?", (sensor_id_1, sensor_type_1))
        rows = cursor.fetchall()
        if rows:
            dict1 = {
                "longitude": rows[0][0],
                "latitude": rows[0][1],
                "radius": rows[0][2]
            }
            # print(dict1)
        else:
            print("This sensor doesnt exist!")
            return
        cursor.execute("select longitude, latitude, radius from sensors \
                     where ID=? and type=?", (sensor_id_2, sensor_type_2))
        rows = cursor.fetchall()
        if rows:
            dict2 = {
                "longitude": rows[0][0],
                "latitude": rows[0][1],
                "radius": rows[0][2]
            }
            # print(dict2)
        else:
            print("This sensor doesnt exist!")
            return
    cursor.close()
    if if_tow_circle_overlaps(dict1["longitude"], dict2["longitude"], dict1["latitude"], dict2["latitude"],
                              dict1["radius"], dict2["radius"]):
        print("Yes!")
        return 1
    else:
        print("No!")
        return 0


# "حوزه استحفاظی چه سنسورهایی با یکدیگر تداخل ندارد؟"
def get_all_sensors_that_do_not_interfere_based_on_sensor_type(sensor_type):
    cursor = conn.cursor()
    if sensor_type == "sensor":
        cursor.execute("select * from sensors")
    else:
        cursor.execute("select * from sensors \
                     where type=?", (sensor_type,))
    rows = cursor.fetchall()
    rows2 = rows.copy()
    for i in rows:
        for j in rows2:
            if i[0] != j[0]:
                if not if_tow_circle_overlaps(i[3], j[3], i[4], j[4], i[5], j[5]):
                    print(i)
                    print("and")
                    print(j)
                    print("********")
    # print(type(rows))
    # for row in rows:
    #    print(row)
    cursor.close()


# "تعداد سرهنگ های پادگان # چندتاست؟"
def get_count_of_barracks_staff_based_on_rank(barracks_name, rank):
    cursor = conn.cursor()
    cursor.execute("select count(name) from staff \
                 where barracks_ID=? and rank=?", (barracks_name, rank))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


# "ُسرهنگ # در کدام پادگان حضور دارد؟"
# todo: create training data for this intent
def get_barracks_name_of_a_staff(staff_name, rank):
    cursor = conn.cursor()
    cursor.execute("select barracks_ID from staff \
                 where name=? and rank=?", (staff_name, rank))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print(rank + " " + staff_name + " does not exist!")
    cursor.close()


# "سطح دسترسی سرهنگ # چیست؟"
# todo: create training data for this intent
def get_access_level_of_a_staff(staff_name, rank):
    cursor = conn.cursor()
    cursor.execute("select access_level from staff \
                 where name=? and rank=?", (staff_name, rank))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print(rank + " " + staff_name + " does not exist!")
    cursor.close()


# "سرهنگ # فعال است یا بلاک؟"
# todo: create training data for this intent
def is_staff_active(staff_name, rank):
    cursor = conn.cursor()
    cursor.execute("select active from staff \
                 where name=? and rank=?", (staff_name, rank))
    rows = cursor.fetchall()
    if rows:
        if rows[0][0] == 1:
            print(rank + " " + staff_name + " is active!")
        elif rows[0][0] == 0:
            print(rank + " " + staff_name + " is blocked!")
    else:
        print(rank + " " + staff_name + " does not exist!")
    cursor.close()


def create_training_set():
    my_list = []
    for i in range(1, 1001):
        for key in sensor_type:
            # "چند سنسور از نوع رادار مربوط به پادگان 1 وجود دارد؟"
            my_dict = {
                "text": "چند سنسور از نوع " + str(key) + " مربوط به پادگان " + str(i) + " وجود دارد؟",
                "slots": {"sensor_type": str(key),
                          "barracks_name": str(i)},
                "query": "get_sensor_count_based_on_sensor_type #" + str(sensor_type[key]) + " #" + str(i)
            }
            my_list.append(my_dict)

            for key2 in parameter:
                # "رادار 1 با چه فرکانسی کار می کند؟"
                my_dict = {
                    "text": str(key) + " " + str(i) + " با چه " + str(key2) + "ی کار می کند؟",
                    "slots": {"sensor_name": str(i),
                              "sensor_type": str(key),
                              "parameter": str(key2)},
                    "query": "get_parameter_of_sensor_based_on_parameter_type #" + str(i) + " #" + str(
                        sensor_type[key] + " #" + str(parameter[key2]))
                }
                my_list.append(my_dict)

        for key2 in parameter:
            # "سنسور 1 با چه فرکانسی کار می کند؟"
            my_dict = {
                "text": "سنسور " + str(i) + " با چه " + str(key2) + "ی کار می کند؟",
                "slots": {"sensor_name": str(i),
                          "sensor_type": "سنسور",
                          "parameter": str(key2)},
                "query": "get_parameter_of_sensor_based_on_parameter_type #" + str(i) + " #sensor #" + str(
                    parameter[key2])
            }
            my_list.append(my_dict)

        for key in sensor_status:
            # "چند سنسور آنلاین مربوط به پادگان 1 وجود دارد؟"
            my_dict = {
                "text": "چند سنسور " + str(key) + " مربوط به پادگان " + str(i) + " وجود دارد؟",
                "slots": {"sensor_status": str(key),
                          "barracks_name": str(i)},
                "query": "get_sensor_count_based_on_sensor_status #" + str(sensor_status[key]) + " #" + str(i)
            }
            my_list.append(my_dict)

        # "پادگان 1 از چه نوع است؟"
        my_dict = {
            "text": "پادگان " + str(i) + " از چه نوع است؟ ",
            "slots": {"barracks_name": str(i)},
            "query": "get_type_of_barracks #" + str(i)
        }
        my_list.append(my_dict)

        # "پادگان 1 مربوط به دشمن است یا خود؟"
        my_dict = {
            "text": "پادگان " + str(i) + " مربوط به دشمن است یا خود؟ ",
            "slots": {"barracks_name": str(i)},
            "query": "is_barracks_insider #" + str(i)
        }
        my_list.append(my_dict)

        # "مختصات جغرافیایی پادگان 1 چیست؟"
        my_dict = {
            "text": "مختصات جغرافیایی پادگان " + str(i) + " چیست؟ ",
            "slots": {"barracks_name": str(i)},
            "query": "get_coordinates_of_barracks #" + str(i)
        }
        my_list.append(my_dict)

        # "آیپی سنسور 1 چیست؟"
        my_dict = {
            "text": "آیپی سنسور " + str(i) + " چیست؟ ",
            "slots": {"sensor_name": str(i)},
            "query": "get_sensor_IP #" + str(i)
        }
        my_list.append(my_dict)

        # "سنسور 1 از چه نوع است؟"
        my_dict = {
            "text": "سنسور " + str(i) + " از چه نوع است؟ ",
            "slots": {"sensor_name": str(i)},
            "query": "get_sensor_type #" + str(i)
        }
        my_list.append(my_dict)

        # "مختصات جغرافیایی سنسور 1 چیست؟"
        my_dict = {
            "text": "مختصات جغرافیایی سنسور " + str(i) + " چیست؟ ",
            "slots": {"sensor_name": str(i)},
            "query": "get_coordinates_of_sensor #" + str(i)
        }
        my_list.append(my_dict)

        # "پارامترهای مربوط به سنسور 1 دارای چه مقادیری هستند؟"
        my_dict = {
            "text": "پارامتر های مربوط به سنسور " + str(i) + " دارای چه مقادیری هستند؟ ",
            "slots": {"sensor_name": str(i)},
            "query": "get_all_parameters_of_sensor #" + str(i)
        }
        my_list.append(my_dict)

        # "پادگان های دشمن کدامند؟"
        my_dict = {
            "text": "پادگان های دشمن کدامند؟ ",
            "slots": {},
            "query": "get_enemy_barracks"
        }
        my_list.append(my_dict)

        # "سنسورهای دشمن در پادگان 1 کدامند؟"
        my_dict = {
            "text": "سنسور های دشمن در پادگان " + str(i) + " کدامند؟ ",
            "slots": {"barracks_name": str(i)},
            "query": "get_enemy_sensors_based_on_barracks_id #" + str(i)
        }
        my_list.append(my_dict)

    for key2 in area:
        for key in sensor_type:
            # "رادارهای جنوب کشور چه وضعیتی دارند؟"
            my_dict = {
                "text": str(key) + " های " + str(key2) + " کشور چه وضعیتی دارند؟",
                "slots": {"sensor_type": str(key),
                          "area": str(key2)},
                "query": "get_sensors_status_based_on_location_and_sensor_type #" + str(sensor_type[key]) + " #" + str(
                    area[key2])
            }
            my_list.append(my_dict)

        # "سنسورهای جنوب کشور چه وضعیتی دارند؟"
        my_dict = {
            "text": "سنسور های " + str(key2) + " کشور چه وضعیتی دارند؟",
            "slots": {"sensor_type": "سنسور",
                      "area": str(key2)},
            "query": "get_sensors_status_based_on_location_and_sensor_type #sensor #" + str(area[key2])
        }
        my_list.append(my_dict)

    for key in range(1, 1001):
        for key2 in range(1, 1001):
            for type1 in sensor_type:
                for type2 in sensor_type:
                    # "حوزه استحفاظی رادار 1 با حوزه استحفاظی آنتن 2 تداخل دارد؟"
                    my_dict = {
                        "text": "حوزه استحفاظی " + str(type1) + " " + str(key) + " با حوزه استحفاظی " + str(
                            type2) + " " + str(key2) + " تداخل دارد؟",
                        "slots": {"sensor_name_1": str(key),
                                  "sensor_name_2": str(key2),
                                  "sensor_type_1": str(type1),
                                  "sensor_type_2": str(type2)},
                        "query": "check_if_two_sensors_interfere #" + str(key) + " #" + str(key2) + " #"
                                 + str(sensor_type[type1]) + " #" + str(sensor_type[type2])
                    }
                    my_list.append(my_dict)

            # "حوزه استحفاظی سنسور 1 با حوزه استحفاظی سنسور 2 تداخل دارد؟"
            my_dict = {
                "text": "حوزه استحفاظی سنسور " + str(key) + " با حوزه استحفاظی سنسور " + " " + str(
                    key2) + " تداخل دارد؟",
                "slots": {"sensor_name_1": str(key),
                          "sensor_name_2": str(key2),
                          "sensor_type_1": "سنسور",
                          "sensor_type_2": "سنسور"},
                "query": "check_if_two_sensors_interfere #" + str(key) + " #" + str(key2) + " #sensor #sensor"
            }
            my_list.append(my_dict)

    for key in sensor_type:
        # "حوزه استحفاظی چه رادارهایی با هم تداخل ندارند؟"
        my_dict = {
            "text": "حوزه استحفاظی چه " + str(key) + " هایی با هم نداخل ندارند؟",
            "slots": {"sensor_type": str(key)},
            "query": "get_all_sensors_that_do_not_interfere_based_on_sensor_type #" + str(sensor_type[key])
        }
        my_list.append(my_dict)

    # "حوزه استحفاظی چه سنسورهایی با هم تداخل ندارند؟"
    my_dict = {
        "text": "حوزه استحفاظی چه سنسور هایی با هم تداخل ندارند؟",
        "slots": {"sensor_type": "سنسور"},
        "query": "get_all_sensors_that_do_not_interfere_based_on_sensor_type #sensor"
    }
    my_list.append(my_dict)
    for item in my_list:
        print(item)
    print(len(my_list))



def create_ner_intent_json():
    my_list = []
    for i in range(1, 1001):
        for key in sensor_type:
            # "چند سنسور از نوع رادار مربوط به پادگان 1 وجود دارد؟"
            my_dict = {
                "text": "چند سنسور از نوع " + str(key) + " مربوط به پادگان " + str(i) + " وجود دارد؟",
                "slots": {"sensor_type": str(key),
                          "barracks_name": str(i)},
                "query": "get_sensor_count_based_on_sensor_type #" + str(sensor_type[key]) + " #" + str(i)
            }
            my_list.append(my_dict)

            for key2 in parameter:
                # "رادار 1 با چه فرکانسی کار می کند؟"
                my_dict = {
                    "text": str(key) + " " + str(i) + " با چه " + str(key2) + "ی کار می کند؟",
                    "slots": {"sensor_name": str(i),
                              "sensor_type": str(key),
                              "parameter": str(key2)},
                    "query": "get_parameter_of_sensor_based_on_parameter_type #" + str(i) + " #" + str(
                        sensor_type[key] + " #" + str(parameter[key2]))
                }
                my_list.append(my_dict)

        for key2 in parameter:
            # "سنسور 1 با چه فرکانسی کار می کند؟"
            my_dict = {
                "text": "سنسور " + str(i) + " با چه " + str(key2) + "ی کار می کند؟",
                "slots": {"sensor_name": str(i),
                          "sensor_type": "سنسور",
                          "parameter": str(key2)},
                "query": "get_parameter_of_sensor_based_on_parameter_type #" + str(i) + " #sensor #" + str(
                    parameter[key2])
            }
            my_list.append(my_dict)

        for key in sensor_status:
            # "چند سنسور آنلاین مربوط به پادگان 1 وجود دارد؟"
            my_dict = {
                "text": "چند سنسور " + str(key) + " مربوط به پادگان " + str(i) + " وجود دارد؟",
                "slots": {"sensor_status": str(key),
                          "barracks_name": str(i)},
                "query": "get_sensor_count_based_on_sensor_status #" + str(sensor_status[key]) + " #" + str(i)
            }
            my_list.append(my_dict)

        # "پادگان 1 از چه نوع است؟"
        my_dict = {
            "text": "پادگان " + str(i) + " از چه نوع است؟ ",
            "slots": {"barracks_name": str(i)},
            "query": "get_type_of_barracks #" + str(i)
        }
        my_list.append(my_dict)

        # "پادگان 1 مربوط به دشمن است یا خود؟"
        my_dict = {
            "text": "پادگان " + str(i) + " مربوط به دشمن است یا خود؟ ",
            "slots": {"barracks_name": str(i)},
            "query": "is_barracks_insider #" + str(i)
        }
        my_list.append(my_dict)

        # "مختصات جغرافیایی پادگان 1 چیست؟"
        my_dict = {
            "text": "مختصات جغرافیایی پادگان " + str(i) + " چیست؟ ",
            "slots": {"barracks_name": str(i)},
            "query": "get_coordinates_of_barracks #" + str(i)
        }
        my_list.append(my_dict)

        # "آیپی سنسور 1 چیست؟"
        my_dict = {
            "text": "آیپی سنسور " + str(i) + " چیست؟ ",
            "slots": {"sensor_name": str(i)},
            "query": "get_sensor_IP #" + str(i)
        }
        my_list.append(my_dict)

        # "سنسور 1 از چه نوع است؟"
        my_dict = {
            "text": "سنسور " + str(i) + " از چه نوع است؟ ",
            "slots": {"sensor_name": str(i)},
            "query": "get_sensor_type #" + str(i)
        }
        my_list.append(my_dict)

        # "مختصات جغرافیایی سنسور 1 چیست؟"
        my_dict = {
            "text": "مختصات جغرافیایی سنسور " + str(i) + " چیست؟ ",
            "slots": {"sensor_name": str(i)},
            "query": "get_coordinates_of_sensor #" + str(i)
        }
        my_list.append(my_dict)

        # "پارامترهای مربوط به سنسور 1 دارای چه مقادیری هستند؟"
        my_dict = {
            "text": "پارامتر های مربوط به سنسور " + str(i) + " دارای چه مقادیری هستند؟ ",
            "slots": {"sensor_name": str(i)},
            "query": "get_all_parameters_of_sensor #" + str(i)
        }
        my_list.append(my_dict)

        # "پادگان های دشمن کدامند؟"
        my_dict = {
            "text": "پادگان های دشمن کدامند؟ ",
            "slots": {},
            "query": "get_enemy_barracks"
        }
        my_list.append(my_dict)

        # "سنسورهای دشمن در پادگان 1 کدامند؟"
        my_dict = {
            "text": "سنسور های دشمن در پادگان " + str(i) + " کدامند؟ ",
            "slots": {"barracks_name": str(i)},
            "query": "get_enemy_sensors_based_on_barracks_id #" + str(i)
        }
        my_list.append(my_dict)

    for key2 in area:
        for key in sensor_type:
            # "رادارهای جنوب کشور چه وضعیتی دارند؟"
            my_dict = {
                "text": str(key) + " های " + str(key2) + " کشور چه وضعیتی دارند؟",
                "slots": {"sensor_type": str(key),
                          "area": str(key2)},
                "query": "get_sensors_status_based_on_location_and_sensor_type #" + str(sensor_type[key]) + " #" + str(
                    area[key2])
            }
            my_list.append(my_dict)

        # "سنسورهای جنوب کشور چه وضعیتی دارند؟"
        my_dict = {
            "text": "سنسور های " + str(key2) + " کشور چه وضعیتی دارند؟",
            "slots": {"sensor_type": "سنسور",
                      "area": str(key2)},
            "query": "get_sensors_status_based_on_location_and_sensor_type #sensor #" + str(area[key2])
        }
        my_list.append(my_dict)

    for key in range(1, 1001):
        for key2 in range(1, 1001):
            for type1 in sensor_type:
                for type2 in sensor_type:
                    # "حوزه استحفاظی رادار 1 با حوزه استحفاظی آنتن 2 تداخل دارد؟"
                    my_dict = {
                        "text": "حوزه استحفاظی " + str(type1) + " " + str(key) + " با حوزه استحفاظی " + str(
                            type2) + " " + str(key2) + " تداخل دارد؟",
                        "slots": {"sensor_name_1": str(key),
                                  "sensor_name_2": str(key2),
                                  "sensor_type_1": str(type1),
                                  "sensor_type_2": str(type2)},
                        "query": "check_if_two_sensors_interfere #" + str(key) + " #" + str(key2) + " #"
                                 + str(sensor_type[type1]) + " #" + str(sensor_type[type2])
                    }
                    my_list.append(my_dict)

            # "حوزه استحفاظی سنسور 1 با حوزه استحفاظی سنسور 2 تداخل دارد؟"
            my_dict = {
                "text": "حوزه استحفاظی سنسور " + str(key) + " با حوزه استحفاظی سنسور " + " " + str(
                    key2) + " تداخل دارد؟",
                "slots": {"sensor_name_1": str(key),
                          "sensor_name_2": str(key2),
                          "sensor_type_1": "سنسور",
                          "sensor_type_2": "سنسور"},
                "query": "check_if_two_sensors_interfere #" + str(key) + " #" + str(key2) + " #sensor #sensor"
            }
            my_list.append(my_dict)

    for key in sensor_type:
        # "حوزه استحفاظی چه رادارهایی با هم تداخل ندارند؟"
        my_dict = {
            "text": "حوزه استحفاظی چه " + str(key) + " هایی با هم نداخل ندارند؟",
            "slots": {"sensor_type": str(key)},
            "query": "get_all_sensors_that_do_not_interfere_based_on_sensor_type #" + str(sensor_type[key])
        }
        my_list.append(my_dict)

    # "حوزه استحفاظی چه سنسورهایی با هم تداخل ندارند؟"
    my_dict = {
        "text": "حوزه استحفاظی چه سنسور هایی با هم تداخل ندارند؟",
        "slots": {"sensor_type": "سنسور"},
        "query": "get_all_sensors_that_do_not_interfere_based_on_sensor_type #sensor"
    }
    my_list.append(my_dict)
    for item in my_list:
        print(item)
    print(len(my_list))


def if_tow_circle_overlaps(longitude1, longitude2, latitude1, latitude2, radius1, radius2):
    '''
     1. Convert (lat, lon) to (x,y,z) geocentric coordinates.
     As usual, because we may choose units of measurement in which the earth has a unit radius
     '''
    x_p1 = Decimal(cos(math.radians(longitude1)) * cos(math.radians(latitude1)))  # x = cos(lon)*cos(lat)
    y_p1 = Decimal(sin(math.radians(longitude1)) * cos(math.radians(latitude1)))  # y = sin(lon)*cos(lat)
    z_p1 = Decimal(sin(math.radians(latitude1)))  # z = sin(lat)
    x1 = (x_p1, y_p1, z_p1)
    x_p2 = Decimal(cos(math.radians(longitude2)) * cos(math.radians(latitude2)))  # x = cos(lon)*cos(lat)
    y_p2 = Decimal(sin(math.radians(longitude2)) * cos(math.radians(latitude2)))  # y = sin(lon)*cos(lat)
    z_p2 = Decimal(sin(math.radians(latitude2)))  # z = sin(lat)
    x2 = (x_p2, y_p2, z_p2)
    '''
     2. Convert the radii r1 and r2 (which are measured along the sphere) to angles along the sphere.
     By definition, one nautical mile (NM) is 1/60 degree of arc (which is pi/180 * 1/60 = 0.0002908888 radians).
     '''
    r1 = Decimal(math.radians((radius1 / 1852) / 60))  # radius1/1852 converts meter to Nautical mile.
    r2 = Decimal(math.radians((radius2 / 1852) / 60))
    '''
     3. The geodesic circle of radius r1 around x1 is the intersection of the earth's surface with an Euclidean sphere
     of radius sin(r1) centered at cos(r1)*x1.
     4. The plane determined by the intersection of the sphere of radius sin(r1) around cos(r1)*x1 and the earth's surface
     is perpendicular to x1 and passes through the point cos(r1)x1, whence its equation is x.x1 = cos(r1)
     (the "." represents the usual dot product); likewise for the other plane. There will be a unique point x0 on the
     intersection of those two planes that is a linear combination of x1 and x2. Writing x0 = ax1 + b*x2 the two planar
     equations are;
        cos(r1) = x.x1 = (a*x1 + b*x2).x1 = a + b*(x2.x1)
        cos(r2) = x.x2 = (a*x1 + b*x2).x2 = a*(x1.x2) + b
     Using the fact that x2.x1 = x1.x2, which I shall write as q, the solution (if it exists) is given by
        a = (cos(r1) - cos(r2)*q) / (1 - q^2),
        b = (cos(r2) - cos(r1)*q) / (1 - q^2).
     '''
    q = Decimal(np.dot(x1, x2))
    if q ** 2 != 1:
        a = (Decimal(cos(r1)) - Decimal(cos(r2)) * q) / (1 - q ** 2)
        b = (Decimal(cos(r2)) - Decimal(cos(r1)) * q) / (1 - q ** 2)
        '''
         5. Now all other points on the line of intersection of the two planes differ from x0 by some multiple of a vector
         n which is mutually perpendicular to both planes. The cross product  n = x1~Cross~x2  does the job provided n is 
         nonzero: once again, this means that x1 and x2 are neither coincident nor diametrically opposite. (We need to 
         take care to compute the cross product with high precision, because it involves subtractions with a lot of
         cancellation when x1 and x2 are close to each other.)
         '''
        n = np.cross(x1, x2)
        '''
         6. Therefore, we seek up to two points of the form x0 + t*n which lie on the earth's surface: that is, their length
         equals 1. Equivalently, their squared length is 1:  
         1 = squared length = (x0 + t*n).(x0 + t*n) = x0.x0 + 2t*x0.n + t^2*n.n = x0.x0 + t^2*n.n
         '''
        x0_1 = [a * f for f in x1]
        x0_2 = [b * f for f in x2]
        x0 = [sum(f) for f in zip(x0_1, x0_2)]
        '''
           The term with x0.n disappears because x0 (being a linear combination of x1 and x2) is perpendicular to n.
           The two solutions easily are   t = sqrt((1 - x0.x0)/n.n)    and its negative. Once again high precision
           is called for, because when x1 and x2 are close, x0.x0 is very close to 1, leading to some loss of
           floating point precision.
         '''
        if (np.dot(x0, x0) <= 1) & (
                np.dot(n, n) != 0):  # This is to secure that (1 - np.dot(x0, x0)) / np.dot(n,n) > 0
            t = Decimal(sqrt((1 - np.dot(x0, x0)) / np.dot(n, n)))
            t1 = t
            t2 = -t
            i1 = x0 + t1 * n
            i2 = x0 + t2 * n
            '''
             7. Finally, we may convert these solutions back to (lat, lon) by converting geocentric (x,y,z) to geographic
             coordinates. For the longitude, use the generalized arctangent returning values in the range -180 to 180
             degrees (in computing applications, this function takes both x and y as arguments rather than just the
             ratio y/x; it is sometimes called "ATan2").
             '''
            i1_lat = math.degrees(math.asin(i1[2]))
            i1_lon = math.degrees(math.atan2(i1[1], i1[0]))
            ip1 = (i1_lat, i1_lon)
            i2_lat = math.degrees(math.asin(i2[2]))
            i2_lon = math.degrees(math.atan2(i2[1], i2[0]))
            ip2 = (i2_lat, i2_lon)
            return [ip1, ip2]
        elif np.dot(n, n) == 0:
            return "The centers of the circles can be neither the same point nor antipodal points."
        else:
            return "The circles do not intersect"
    else:
        return "The centers of the circles can be neither the same point nor antipodal points."


create_training_set()
