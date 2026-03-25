import pickle

from pytorch_tabnet.tab_model import TabNetRegressor

from app.ml_model.preprocessor import Preprocessor


class Prediction_model:
    def __init__(self):
        self.model = TabNetRegressor()
        self.model.load_model("app/ml_model/tabnet_model.zip")
        with open("app/ml_model/scaler_X.pkl", "rb") as f:
            self.scaler_X = pickle.load(f)
        with open("app/ml_model/scaler_y.pkl", "rb") as f:
            self.scaler_y = pickle.load(f)
        with open("app/ml_model/feature_order.pkl", "rb") as f:
            self.feature_order = pickle.load(f)
        self.preprocessor = Preprocessor(feature_order=self.feature_order, scaler_X=self.scaler_X)

    def predict(self, data: dict) -> float:
        X_scaled = self.preprocessor.transform(data)
        pred_scaled = self.model.predict(X_scaled).flatten()
        pred_price = self.scaler_y.inverse_transform(pred_scaled.reshape(-1, 1)).flatten()[0]
        return float(pred_price)
