<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Fraud Detection Analysis - Machine Learning</h1>

<h2>Project Overview</h2>
<p>
    This project focuses on building a machine learning model to detect fraudulent transactions in mobile financial services.
    The goal is to enhance security by developing a model that can predict fraudulent activities in real-time with high accuracy and precision.
</p>
<p>
    The project uses various machine learning algorithms like Logistic Regression, Support Vector Classifier (SVC), Random Forest, and Decision Tree to build a robust fraud detection system.
</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#project-overview">Project Overview</a></li>
    <li><a href="#technologies-used">Technologies Used</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#how-to-run">How to Run</a></li>
    <li><a href="#results">Results</a></li>
    <li><a href="#model-performance">Model Performance</a></li>
    <li><a href="#deployment">Deployment</a></li>
    <li><a href="#contributors">Contributors</a></li>
</ul>

<h2 id="technologies-used">Technologies Used</h2>
<ul>
    <li><strong>Programming Language</strong>: Python</li>
    <li><strong>Libraries</strong>:
        <ul>
            <li>Pandas</li>
            <li>NumPy</li>
            <li>Scikit-learn</li>
            <li>Matplotlib</li>
            <li>Seaborn</li>
        </ul>
    </li>
    <li><strong>Tools</strong>: Jupyter Notebook, Git</li>
</ul>

<h2 id="project-structure">Project Structure</h2>
<p>The project files and their purposes are as follows:</p>
<ul>
    <li><strong>data</strong>: Contains the dataset used for model training and testing.</li>
    <li><strong>notebooks</strong>: Jupyter notebooks with model implementation, data preprocessing, and exploratory data analysis.</li>
    <li><strong>scripts</strong>: Python scripts for model training, hyperparameter tuning, and evaluation.</li>
    <li><strong>images</strong>: Contains visualizations and model performance outputs.</li>
    <li><strong>README.md</strong>: Project documentation.</li>
    <li><strong>requirements.txt</strong>: Required libraries and dependencies.</li>
</ul>

<h2 id="how-to-run">How to Run</h2>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/JayKacha20/Fraud-Detection-Analysis---ML.git
cd Fraud-Detection-Analysis---ML
        </code></pre>
    </li>
    <li>Install dependencies:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Run the Jupyter notebooks for model training:
        <pre><code>jupyter notebook notebooks/</code></pre>
    </li>
    <li>Train and evaluate models using the Python scripts:
        <pre><code>python scripts/train_model.py</code></pre>
    </li>
</ol>

<h2 id="results">Results</h2>
<p>
    The models were trained and evaluated on various metrics such as accuracy, precision, recall, and AUC-ROC score.
    After hyperparameter tuning, the Random Forest model showed the best performance with an accuracy of <strong>XX%</strong> and precision of <strong>YY%</strong>.
</p>

<h2 id="model-performance">Model Performance</h2>
<table>
    <thead>
        <tr>
            <th>Model</th>
            <th>Accuracy</th>
            <th>Precision</th>
            <th>Recall</th>
            <th>F1-Score</th>
            <th>AUC-ROC</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Logistic Regression</td>
            <td>0.998558</td>
            <td>1.000000</td>
            <td>0.875</td>
            <td>0.933333</td>
            <td>0.988102</td>
        </tr>
        <tr>
            <td>Support Vector Classifier (SVC)</td>
            <td>0.996395</td>
            <td>0.823529</td>
            <td>0.875</td>
            <td>0.848485</td>
            <td>N/A</td>
        </tr>
        <tr>
            <td>Random Forest Classifier</td>
            <td>0.995674</td>
            <td>0.777778</td>
            <td>0.875</td>
            <td>0.823529</td>
            <td>0.998541</td>
        </tr>
        <tr>
            <td>Decision Tree Classifier</td>
            <td>0.997116</td>
            <td>0.875000</td>
            <td>0.875</td>
            <td>0.875000</td>
            <td>0.936771</td>
        </tr>
    </tbody>
</table>


<h2 id="deployment">Deployment</h2>
<p>The final model is deployed for real-time fraud detection. Below is an example output of a transaction being classified as fraudulent.</p>
<img src="deployment_output.png" alt="Model Deployment Output" width="500" />

<h2 id="contributors">Contributors</h2>
<ul>
    <li><strong><a href="https://github.com/JayKacha20">Jay Kacha</a></strong> - Data Science Intern</li>
</ul>

</body>
</html>
