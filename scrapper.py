from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def getEntry(div):
    print('Inside getEntry()')
    pass
    return entry


def getAllEntriesFromUrl1(url):
    entries = []
    #
    print('Opening the url...')
    print(url)
    html = urlopen(url)
    print('Opened the url..')
    soup = BeautifulSoup(html, 'lxml')
    candidatesTables = soup.findAll("table", {"class": "taglib-search-iterator"})
    if candidatesTables != None and len(candidatesTables) > 0:
        trTag = candidatesTables[0].find_all('tr', {"class": "results-row"});
        print('Number of trTags that are a good candidate: ' + str(len(trTag)))
        if trTag != None and len(trTag):
            count = 0
            for oneTrTag in trTag:
                tdTag = oneTrTag.findAll('div', {"class": "aui-column-content aui-column-content-last"})
                count = count + len(tdTag)
                if tdTag != None and len(tdTag) > 0:
                    entry = getEntry(oneTrTag)
                    entries.append(entry)
            print('Count = ' + str(count))
    else:
        raise Exception('Did not find a table with class="taglib-search-iterator"')
    return entries

def getAllEntriesFromUrl(url):
    entries = []
    print('Opening the url...')
    print(url)
    html = urlopen(url)
    print('Opened the url..')
    soup = BeautifulSoup(html, 'lxml')
    #inputValue = soup.findAll('input', {"id", "_councillors_WAR_councillorsportlet_csearchContainerPrimaryKeys"})
    inputValue = soup.find('input', {"name": "csearchContainerPrimaryKeys"})
    print('inputValue found..')
    valueInTxt = inputValue.get('value')
    print('got input value')
    parsed_json = json.loads(valueInTxt)
    print('value = ' + str(type(parsed_json)))

def main():
    url = 'http://bbmp.gov.in/en/wardwisecouncliesdetails?p_p_id=councillors_WAR_councillorsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=2&_councillors_WAR_councillorsportlet_keywords=&_councillors_WAR_councillorsportlet_advancedSearch=false&_councillors_WAR_councillorsportlet_andOperator=true&_councillors_WAR_councillorsportlet_resetCur=false&_councillors_WAR_councillorsportlet_delta=198'
    entries = getAllEntriesFromUrl(url)
    pass

if __name__ == '__main__':
    main()
