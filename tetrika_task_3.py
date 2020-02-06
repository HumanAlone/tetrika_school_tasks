participants_dict = {}
users_dict = {}


def from_utc_to_local(inp_date):
    from datetime import datetime
    from dateutil import tz

    try:
        new_date = datetime.strptime(inp_date, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        try:
            new_date = datetime.strptime(inp_date, "%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            print("Something went wrong...")
        else:
            new_date = datetime.strftime(new_date.replace(tzinfo=tz.tzutc()).astimezone(), "%Y-%m-%d %H:%M:%S")
            return new_date
    else:
        new_date = datetime.strftime(new_date.replace(tzinfo=tz.tzutc()).astimezone(), "%Y-%m-%d %H:%M:%S")
        return new_date


try:
    with open(r"C:\Users\HumanAlone\Downloads\tech_quality\users.txt", 'r', encoding='utf-8') as f_inp:
        f_inp.readline()
        f_inp.readline()
        for line in f_inp:
            temp = list(map(lambda x: x.strip(), line.split('|')))
            if len(temp) == 2:
                users_dict[temp[0]] = temp[1]
except FileNotFoundError as err:
    print(err.args[1])

try:
    with open(r"C:\Users\HumanAlone\Downloads\tech_quality\participants.txt", 'r', encoding='utf-8') as f_inp:
        f_inp.readline()
        f_inp.readline()
        for line in f_inp:
            temp = list(map(lambda x: x.strip(), line.split('|')))
            if len(temp) == 2:
                if temp[0] not in participants_dict:
                    if users_dict[temp[1]] == 'tutor':
                        participants_dict[temp[0]] = temp[1]
                    else:
                        participants_dict[temp[0]] = None
                else:
                    if users_dict[temp[1]] == 'tutor':
                        participants_dict[temp[0]] = temp[1]
except FileNotFoundError as err:
    print(err.args[1])
except KeyError as err:
    print("Something went wrong...")

lessons_dict = {}
try:
    with open(r"C:\Users\HumanAlone\Downloads\tech_quality\lessons.txt", 'r', encoding='utf-8') as f_inp:
        f_inp.readline()
        f_inp.readline()
        for line in f_inp:
            temp = list(map(lambda x: x.strip(), line.split('|')))
            if len(temp) == 4:
                if temp[2] == 'phys':
                    lessons_dict[temp[0]] = [temp[1], from_utc_to_local(temp[3]), participants_dict[temp[1]]]

except FileNotFoundError as err:
    print(err.args[1])
except KeyError as err:
    print("Something went wrong...")

try:
    with open(r"C:\Users\HumanAlone\Downloads\tech_quality\quality.txt", 'r', encoding='utf-8') as f_inp:
        f_inp.readline()
        f_inp.readline()
        for line in f_inp:
            temp = list(map(lambda x: x.strip(), line.split('|')))
            if len(temp) == 2:
                if temp[0] in lessons_dict:
                    if temp[1]:
                        lessons_dict[temp[0]].append([temp[1]])
except FileNotFoundError as err:
    print(err.args[1])
except KeyError as err:
    print("Something went wrong...")
else:
    date_tutor_average_dict = {}
    for value in lessons_dict.values():
        day = value[1].split()[0]
        if len(value) > 3:
            if day not in date_tutor_average_dict:
                date_tutor_average_dict[day] = {value[2]: value[3]}
            else:
                if value[2] in date_tutor_average_dict[day]:
                    date_tutor_average_dict[day][value[2]] += value[3]
                else:
                    date_tutor_average_dict[day][value[2]] = value[3]

    res = {}
    for key, value in date_tutor_average_dict.items():
        res[key] = sorted(value.items(), key=lambda x: sum(list((map(int, x[1])))) / len(x[1]))[0]

    for k, v in sorted(res.items()):
        print(k, v[0], "{:0.2}".format(sum(list(map(int, (v[1])))) / len(v[1])))
