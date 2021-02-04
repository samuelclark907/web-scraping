import requests
from bs4 import BeautifulSoup as bs

url = 'https://en.wikipedia.org/wiki/Cryptocurrency'



def get_citations_needed_count(enter_url):
    response = requests.get(enter_url)
    content = response.content
    soup = bs(content, 'html.parser')
    result = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    total_results = len(result)
    print(f'{total_results} citataions needed')
    return total_results

def get_citations_needed_report(enter_url):
    response = requests.get(enter_url)
    content = response.content
    soup = bs(content, 'html.parser')
    allcits = soup.find('p')
    print(allcits.strip())
    



# get_citations_needed_count(url)
get_citations_needed_report(url)


