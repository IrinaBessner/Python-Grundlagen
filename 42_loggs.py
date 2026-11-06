
import logging          #Eine Python-Bibliothek zur Protokollierung von Ereignissen (Logs)

# Настройка логирования - Die Konfiguration des Loggings
logging.basicConfig(

    level=logging.DEBUG,          # welche eine Log-Nachricht dargestellt wird

    format="%(asctime)s - %(filename)s - Zeile %(lineno)d - %(levelname)s - %(message)s",
    handlers=[                     # Ein Logging-Handler (Protokollierungs-Handler), der festlegt, wohin die Log-Nachrichten ausgegeben werden.
        logging.FileHandler("mylog.log", mode="w", encoding="utf-8"),
        logging.StreamHandler()  # gibt die Log-Nachrichten in der Konsole aus, verwendet standardmäßig stderr – den Standardfehlerausgabekanal
    ]
)

# Logging levels - Уровни логирования
logging.debug("Отладка с полной информацией")
logging.info("Программа запущена успешно")
logging.warning("Внимание! Проверьте входные данные")
logging.error("Произошла ошибка Что-то пошло не так")
logging.critical("Критическая ошибка! Программа завершена")

# специальные обозначения для логирования - Formatierungsattribute des Logging-Moduls
#   %(asctime)s	    Datum und Uhrzeit des Log-Eintrags  - Дата и время события 
#   %(filename)s    Name der Python-Datei   -             Имя файла Python 
#   %(lineno)d	    Zeilennummer im Quellcode             Номер строки кода 
#   %(levelname)s	Name der Protokollierungsstufe        Уровень сообщения: DEBUG, INFO и т. д. 
#   %(message)s	    Inhalt der Log-Nachricht              Сам текст сообщения 
#   %(name)s	    Name des Loggers                      Имя логгера
#   %(funcName)s	Name der aufgerufenen Funktion   	  Имя вызванной функции
#   %(module)s	    Name des Moduls	                      Имя модуля
#   %(process)d	    Prozess-ID	                          ID процесса
#   %(thread)d	    Thread-ID (ID des Threads)	          ID потока

#   2026-11-05 14:30:12 - main.py - Zeile 15 - INFO - Программа запущена


# Logging внутри функции
def divide(a, b):
    logging.debug(f"Вызов функции divide({a}, {b})")   # Das f vor einer Zeichenkette kennzeichnet einen sogenannten f-String (formatierte Zeichenkette).
                                                       # Damit können Variablenwerte direkt in einen Text eingefügt werden.
    if b == 0:
        logging.error("Деление на ноль невозможно!")
        return None

    result = a / b
    logging.info(f"Результат: {result}")
    return result


divide(10, 2)
divide(5, 0)


# Logging und Exception Handling
def open_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            logging.info(f"Файл '{filename}' успешно открыт")
            print(f.read())

    except FileNotFoundError:
        logging.error(f"Файл '{filename}' не найден!")

    finally:
        logging.debug("Функция open_file завершена")


open_file("existing_file.txt")
open_file("not_existing_file.txt")
