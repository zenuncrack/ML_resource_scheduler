<body>

<h1>📘 ML Resource Scheduler</h1>
<p>A FastAPI web service that uses <strong>PuLP</strong> to optimally schedule machine learning jobs based on available GPU, CPU, and job priorities. The scheduler efficiently allocates limited resources while maximizing job priorities.</p>

<hr>

<h2>🚀 Features</h2>
<ul>
    <li>🖥️ Schedule ML jobs based on GPU and CPU constraints</li>
    <li>📊 Maximize total priority of selected jobs</li>
    <li>📄 Supports multiple jobs with different GPU, CPU, RAM, priorities, and deadlines</li>
    <li>🌐 REST API endpoint to submit jobs and get an optimized schedule</li>
    <li>⚙️ Implemented using Python, FastAPI, and PuLP</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>

<pre>
├── app/
│   ├─ app.py          # FastAPI application
│   └─ optimizer.py    # PuLP optimization logic
├── requirements.txt   # Dependencies
└── README.html        # This file
</pre>

<hr>

<h2>⚙️ How It Works</h2>

<h3>1️⃣ Job Submission</h3>
<p>User sends a POST request with job details and available resources:</p>

<pre><code>POST /optimize
{
  "jobs": [...],
  "total_gpu": 8,
  "total_cpu": 32
}</code></pre>

<h3>2️⃣ Optimization</h3>
<ul>
    <li>Create a linear programming problem using PuLP</li>
    <li>Decision variables represent whether each job is selected (binary 0/1)</li>
    <li>Objective: maximize total job priority</li>
    <li>Constraints: total GPU and CPU usage ≤ available resources</li>
    <li>PuLP solver finds the optimal set of jobs</li>
</ul>

<h3>3️⃣ Response</h3>
<p>Returns a schedule indicating which jobs to run:</p>

<pre><code>{
  "schedule": {
    "J1": 1,
    "J2": 1,
    "J3": 0,
    "J4": 1
  }
}</code></pre>

<p><strong>1</strong> → job selected<br>
<strong>0</strong> → job not selected</p>

<hr>

<h2>💻 Running the App</h2>

<h3>1️⃣ Install dependencies</h3>
<pre><code>pip install fastapi uvicorn pulp</code></pre>

<h3>2️⃣ Run FastAPI server</h3>
<pre><code>uvicorn app:app --reload</code></pre>
<p>Server runs at: <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a></p>

<h3>3️⃣ Test API</h3>
<p>Use <a href="http://127.0.0.1:8000/docs">Swagger UI</a> to send POST requests and get optimized schedules.</p>

<hr>

<h2>📦 Example Request (JSON)</h2>
<pre><code>{
  "jobs": [
    {"job_id": "J1", "gpu_required": 4, "cpu_required": 16, "ram_required": 32, "priority": 3, "deadline": 8},
    {"job_id": "J2", "gpu_required": 2, "cpu_required": 8, "ram_required": 16, "priority": 1, "deadline": 5},
    {"job_id": "J3", "gpu_required": 6, "cpu_required": 12, "ram_required": 24, "priority": 2, "deadline": 10},
    {"job_id": "J4", "gpu_required": 1, "cpu_required": 4, "ram_required": 8, "priority": 2, "deadline": 12}
  ],
  "total_gpu": 8,
  "total_cpu": 32
}</code></pre>

<h2>📜 License</h2>
<p>This project is open-source and free to modify.</p>

</body>
</html>
