from docling.document_converter import DocumentConverter
import os


def parse_pdf_simple(pdf_path):

    # Проверяем, существует ли файл
    if not os.path.exists(pdf_path):
        print(f"Ошибка: файл '{pdf_path}' не найден!")
        return None

    # Создаём конвертер
    converter = DocumentConverter()

    # Парсим документ
    print(f"\nПарсим файл: {pdf_path}")
    print("Подожди немного, работаем...\n")

    result = converter.convert(pdf_path)

    # Получаем текст в markdown формате
    text = result.document.export_to_markdown()

    return text


# Использование
if __name__ == "__main__":
    print("=" * 50)
    print("PDF ПАРСЕР через Docling")
    print("=" * 50)

    # Запрашиваем путь к файлу
    pdf_file = input("\nВведи путь к PDF файлу: ").strip()

    # Убираем кавычки, если пользователь их добавил
    pdf_file = pdf_file.strip('"').strip("'")

    # Парсим
    text = parse_pdf_simple(pdf_file)

    if text:
        # Выводим весь текст
        print("\n" + "=" * 50)
        print("СОДЕРЖИМОЕ ДОКУМЕНТА:")
        print("=" * 50 + "\n")
        print(text)

        # Спрашиваем, сохранить ли в файл
        save = input("\n\nСохранить результат в файл? (y/n): ").strip().lower()

        if save in ['y', 'yes', 'д', 'да']:
            output_file = input("Имя выходного файла (по умолчанию output.txt): ").strip()
            if not output_file:
                output_file = "output.txt"

            with open(output_file, "w", encoding="utf-8") as f:
                f.write(text)

            print(f"\n✓ Текст сохранён в {output_file}")

        print("\n" + "=" * 50)
        print("Готово!")
