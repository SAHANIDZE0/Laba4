import argparse
import csv
import os
import time
import re
import requests
from bs4 import BeautifulSoup

CACHE_DIR = 'cache'

def get_html(country, use_cache=True):
    url_country = country.replace(' ', '_')
    url = f'https://en.wikipedia.org/wiki/{url_country}'
    
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
        
    cache_file = os.path.join(CACHE_DIR, f'{url_country}.html')
    
    if use_cache and os.path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf-8') as f:
            return f.read()
            
    print(f"Загрузка данных для: {country}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        html = response.text
        
        with open(cache_file, 'w', encoding='utf-8') as f:
            f.write(html)
            
        time.sleep(1)
        return html
    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети при загрузке {country}: {e}")
        return None

def clean_number(text):
    if not text:
        return ""
    text = re.sub(r'\[.*?\]', '', text)
    numbers = re.findall(r'\d+', text)
    return ''.join(numbers) if numbers else ""

def parse_country(html):
    if not html:
        return "", "", ""
        
    soup = BeautifulSoup(html, 'html.parser')
    infobox = soup.find('table', class_='infobox')
    
    if not infobox:
        return "", "", ""
        
    capital = ""
    area = ""
    population = ""
    
    for row in infobox.find_all('tr'):
        header = row.find('th')
        data = row.find('td')
        
        if header and data:
            header_text = header.get_text(strip=True).lower()
            data_text = data.get_text(separator=' ', strip=True)
            
            if 'capital' in header_text and not capital:
                capital = data_text.split('[')[0].strip()
            elif 'area' in header_text and not area:
                area = clean_number(data_text)
            elif 'population' in header_text and not population:
                population = clean_number(data_text)
                
    return capital, area, population

def main():
    parser = argparse.ArgumentParser(description="Парсер стран из Википедии")
    parser.add_argument('--input', default='countries.txt', help='Входной файл со списком стран')
    parser.add_argument('--output', default='countries_data.csv', help='Выходной CSV файл')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Файл {args.input} не найден!")
        return

    with open(args.input, 'r', encoding='utf-8') as f:
        countries = [line.strip() for line in f if line.strip()]

    results = []
    for country in countries:
        html = get_html(country)
        if html:
            capital, area, population = parse_country(html)
            results.append({
                'country': country,
                'city': capital,
                'area': area,
                'population': population
            })
        else:
            results.append({
                'country': country,
                'city': '',
                'area': '',
                'population': ''
            })

    with open(args.output, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['country', 'city', 'area', 'population'])
        writer.writeheader()
        writer.writerows(results)
        
    print(f"\nГотово! Данные сохранены в {args.output}")

if __name__ == '__main__':
    main()