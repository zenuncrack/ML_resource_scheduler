from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from optimizer import optimizer_pulp


app = FastAPI()

class Job(BaseModel):
    job_id: str
    gpu_required: int 
    cpu_required: int 
    ram_required: int=0
    priority:int=1
    deadline:int =10 

class JobRequest(BaseModel):
    jobs: List[Job]
    total_gpu:int 
    total_cpu:int 


@app.post("/optimize")
def schedule_jobs(req:JobRequest):
    result = optimizer_pulp(req.jobs, req.total_gpu,req.total_cpu)
    return{'schedule':result}