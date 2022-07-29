from fastapi import FastAPI
from routes.student import student_router

app = FastAPI()

# Register router
app.include_router(student_router)