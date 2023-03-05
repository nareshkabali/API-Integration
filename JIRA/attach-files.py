import requests

issue_key = 'API-20'
url = 'https://naresh-k.atlassian.net/rest/api/3/issue/'+issue_key+'/attachments'
headers = {'X-Atlassian-Token' : 'nocheck'}
api_key = 'ATATT3xFfGF0-qlBqwB53QklEbFEu3bbRye4_B_OLThaxv1WtOgHsIgFez87rSI-4fhClpvXq3OwFJtqJ_kgdXnv_f_F63URtepjQsS5l03oP5ngccNvkMATS3f-GR82HQ4TIxL3HTWnmWh47CkYEtLx7wfb9A4v0HQBd5w89uQQ9LiyByhPI_k=E1187AAE'
auth = ('nareshkabali.nk@gmail.com', api_key)
files = {'file': open(r'C:\Users\Naresh.K\PycharmProjects\API-Integration\Files\Test Evidences in Excel.xlsx', 'rb')}

data = {
    "fields": {
       "project":
       {
          "key": "API"
       },
       "summary": "API Test - Creating First Defect using Python",
       "description": "Creating a JIRA defect using the python code and REST API",
       "issuetype": {
          "name": "Bug"
       }
   }
}

response = requests.post(url = url,
                         auth = auth,
                         json = data,
                         headers = headers,
                         files = files
                         )
print(response.json())


