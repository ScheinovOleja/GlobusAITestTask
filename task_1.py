import re

from docx import Document


# TODO вынес в доп функцию, чтобы не было сильной нагрузки и вложенности в основной
def check_category(row_text):
    if 'Stillingskategori' in row_text:
        roles = dict()
        for text in row_text:
            my_text = re.findall(r'(\d{1,} \w{10,})', text)
            for role in my_text:
                roles[role.split(' ')[1]] = int(role.split(' ')[0])
        if roles:
            return roles


def parse_doc(filename: str):
    document = Document(filename)
    for table in document.tables:
        for row in table.rows:
            row_text = set(cell.text for cell in row.cells)
            roles = check_category(row_text)
            if roles:
                return roles


if __name__ == '__main__':
    print(parse_doc('source_document_for_multiple_needs__roles_with_positions_amount.docx'))
