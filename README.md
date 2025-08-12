<h1 align="center">🩺 Medical AI Agent</h1>

<p align="center">
  <strong>Your AI-powered Medical Data & Information Assistant</strong><br>
  Query heart disease, cancer, and diabetes datasets or get general medical information – all in one place.
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
Medical AI Agent is a multi-tool system that intelligently processes user questions about medical datasets and general health information.  
It detects whether you want <strong>data analysis</strong> from local CSV datasets or <strong>general medical knowledge</strong> and routes your query accordingly.
</p>

<ul>
  <li>❤️ <strong>Heart Disease Tool</strong>: Analyze heart disease dataset with SQL queries</li>
  <li>🎗️ <strong>Cancer Tool</strong>: Explore cancer statistics and patterns</li>
  <li>💉 <strong>Diabetes Tool</strong>: Study diabetes trends and metrics</li>
  <li>🌐 <strong>Medical Info Search Tool</strong>: Get general offline medical facts</li>
</ul>

<hr>

<h2>🚀 Features</h2>

<ul>
  <li>📊 Automatic CSV → SQLite conversion at startup</li>
  <li>🧠 Intent detection for dataset queries vs. general health info</li>
  <li>💬 Human-friendly natural language answers</li>
  <li>⚙️ Built with <code>Python</code> and <code>Pandas</code></li>
</ul>

<hr>

<h2>🧠 How It Works</h2>

<ol>
  <li>CSV files (heart, cancer, diabetes) are automatically converted to SQLite databases</li>
  <li>The <code>MedicalAIAgent</code> receives your query</li>
  <li>It detects if you are asking for <strong>statistics</strong> or <strong>medical info</strong></li>
  <li>Data questions are routed to the right database tool, while general questions go to the offline medical info tool</li>
</ol>

<hr>

<h2>📂 Folder Structure</h2>

<pre>
medical-ai-agent/
│
├── databases/               ← Auto-generated SQLite DBs
├── medical_agent.py         ← Main script
├── heart.csv
├── The_Cancer_data_1500_V2.csv
├── diabetes.csv
├── requirements.txt
└── README.md
</pre>

<hr>

<h2>⚙️ Setup Instructions</h2>

<ol>
  <li>Clone the repository</li>
  
  <pre><code>git clone https://github.com/yourusername/medical-ai-agent</code></pre>

  <li>Install dependencies</li>

  <pre><code>pip install -r requirements.txt</code></pre>

  <li>Place your CSV files in the project root</li>

  <pre>
heart.csv
The_Cancer_data_1500_V2.csv
diabetes.csv
  </pre>

  <li>Run the program</li>

  <pre><code>python medical_agent.py</code></pre>
</ol>

<hr>

<h2>🧪 Sample Queries</h2>

<ul>
  <li><code>What is the average age in heart dataset?</code></li>
  <li><code>What are the symptoms of cancer?</code></li>
  <li><code>Show the average BMI in diabetes dataset</code></li>
</ul>

<hr>

<h2>🙌 Credits</h2>

<p>
Created by <strong>Mehadi Hassan</strong> using Python, Pandas, and SQLite for efficient medical data analysis.
</p>

<hr>

<p align="center">⭐ Star this repo if you find it useful for medical data insights!</p>
