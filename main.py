from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def index():
    return {"data":{"name":"sohaib ahmad","age":22}}


@app.get("/about") 
def about():
    return {"data":"about page"} 