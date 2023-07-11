import time

from googleapiclient.discovery import build
import csv

api_key='AIzaSyDAFEg7SzB5EBjgQkgbTr3OEAJmaXiBM9A'
resource = build("customsearch", 'v1', developerKey=api_key).cse()
with open(r'consulting_companies_cleaned.csv', 'r') as file:
    reader = csv.reader(file)
    raw_data = list(reader)
    data=[]
    i=0
    for counter, row in enumerate(raw_data):
        name = row[0]
        web_link=row[1]
        query = f'site:www.linkedin.com/in/ AND "{name}" AND partner'
        time.sleep(1)
        result = resource.list(q=query, cx='738614f36fb84493d').execute()
        try:
            for count, r in enumerate(result['items']):
               title=r['title']
               link=r['link']
               description=r['snippet']
               meta=r['pagemap']['metatags'][0]['og:description']
               data.append([link, web_link, title, name, description, meta])
               i+=1
               if count==4:
                   break
            print(name)
        except:
            print(f'ERROR: {query}')

with open('consulting_people_new_raw.csv', 'w', encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerows(data)