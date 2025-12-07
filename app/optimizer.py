import pulp

def optimizer_pulp(jobs, total_gpu, total_cpu):
 
    model = pulp.LpProblem("ML_Resource_Scaling", pulp.LpMaximize)

    
    x = {j.job_id: pulp.LpVariable(f"x_{j.job_id}", 0, 1, pulp.LpBinary) for j in jobs}

   
    model += pulp.lpSum([j.priority * x[j.job_id] for j in jobs])

    
    model += pulp.lpSum([j.gpu_required * x[j.job_id] for j in jobs]) <= total_gpu
    model += pulp.lpSum([j.cpu_required * x[j.job_id] for j in jobs]) <= total_cpu

    
    model.solve()

    
    return {j.job_id: int(pulp.value(x[j.job_id])) for j in jobs}
