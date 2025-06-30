import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import os


class DataAnalyzer:
    def __init__(self, data: pd.DataFrame, level: str):
        self.data = data
        self.level = level
        self.results = {}
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.ASSETS_DIR = os.path.join(self.BASE_DIR, "assets")
        os.makedirs(self.ASSETS_DIR, exist_ok=True)

    def perform_analysis(self):
        try:
            self.basic_description()
            if self.level in ["LEVEL-2", "LEVEL-3"]:
                self.level2_analysis()
            if self.level == "LEVEL-3":
                self.level3_analysis()
        except Exception as e:
            self.results["error"] = str(e)
        return self.results
    
    def basic_description(self):
        self.results["description"] = (
            "This dataset contains transactions occurring between 01/12/2010 and 09/12/2011 "
            "for a UK-based online retailer. It includes InvoiceNo, StockCode, Quantity, UnitPrice, etc."
        )
        self.results["Column_info"] = self.data.dtypes.astype(str).to_dict()
        self.results["Columns"] = self.data.columns.tolist()
        self.results["Facts"] = [
            f"Number of unique customers: {self.data['CustomerID'].nunique()}",
            f"Most frequent country: {self.data['Country'].mode()[0]}"
        ]

    def level2_analysis(self):
        df = self.data.copy()
        df = df[df['Quantity'] > 0]

        # Plot 1: Top 10 Countries
        top_countries = df['Country'].value_counts().head(10)
        plt.figure(figsize=(8, 4))
        sns.barplot(x=top_countries.values, y=top_countries.index, hue=top_countries.index, palette="viridis", legend=False)
        plt.title("Top 10 Countries by Transactions")
        plt.tight_layout()
        plt.savefig(os.path.join(self.ASSETS_DIR, "top_countries.png"))
        self.results["Plot_1"] = os.path.join(self.ASSETS_DIR, "top_countries.png")
        plt.close()

        # Plot 2: Monthly Sales Trend
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'].copy())  # Avoid SettingWithCopyWarning
        monthly_sales = df.set_index('InvoiceDate').resample('MS')['Quantity'].sum()  # Use 'MS' for month-start
        plt.figure(figsize=(8, 4))
        monthly_sales.plot()
        plt.title("Monthly Sales Trend")
        plt.xlabel("Month")
        plt.ylabel("Quantity Sold")
        plt.tight_layout()
        plt.savefig(os.path.join(self.ASSETS_DIR, "monthly_sales.png"))
        self.results["Plot_2"] = os.path.join(self.ASSETS_DIR, "monthly_sales.png")
        plt.close()

        # Plot 3: Top 5 Products
        top_products = df['Description'].value_counts().head(5)
        plt.figure(figsize=(8, 4))
        sns.barplot(x=top_products.values, y=top_products.index, hue=top_products.index, palette="magma", legend=False)
        plt.title("Top 5 Products")
        plt.tight_layout()
        plt.savefig(os.path.join(self.ASSETS_DIR, "top_products.png"))
        self.results["Plot_3"] = os.path.join(self.ASSETS_DIR, "top_products.png")
        plt.close()

    def level3_analysis(self):
        df = self.data.copy()
        df = df[df['Quantity'] > 0]

        # Plot 4: Revenue by Country
        df['Revenue'] = df['Quantity'] * df['UnitPrice']
        revenue_by_country = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(10)
        plt.figure(figsize=(8, 4))
        sns.barplot(x=revenue_by_country.values, y=revenue_by_country.index, hue=revenue_by_country.index, palette="coolwarm", legend=False)
        plt.title("Top Countries by Revenue")
        plt.tight_layout()
        plt.savefig(os.path.join(self.ASSETS_DIR, "revenue_country.png"))
        self.results["Plot_4"] = os.path.join(self.ASSETS_DIR, "revenue_country.png")
        plt.close()

        # Plot 5: Distribution of Unit Price
        plt.figure(figsize=(6, 4))
        plt.xlim(0, 50)
        sns.histplot(df['UnitPrice'], bins=50, color='skyblue')  
        plt.title("Distribution of Unit Price")
        plt.tight_layout()
        plt.savefig(os.path.join(self.ASSETS_DIR, "unit_price_dist.png"))
        self.results["Plot_5"] = os.path.join(self.ASSETS_DIR, "unit_price_dist.png")
        plt.close()

        # Plot 6: Invoice Vs Revenue
        invoice_revenue = df.groupby('InvoiceNo')['Revenue'].sum().sort_values(ascending=False).head(20)
        plt.figure(figsize=(10, 4))
        sns.barplot(x=invoice_revenue.index.astype(str), y=invoice_revenue.values, palette="Set3", legend=False)
        plt.xticks(rotation=90)
        plt.title("Top 20 Invoice by Revenue")
        plt.tight_layout()
        plt.savefig(os.path.join(self.ASSETS_DIR, "invoice_revenue.png"))
        self.results["Plot_6"] = os.path.join(self.ASSETS_DIR, "invoice_revenue.png")
        plt.close()
