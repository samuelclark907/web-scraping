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
    eachptag = soup.find_all('p')

    each_citation = '' 

    for citation in eachptag:
        if citation.find('sup', class_='noprint Inline-Template Template-Fact'):
            eachcit = citation.text.strip()
            eachcitsplit = eachcit.split('[citation needed]')
            # print(eachcitsplit)
            for i in eachcitsplit:
                each_citation += f'{i}\n'
            # for i in eachcitsplit:
            #     pass
                # print(f'Citation needed for {i}')
                # each_citation += f'Citation needed for {i}'
    print(each_citation)            
    return each_citation
    
    



# get_citations_needed_count(url)
get_citations_needed_report(url)


