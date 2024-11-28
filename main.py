import requests
import datetime

pix="https://pixe.la/v1/users"

USERNAME="lingesh25"
USERTOKEN="lingesh25five"

params={
    "token":USERTOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response=requests.post(url=pix, json=params)
# print(response)
# print(response.text)

graph_endpoint=f"{pix}/{USERNAME}/graphs"

# graph_config={
#     'id':"graph1",
#     'name':'Cycling graph',
#     'unit':'Km',
#     'type':'float',
#     'color':'momiji'
# }
header={
    "X-USER-TOKEN":USERTOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_config,headers=header)
# print(response.text)

adding_data=f"{graph_endpoint}/graph1"

header={
    "X-USER-TOKEN":USERTOKEN
}

now=datetime.datetime.now()
today=now.strftime("%Y%m%d")

add={
    'date':f'{today}',
    'quantity':float(input("How many KM you have cycled?\n"))

}
response=requests.post(url=adding_data,json=add,headers=header)
print(response.text)

# update=f"{adding_data}/{today}"
# params={
#     'quantity':"12.5"
# }

# response=requests.put(url=update,json=params,headers=header)
# print(response.text)

# delet=f"{adding_data}/20240615"
# reponse=requests.delete(url=delet,headers=header)
# print(reponse)
