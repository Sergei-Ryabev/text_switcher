import time

import keyboard
import pyperclip


ru_en_layout_map = {
    'А': 'F', 'а': 'f',
    'Б': '<', 'б': ',',
    'В': 'D', 'в': 'd',
    'Г': 'U', 'г': 'u',
    'Д': 'L', 'д': 'l',
    'Е': 'T', 'е': 't',
    'Ё': '~', 'ё': '`',
    'Ж': ':', 'ж': ';',
    'З': 'P', 'з': 'p',
    'И': 'B', 'и': 'b',
    'Й': 'Q', 'й': 'q',
    'К': 'R', 'к': 'r',
    'Л': 'K', 'л': 'k',
    'М': 'V', 'м': 'v',
    'Н': 'Y', 'н': 'y',
    'О': 'J', 'о': 'j',
    'П': 'G', 'п': 'g',
    'Р': 'H', 'р': 'h',
    'С': 'C', 'с': 'c',
    'Т': 'N', 'т': 'n',
    'У': 'E', 'у': 'e',
    'Ф': 'A', 'ф': 'a',
    'Х': '{', 'х': '[',
    'Ц': 'W', 'ц': 'w',
    'Ч': 'X', 'ч': 'x',
    'Ш': 'I', 'ш': 'i',
    'Щ': 'O', 'щ': 'o',
    'Ъ': '}', 'ъ': ']',
    'Ы': 'S', 'ы': 's',
    'Ь': 'M', 'ь': 'm',
    'Э': '"', 'э': "'",
    'Ю': '>', 'ю': '.',
    'Я': 'Z', 'я': 'z',
    ' ': ' ',
}
en_ru_layout_map = {value: key for key, value in ru_en_layout_map.items()}
full_layout_map = ru_en_layout_map|en_ru_layout_map

def replace_and_paste():
    """
    Функция заменяет выделенный текст на новый и возвращает его в буфер обмена.
    :param old_text: Исходный выделенный текст.
    :param new_text: Текст, которым будем заменять старый.
    """
    try:
        # Читаем выделенный текст из буфера обмена
        input_string = pyperclip.paste()
        print(input_string)
        if not input_string:
            raise ValueError("Буфер обмена пуст")
        # Выполняем замену текста
        output_string = ''.join([full_layout_map.get(char, char) for char in input_string])
        # Возвращаем обновленный текст обратно в буфер обмена
        pyperclip.copy(output_string)
        print(f"Выполнено! Текст заменён на:\n{output_string}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def paste_from_clipboard():
    time.sleep(0.2)
    keyboard.press_and_release('ctrl+x')
    time.sleep(0.2)
    replace_and_paste()
    keyboard.press_and_release('ctrl+v')

keyboard.add_hotkey('ctrl+shift', paste_from_clipboard)

# keyboard.wait('ctrl+shift')
if __name__ == '__main__':
    while True:
        time.sleep(0.2)
        pass
           
