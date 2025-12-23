from fastapi import FastAPI

app = FastAPI()

class person:
    
    name = "priti"
     
    def __init__(self,name:str):
        self.name = name
    
    
# pname = "priti"

def get_person_name(one_person:person):
    return one_person.name

@app.get("/")
def read_root():
    p = person("priti")
    return {"name": get_person_name(p)}

# get_person_name(pname)