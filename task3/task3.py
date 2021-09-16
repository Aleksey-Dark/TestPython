from typing import Optional, Dict, Tuple
from datetime import datetime
import csv
import os


def main():
    request = input('Введите путь к файлу и  даты начала и конца периода:\n')
    try:
        pth, df, dt = request.split()
        print(os.path.isfile(os.path.abspath(pth)))
        if os.path.isfile(os.path.abspath(pth)):
            df = date_format(df)
            dt = date_format(dt)
            if df > dt:
                raise ValueError
            answer = count(pth, df, dt)
            if not answer:
                raise ValueError
            write_result(answer)
        else:
            raise ValueError
    except ValueError:
        print('usage')
    else:
        print('Ok')


def count(file: str, date_from: datetime, date_to: datetime) -> Optional[Dict]:
    """
    Функция анализа данных из log-файла за период времени

    :param file: Имя файла для анализа
    :type file: str

    :param date_from: Начало периода для анализа
    :type date_from: datetime

    :param date_to: Конец периода для анализа
    :type date_from: datetime

    :return: словарь с результатами анализа
    :rtype dict
    """
    result_dct = None
    i = 0
    cur_vol = 0

    with open(file, 'r', encoding='utf-8') as r_file:
        for i_line in r_file:
            if i == 0 or i == 1:
                i += 1
                continue
            elif i == 2:
                i += 1
                cur_vol = int(i_line.split()[0])
            else:
                date, value, result = parsing(i_line)
                if date_from <= date <= date_to:
                    if not result_dct:
                        result_dct = {x: 0 for x in heading}
                        result_dct['Объем воды на начало периода'] = str(cur_vol)

                    if value > 0:
                        result_dct['Количество попыток налить воду'] += 1
                        if result:
                            result_dct['Объем воды налит'] += value
                            cur_vol += value
                        else:
                            result_dct['Объем воды не налит'] += value
                            result_dct['Процент ошибок при наливании воды'] += 1

                    else:
                        result_dct['Количество попыток забора воды'] += 1
                        if result:
                            result_dct['Объем воды забран'] -= value
                            cur_vol += value
                        else:
                            result_dct['Объем воды не забран'] -= value
                            result_dct['Процент ошибок при заборе воды'] += 1

                else:
                    if result_dct:
                        break
        if result_dct:
            result_dct['Объем воды на конец периода'] = str(cur_vol)
            result_dct['Процент ошибок при наливании воды'] = round(
                result_dct['Процент ошибок при наливании воды'] / result_dct['Количество попыток налить воду'] * 100,
                1
            )

            result_dct['Процент ошибок при заборе воды'] = round(
                result_dct['Процент ошибок при заборе воды'] / result_dct['Количество попыток забора воды'] * 100,
                1
            )
        return result_dct


def parsing(line: str) -> Tuple[datetime, int, bool]:
    """
    Функция для сбора данных данных из строки

    :param line: Строка из log-файла
    :type line: str

    :return: Данные для анализа
    :rtype: tuple
    """
    date, _, data = line.split(' - ')
    date = date_format(date)

    data, result = data.split('l')
    if 'успех' in result:
        result = True
    else:
        result = False

    *head, act, value = data.split()
    if 'scoop' in act:
        value = -int(value)
    else:
        value = int(value)

    return date, value, result


def date_format(date: str) -> datetime:
    """
    Функция для преобразования строки даты в объект datetime

    :param date: Строка с датой
    :type date: str

    :return: объект datetime
    :rtype: datetime
    """
    return datetime.strptime(date[:19], '%Y-%m-%dT%H:%M:%S')


def write_result(data: Dict) -> None:
    """
    Функция записи результатов в .csv файл

        :param data: Данные для записи в файл
        :type data: dict
    """

    with open("result.csv", mode="w", encoding='utf-8') as w_file:
        names = heading
        file_writer = csv.DictWriter(w_file, delimiter=",",
                                     lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        file_writer.writerow(data)


heading = [
    'Количество попыток налить воду',
    'Процент ошибок при наливании воды',
    'Объем воды налит',
    'Объем воды не налит',
    'Количество попыток забора воды',
    'Процент ошибок при заборе воды',
    'Объем воды забран',
    'Объем воды не забран',
    'Объем воды на начало периода',
    'Объем воды на конец периода'
]

main()

# '/home/aleksey/PycharmProjects/TestPython/task3/log.log 2021-09-15T11:54:10 2021-09-15T12:06:43.178'
# /home/aleksey/PycharmProjects/TestPython_/task3/log.log 2021-09-15T11:54:10 2021-09-15T12:06:43.178
# /home/aleksey/PycharmProjects/TestPython_/task4/log.log 2021-09-15T11:54:10 2021-09-15T12:06:43.178
# .../TestPython_/task3/log.log 2021-09-15T11:54:10 2021-09-15T12:06:43.178