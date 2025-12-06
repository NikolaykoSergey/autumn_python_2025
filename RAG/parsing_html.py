import requests
from bs4 import BeautifulSoup
import textwrap


def fetch_html(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/131.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers, timeout=20)
    resp.raise_for_status()
    return resp.text


def html_to_clean_text(html):

    soup = BeautifulSoup(html, "html.parser")

    # Сносим всё служебное
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # Для Wikipedia основной контент обычно в div с id="bodyContent" или id="mw-content-text"
    main = soup.find(id="mw-content-text") or soup.find(id="bodyContent") or soup.body

    lines = []

    def add_line(text, indent=0, wrap=100):
        text = text.strip()
        if not text:
            return
        wrapped = textwrap.fill(
            text,
            width=wrap,
            subsequent_indent=" " * indent,
            replace_whitespace=True
        )
        lines.append(wrapped)

    # Простейший проход по дереву с сохранением структуры
    for elem in main.descendants:
        # Заголовки
        if elem.name in ["h1", "h2", "h3", "h4"]:
            title = elem.get_text(strip=True)
            if not title:
                continue
            lines.append("")  # пустая строка перед заголовком
            lines.append(title)
            lines.append("-" * len(title))
        # Абзацы
        elif elem.name == "p":
            text = elem.get_text(" ", strip=True)
            add_line(text)
            lines.append("")
        # Элементы списка
        elif elem.name in ["li"]:
            text = elem.get_text(" ", strip=True)
            if text:
                add_line("• " + text, indent=2)

    # Убираем возможные лишние пустые строки подряд
    cleaned_lines = []
    last_empty = False
    for ln in lines:
        if ln.strip() == "":
            if not last_empty:
                cleaned_lines.append("")
            last_empty = True
        else:
            cleaned_lines.append(ln)
            last_empty = False

    return "\n".join(cleaned_lines).strip()


def parse_wikipedia_page(url):

    print(f"Скачиваем: {url}")
    html = fetch_html(url)
    print("Обрабатываем HTML...\n")
    text = html_to_clean_text(html)
    return text


if __name__ == "__main__":
    print("=" * 80)
    print("ПАРСЕР HTML (пример на Википедии)")
    print("=" * 80)

    default_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    url = input(f"\nВведи URL страницы (Enter для примера с Python): ").strip()
    if not url:
        url = default_url

    try:
        text = parse_wikipedia_page(url)
    except Exception as e:
        print(f"\nОшибка при парсинге: {e}")
    else:
        print("\n" + "=" * 80)
        print("РЕЗУЛЬТАТ (первые 1500 символов):")
        print("=" * 80 + "\n")
        print(text[:1500])
        print("\n... (остальное можно сохранить в файл)\n")

        save = input("Сохранить полный текст в файл? (y/n): ").strip().lower()
        if save in ["y", "yes", "д", "да"]:
            fname = input("Имя файла (по умолчанию page.txt): ").strip()
            if not fname:
                fname = "page.txt"
            with open(fname, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"\n✓ Текст сохранён в {fname}")
