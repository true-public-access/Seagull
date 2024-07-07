import json
def updateset(key,new_value, *, ind=1 ):
    
    import json 
    
# first, get the absolute path to json file
    PATH_TO_JSON = 'setings/setings.json' #  assuming same directory (but you can work your magic here with os.)

# read existing json to memory. you do this to preserve whatever existing data. 
    with open(PATH_TO_JSON,'r') as jsonfile:
        json_content = json.load(jsonfile)
    
   

    json_content[key] = new_value

    with open(PATH_TO_JSON,'w') as jsonfile:
        json.dump(json_content, jsonfile, indent=ind)


def rdset(key):
    import json
 
# Opening JSON file
    with open('setings/setings.json', 'r') as openfile:
 
    # Reading from json file
        json_object = json.load(openfile)

    return json_object[key]
    
def readallset():
    keys= []
    values=[]
    import json
 
# Opening JSON file
    with open('setings/setings.json', 'r') as openfile:
        jdata=json.load(openfile)
    
        for key, value in jdata.items(): 
            keys.append(key)
            values.append(value) 
    return keys,values 



if __name__ == "__main__":
    print(readallset())
    



