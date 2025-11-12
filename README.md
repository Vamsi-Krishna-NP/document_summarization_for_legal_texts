# document_summarization_for_legal_texts

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the app.py
8. Update the main.py

---

## Project Overview

This repository provides tools for summarizing legal documents using deep learning (T5 model). It includes:
- A Streamlit web app for interactive summarization (`app.py`)
- A modular pipeline for data ingestion, validation, transformation, and model training (`main.py`)
- Research notebooks for experimentation (`research/`)
- Configuration and parameters via YAML files
- Pre-built data and model artifacts

## Directory Structure

```
├── app.py                # Streamlit web app
├── main.py               # Pipeline runner
├── requirements.txt      # Python dependencies
├── Dockerfile            # Containerization (edit to use)
├── setup.py              # Install as package (optional)
├── config/               # YAML configuration files
├── params.yaml           # Training parameters
├── artifacts/            # Data, models, tokenizer, etc.
├── datascience/          # Source code (components, pipeline, utils)
├── research/             # Jupyter notebooks
```

## Data Setup

The pipeline expects legal summary data. By default, it will download and unzip the dataset from:
```
https://github.com/Vamsi-Krishna-NP/Just_datasets/raw/main/legal_summary.zip
```
You can change the source URL in `config/config.yaml`.

## How to Download and Run

### Download the Repository

```powershell
git clone https://github.com/Vamsi-Krishna-NP/document_summarization_for_legal_texts.git
```
Or download as a ZIP from GitHub and extract it.

### Install Dependencies

Navigate to the project directory and install required packages:

```powershell
cd document_summarization_for_legal_texts
pip install -r requirements.txt
```

### Run the Streamlit App

```powershell
streamlit run app.py
```

### Run the Training Pipeline

```powershell
python main.py
```

## Docker Usage (Optional)

Edit the `Dockerfile` to match your environment, then build and run:

```powershell
docker build -t legal-summarizer .
docker run -p 8501:8501 legal-summarizer
```

## Install as a Package (Optional)

```powershell
pip install .
```

## Research Notebooks

See the `research/` folder for step-by-step experiments and trials.

---

## Configuration

Edit `config/config.yaml` and `params.yaml` to customize data paths, model parameters, and training options.

---
  
## How to Download and Run

### Download the Repository

You can download this repository using Git:

```powershell
git clone https://github.com/Vamsi-Krishna-NP/document_summarization_for_legal_texts.git
```

Or download as a ZIP from GitHub and extract it.

### Install Dependencies

Navigate to the project directory and install required packages:

```powershell
cd document_summarization_for_legal_texts
pip install -r requirements.txt
```

### Run the Application

To start the main application:

```powershell
python app.py
```

Or run the main pipeline:

```powershell
python main.py
```