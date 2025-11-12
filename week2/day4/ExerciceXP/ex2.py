import json,os
from pathlib import Path

# Convert __file__ to a Path object
path = Path(__file__)

folder_name = path.parent.name

print(folder_name) 

sampleJson = { 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}

#print the salary value
print(sampleJson["company"]["employee"]["payable"]["salary"])

#add new key to employee dict
sampleJson["company"]["employee"]["birth_date"]="1999-08-27"
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sampleJson.json")

# Save the modified JSON to a file.
with open(file_path, 'w') as file_obj:
    json.dump(sampleJson, file_obj,sort_keys=True)



#read the json modify the salary and write again in to file
with open(file=file_path, mode="r+") as file_obj:
    modified_jsone_file = json.load(file_obj)
    modified_jsone_file["company"]["employee"]["payable"]["salary"]=8000
    file_obj.seek(0)
    json.dump(modified_jsone_file,file_obj,indent=4)
    file_obj.truncate()







 
