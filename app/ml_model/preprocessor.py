import pandas as pd


class Preprocessor:
    def __init__(self, feature_order, scaler_X):
        self.feature_order = feature_order
        self.scaler_X = scaler_X

    def transform(self, data: dict):
        df = pd.DataFrame([data])
        df["floor_ratio"] = df["floor"] / df["num_floors"].replace(0, 1)
        df["living_ratio"] = df["living_area"] / df["total_area"].replace(0, 1)
        df = pd.get_dummies(df)
        for col in self.feature_order:
            if col not in df.columns:
                df[col] = 0
        df = df[self.feature_order]
        X_scaled = self.scaler_X.transform(df)
        return X_scaled
