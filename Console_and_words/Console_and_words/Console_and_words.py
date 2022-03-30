import re # імпорт шаблонів керування регулярних виразівimport docx
import os
from sys import stdin, stdout
from os import path

# -*- coding: utf-8 -*- 
# вираз вище дозволяє відкривати файли, які знаходяться в каталозі, які названі і в назві якої наявні букви, написані кирилицею

# внесення розташування потрібного файлу та його назву

def reuse(): # функція для повторного використання програми
    print ("Повторити виконання програми?")
    print ("1 - так. 2 - ні.")
    k = input()

    if (k == '1'):
         main()
    elif (k == '2'):
         return 0
    else :
         print ("Невірно введений символ.")
         reuse()

def get_file_name(): # функція для отримання шляху до файла, поки не буде підтвердження, що він існує
     while True:
        name = input('Введіть розташування файлу: ')
        if path.exists(name):
            if path.isfile(name):
                return name
            else:
                print("Вказанні дані не являються файлом.")
        else:
            print("Вказаний шлях не існує.")

def main():

    path = get_file_name() # отримання шляху до файлу

    document_text = open(path, 'r', encoding="utf8") # відкриття потрібного файлу з можливістю читання слів написаних кирилицею
    text_string = document_text.read().lower() # збереження файлу у строкову змінну з низьким регістром

    frequency = {} # ініціація пустого словника

    match_pattern_lat = re.findall(r'\b[a-z]{1,15}\b', text_string) # знаходимо всі слова, написані латиницею
    match_pattern_kir = re.findall(r'\b[а-я]{1,15}\b', text_string) # знаходимо всі слова, написані кирилицею

    for word in match_pattern_lat: # цикл для запису в словник всіх слів, написаних латиницею
        count = frequency.get(word,0)
        frequency[word] = count + 1

    for word in match_pattern_kir: # цикл для запису в словник всіх слів, написаних кирилицею
        count = frequency.get(word,0)
        frequency[word] = count + 1
     
    frequency_list = frequency.keys() # зв'язування слів з їхньою частотою
 
    for words in frequency_list: # друк отриманих результатів
        print (words,":", frequency[words])

    k = reuse()
    return k
    
k = 1

while (k!=0) :
    k = main()
    if (k == '1'):
        break
    elif (k == '0'):
        break