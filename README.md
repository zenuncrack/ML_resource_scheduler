<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ML Resource Scheduler</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 40px auto;
            padding: 0 20px;
            background-color: #f8f9fa;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code, pre {
            background-color: #eaeaea;
            padding: 4px 8px;
            border-radius: 4px;
            font-family: Consolas, monospace;
        }
        pre {
            overflow-x: auto;
            padding: 10px;
        }
        ul {
            margin: 10px 0 20px 20px;
        }
        a {
            color: #2980b9;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .json {
            background-color: #f1f1f1;
            padding: 10px;
            border-left: 4px solid #2980b9;
        }
    </style>
</head>
<body>
    <h1>ML Resource Scheduler</h1>
    <p>A <strong>FastAPI-based web service</strong> that uses <strong>linear programming with PuLP</strong> to optimally schedule machine learning jobs based on available GPU, CPU, and job priorities. The scheduler efficiently allocates limited resources while maximizing job priorities.</p>

    <h2>Features</h2>
    <ul>
        <li>Schedule ML jobs based on <strong>GPU and CPU constraints</strong>.</li>
        <li>Maximize total <strong>priority of selected jobs</strong>.</li>
        <li>Supports multiple jobs with different <strong>GPU, CPU, RAM requirements, priorities, and deadlines</strong>.</li>
        <li>REST API endpoint to submit jobs and get an optimized schedule.</li>
        <li>Implemented using <strong>Python, FastAPI, and PuLP</strong>.</li>
    </ul>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.9+</li>
        <li>FastAPI</li>
        <li>Uvicorn</li>
        <li>PuLP</li>
    </ul>
    <p>Install dependencies:</p>
    <pre><code>pip install fastapi uvicorn pulp</code></pre>

    <h2>Running the Project</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone &lt;repository_url&gt;
cd ML_resource_scheduler</code></pre>
        </li>
        <li>Activate virtual environment:
            <pre><code>python -m venv myvenv
source myvenv/bin/activate   # Linux/Mac
myvenv\Scripts\activate      # Windows</code></pre>
        </li>
        <li>Install dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Start FastAPI server:
            <pre><code>uvicorn app:app --reload</code></pre>
            Server runs at: <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>
        </li>
        <li>Open API docs: <a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs</a></li>
    </ol>

    <h2>API Endpoint</h2>
    <h3>POST /optimize</h3>
    <p>Submit job requests and get an optimized schedule.</p>

    <p>Request Body Example:</p>
    <pre class="json"><code>{
  "jobs": [
    {"job_id": "J1", "gpu_required": 4, "cpu_required": 16, "ram_required": 32, "priority": 3, "deadline": 8},
    {"job_id": "J2", "gpu_required": 2, "cpu_required": 8, "ram_required": 16, "priority": 1, "deadline": 5},
    {"job_id": "J3", "gpu_required": 6, "cpu_required": 12, "ram_required": 24, "priority": 2, "deadline": 10},
    {"job_id": "J4", "gpu_required": 1, "cpu_required": 4, "ram_required": 8, "priority": 2, "deadline": 12}
  ],
  "total_gpu": 8,
  "total_cpu": 32
}</code></pre>

    <p>Response Example:</p>
    <pre class="json"><code>{
  "schedule": {
    "J1": 1,
    "J2": 1,
    "J3": 0,
    "J4": 1
  }
}</code></pre>

    <p><strong>1</strong> → job selected<br>
       <strong>0</strong> → job not selected</p>

    <h2>How It Works</h2>
    <ol>
        <li>Receives a list of jobs and total resources (GPU/CPU).</li>
        <li>Creates a <strong>linear programming problem</strong> using PuLP.</li>
        <li>Decision variables represent whether a job is selected (binary 0/1).</li>
        <li>Objective: maximize total job priority.</li>
        <li>Constraints: total GPU and CPU usage ≤ available resources.</li>
        <li>Solves the LP problem and returns a schedule indicating which jobs to run.</li>
    </ol>

    <h2>File Structure</h2>
    <pre><code>ML_resource_scheduler/
│
├─ app/
│   ├─ app.py          # FastAPI application
│   └─ optimizer.py    # PuLP optimization logic
│
├─ requirements.txt
└─ README.html</code></pre>

    <p>Enjoy efficiently scheduling your ML workloads! 🚀</p>
</body>
</html>
