# todo: Создайте иерархию классов для экспорта данных в разные форматы.
# Требования:
# Абстрактный базовый класс DataExporter:
#
# Методы:
# export(self, data) - абстрактный метод
# get_format_name(self) - возвращает название формата
# validate_data(self, data) - общий метод проверки данных (не пустые ли)
#
# Конкретные реализации:
# JSONExporter:
# Экспортирует данные в JSON-формат
# Добавляет поле "export_timestamp" с текущим временем
#
# CSVExporter:
# Экспортирует данные в CSV (если data - список словарей)
# Автоматически определяет заголовки из ключей первого элемента
#
# XMLExporter:
# Создает XML структуру с корневым элементом <report>
# HTMLExporter (дополнительно):
# Создает красивую HTML-таблицу с CSS-стилями


# Этот код должен работать после реализации:
# sales_data = [
#     {"product": "Laptop", "price": 1000, "quantity": 2},
#     {"product": "Mouse", "price": 50, "quantity": 10}
# ]
#
# exporters = [
#     JSONExporter(),
#     CSVExporter(),
#     XMLExporter()
# ]
#
# for exporter in exporters:
#     print(f"Формат: {exporter.get_format_name()}")
#     exporter.export(sales_data)
#     print("---")


from abc import ABC, abstractmethod
import json
import csv
import datetime
import xml.etree.ElementTree as ET
from io import StringIO


class DataExporter(ABC):
    @abstractmethod
    def export(self, data):
        pass

    @abstractmethod
    def get_format_name(self):
        pass

    def validate_data(self, data):
        if not data:
            raise ValueError("Ошибка: данные пустые!")


# JSON
class JSONExporter(DataExporter):
    def export(self, data):
        self.validate_data(data)
        data_with_timestamp = {
            "export_timestamp": datetime.datetime.now().isoformat(),
            "data": data
        }
        print(json.dumps(data_with_timestamp, indent=4, ensure_ascii=False))

    def get_format_name(self):
        return "JSON"


# CSV
class CSVExporter(DataExporter):
    def export(self, data):
        self.validate_data(data)
        if not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
            raise TypeError("Для CSV требуется список словарей!")

        output = StringIO()
        fieldnames = data[0].keys()
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

        print(output.getvalue())
        output.close()

    def get_format_name(self):
        return "CSV"


# XML
class XMLExporter(DataExporter):
    def export(self, data):
        self.validate_data(data)
        root = ET.Element("report")

        for item in data:
            entry = ET.SubElement(root, "entry")
            for key, value in item.items():
                elem = ET.SubElement(entry, key)
                elem.text = str(value)

        tree = ET.ElementTree(root)
        xml_str = ET.tostring(root, encoding="unicode")
        print(xml_str)

    def get_format_name(self):
        return "XML"


# HTML
class HTMLExporter(DataExporter):
    def export(self, data):
        self.validate_data(data)

        html = """
        <html>
        <head>
            <style>
                table {{border-collapse: collapse; width: 60%; margin: 10px;}}
                th, td {{border: 1px solid #999; padding: 8px; text-align: left;}}
                th {{background-color: #f2f2f2;}}
            </style>
        </head>
        <body>
            <h2>Отчет</h2>
            <table>
                <tr>{headers}</tr>
                {rows}
            </table>
        </body>
        </html>
        """

        headers = "".join([f"<th>{h}</th>" for h in data[0].keys()])
        rows = ""
        for item in data:
            row = "".join([f"<td>{v}</td>" for v in item.values()])
            rows += f"<tr>{row}</tr>"

        html_filled = html.format(headers=headers, rows=rows)
        print(html_filled)

    def get_format_name(self):
        return "HTML"


sales_data = [
    {"product": "Laptop", "price": 1000, "quantity": 2},
    {"product": "Mouse", "price": 50, "quantity": 10}
]

exporters = [
    JSONExporter(),
    CSVExporter(),
    XMLExporter(),
    HTMLExporter()
]

for exporter in exporters:
    print(f"Формат: {exporter.get_format_name()}")
    exporter.export(sales_data)
    print("---")
