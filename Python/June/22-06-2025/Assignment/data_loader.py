import pandas as pd

class DataLoader:
    def load_data(self):
        file_path = "D:/Krish Naik/Krish Naik Ultimate Data Science RoadMAp Python/Python/June/22-06-2025/Assignment/Online Retail.xlsx" #download from the kaggle or UCI machine learning dataset
        data = pd.read_excel(file_path)
        return data