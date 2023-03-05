import requests

issue_id = 'API-20'
api_key = 'ATATT3xFfGF0-qlBqwB53QklEbFEu3bbRye4_B_OLThaxv1WtOgHsIgFez87rSI-4fhClpvXq3OwFJtqJ_kgdXnv_f_F63URtepjQsS5l03oP5ngccNvkMATS3f-GR82HQ4TIxL3HTWnmWh47CkYEtLx7wfb9A4v0HQBd5w89uQQ9LiyByhPI_k=E1187AAE'
auth = ('nareshkabali.nk@gmail.com', api_key)

url = 'https://naresh-k.atlassian.net/rest/api/2/issue/'+str(issue_id)
response = requests.get(url=url,
                        auth = auth,)

issue_summary = response.json()['fields']['summary']
issue_desc = response.json()['fields']['description']
issue_assignee = response.json()['fields']['assignee']['displayName']
attachment_name = response.json()['fields']['attachment'][0]['filename']
attachment_url = response.json()['fields']['attachment'][0]['content']

print(f'Issue Summary is ---> {issue_summary}')
print(f'Issue Description is ---> {issue_desc}')
print(f'Issue Assignee is ---> {issue_assignee}')
print(f'Attachment name is ---> {attachment_name}')
print(f'Attachment URL is ---> {attachment_url}')