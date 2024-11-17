import os
import csv

# Путь к папке с CSV-файлами
folder_path = '.'

# Имена выходных файлов
phones_output_file = 'phones.txt'
emails_output_file = 'emails.txt'

# Списки для хранения телефонов и почт
phones = []
emails = []

# Функция для проверки телефона
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 11 and (phone.startswith('79') or phone.startswith('8'))

# Перебираем все файлы в папке
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            next(reader, None)  # Пропускаем заголовок, если есть
            
            for row in reader:
                if len(row) >= 4:  # Убедимся, что строка содержит нужные колонки
                    phone = row[2].strip() #Укажите в Row номер нужной колонки...
                    email = row[3].strip()

                    if phone and is_valid_phone(phone):
                        phones.append(phone)
                    if email:
                        emails.append(email)

# Сохраняем телефоны в файл
with open(phones_output_file, 'w', encoding='utf-8') as phones_file:
    phones_file.write('\n'.join(phones))

# Сохраняем почты в файл
with open(emails_output_file, 'w', encoding='utf-8') as emails_file:
    emails_file.write('\n'.join(emails))

print(f'Телефоны сохранены в {phones_output_file}')
print(f'Почты сохранены в {emails_output_file}')
