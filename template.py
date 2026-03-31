import os

# List of folders to create
folders = [
    "src",
    "src/components",
    "src/pipeline",
    "notebook",
    "templates",
    "artifacts",
    "logs"
]

# List of files to create
files = [
    "app.py",
    "requirements.txt",
    "setup.py",
    "README.md",

    "src/__init__.py",
    "src/logger.py",
    "src/exception.py",
    "src/utils.py",

    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",

    "src/pipeline/__init__.py",
    "src/pipeline/train_pipeline.py",
    "src/pipeline/predict_pipeline.py",

    "templates/index.html",
    "templates/home.html"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Folder created: {folder}")

# Create files
for file in files:
    with open(file, 'w') as f:
        pass
    print(f"File created: {file}")