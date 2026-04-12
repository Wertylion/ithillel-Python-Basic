# import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    # читаємо файл
    with open(html_file, mode='r', encoding='utf-8') as file:
        text = file.read()

    # очищення від тегів
    cleaned = ""
    inside_tag = False

    for char in text:
        if char == "<":
            inside_tag = True
            continue
        elif char == ">":
            inside_tag = False
            continue

        if not inside_tag:
            cleaned += char

    # прибираємо пусті рядки
    lines = cleaned.splitlines()
    filtered_lines = []

    for line in lines:
        if line.strip():
            filtered_lines.append(line.strip())

    result = "\n".join(filtered_lines)

    # запис у файл
    with open(result_file, mode='w', encoding='utf-8') as file:
        file.write(result)


delete_html_tags('draft.html')