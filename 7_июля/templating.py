from docxtpl import DocxTemplate

# загрузили шаблон
doc = DocxTemplate('../docs/template.docx')

# данные для подстановки в него
content = {
    'company': 'ИП Монолит',
    'employee': 'Лакуй Е.А.',
    'position': 'инженер',
    'date': '01/01/2025'
}

doc.render(content)
doc.save('../docs/info.docx')
