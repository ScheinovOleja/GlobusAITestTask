import datetime

from bs4 import BeautifulSoup
import re


def get_deadline_datetime(filename: str):
    with open(filename, "r") as html_file:
        soup = BeautifulSoup(html_file.read(), 'lxml')
        for text in soup.div:
            # TODO регулярка заточена под конкретную задачу парсинга и конкретный формат даты.
            date_from_text = re.search(r'(\d*\d)*.(\d\d)*.\w*\w* (?:[01][0-9]|2[0-3])[.:-][0-5][0-9]', text.text)
            if date_from_text:
                my_datetime = date_from_text.group().replace('.kl', '')
                # TODO так сделано только из-за того, чтобы потом адекватно вставить год в дату
                day = int(my_datetime.split('.')[0])
                month = int(my_datetime.split('.')[1].split(' ')[0])
                hour = int(my_datetime.split(':')[0].split(' ')[1])
                minute = int(my_datetime.split(':')[1])
                # TODO в задании я не совсем понял про год, поэтому по умолчанию будет текущий год
                result_datetime = datetime.datetime(datetime.datetime.now().year, month, day, hour, minute)
                return datetime.datetime.strftime(result_datetime, "%Y-%m-%dT%H:%M:%f")


if __name__ == '__main__':
    print(get_deadline_datetime('source_for_extract_deadline_date_time.html'))
