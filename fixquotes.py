import request

newDict={}
with open('baddata.txt','r') as f_open:
    data = f_open.read()
    print(data)
    print(type(data))
    describeStart = data.index('"description":"') + len('"description":"')


    describeEnd = data.find('","date_incorporation"')

    print('description start', describeStart)
    print('description end', describeEnd)

    print(data[describeStart:describeEnd])

    goodDescription = data[describeStart:describeEnd].replace('"', "'")
    print(data[0:describeStart])

    newData = data[0:describeStart] + goodDescription + data[describeEnd:-1]
    print(newData)

    dict = eval(newData)
    print(dict)
    print(type(dict))


    for key in dict:
        newDict["additional_content__"+key] = dict[key]

with open('title.txt','r') as f_open:
    title = f_open.read()
    print(title)
    print(type(title))
    newDict["title"] = title

response = requests.post('', data=newDict)

