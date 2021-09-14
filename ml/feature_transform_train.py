from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
import pandas as pd
import joblib
from os.path import join, dirname


model_dir= join(dirname(__file__), "artifacts")

class Train:
    """   I Know you have asked to Normaliztion Of test data and train data  items individually
    but am using pipeline do the job for me , no need to manually transform the data
    have just given sample code how to normalize individually : also refer jupyter notebook
    """
    def __init__(self):
        """
        scaler = MinMaxScaler(feature_range=(0, 1))
        df_np = scaler.fit_transform(X_train.to_numpy().reshape(-1, 1))
        X_train_n = pd.DataFrame(df_np.reshape(12289, -1), columns=X_train.columns)
        """
        self.pipe = make_pipeline(MinMaxScaler(), LinearRegression())
        self.model_dir = model_dir

    def model_fit(self,X_train,y_train):
        self.pipe.fit(X_train, y_train)  # apply scaling on training data
        return self.pipe
    def save_model(self,model):
        joblib.dump(model, join(self.model_dir,'models.pkl'))

