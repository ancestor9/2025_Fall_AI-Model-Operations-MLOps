from fastapi import FastAPI, Depends, Query

app = FastAPI()

# dependency function
def user_dep(
    name: str = Query(..., description="User name"), 
    password: str = Query(..., description="User password")
):
    return {"name": name, "valid": True}

# path function / web endpoint
@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user

# http://127.0.0.1:8000/user?name=alice&password=1234 로 확인