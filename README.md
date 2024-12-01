# Analysis-of-the-distribution-pattern-of-shared-bicycles
This is the final project for ECE143. The goal of this project is to analyze the existing (Washington, DC) bikeshare distribution patterns, identify characteristics associated with the distribution patterns, and attempt to predict optimal future deployment strategies.

## Quick Start
1. Clone this repo
```
git clone https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles.git
cd Analysis-of-the-distribution-pattern-of-shared-bicycles-main
```

2. Please download the corresponding data on **[Kaggle](https://www.kaggle.com/datasets/taweilo/capital-bikeshare-dataset-202005202408/data)** and put the data in the [sources folder](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/tree/main/sources).

3. Run the [data_analysis.py](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/data_analysis.py) file, which will generate all the .csv files used for visualization and model training
```
python data_analysis.py
```

4. Run the [Visualization and Prediction Models.ipynb](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/Visualization%20and%20Prediction%20Models.ipynb) file, which will visualize the analysis results and train a model that can be used to predict future bike rental volume.

## File Description
**[data_analysis.py](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/data_analysis.py)**: This file integrates all the modules for data analysis. It will generate all the .csv files for model training and data visualization.

**[Visualization and Prediction Models.ipynb](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/Visualization%20and%20Prediction%20Models.ipynb)**: This file integrates all the codes for data visualization and model training. Please run [data_analysis.py](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/data_analysis.py) before running this file.

**[data_analysis.ipynb](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/data_analysis.ipynb)**: This file is the original file used for data analysis. It integrates all the codes in this project, including the abandoned parts. It also contains some conclusions of this analysis. If you are interested, you can take a look at it.

**[Member_new.ipynb](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/Member_new.ipynb)**: This file is a supplementary file for membership analysis, and its content has been integrated into [Visualization and Prediction Models.ipynb](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/Visualization%20and%20Prediction%20Models.ipynb).

**[sources](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/tree/main/sources)**: This folder is used to store the original data. You should download the original data on **[Kaggle](https://www.kaggle.com/datasets/taweilo/capital-bikeshare-dataset-202005202408/data)** and put it in this folder.




### Attention！！！
If you need to upload new code, please synchronize the local repository first, add changes, and then send a pull request. Otherwise, the latest progress may be lost. **Please pay attention!!!**

**If you are using GitHud for the first time, [read this](https://docs.github.com/en).**

### The directory structure is as follows：
```
/main/
├── data_analysis.ipynb
├── sources
│   ├── data1.csv
│   ├── data2.csv
│   └── ...
├── YOUR FOLDER
│   ├── YOUR_CODE.ipynb
│   └── ...
└── ...
```
