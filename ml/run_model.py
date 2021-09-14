import sys
from os.path import join, dirname
sys.path.append(dirname(dirname(__file__)))
from ml.data_loading import DataLoading
from ml.data_transform import DataTransform
from ml.feature_transform_train import Train



class RunModel:
    def __init__(self,artifacts_path):
        try:
          self.artifacts_dir=artifacts_path
        except Exception  as e:
            print(f"ERROR: {e}")


    def run(self):
        try:
            print("Data Loading Started")
            merged_data = DataLoading().load_data()
            print("Data Loading Completed")
            print("Data Transformation Started")
            dataset, X_train, X_test, y_train, y_test=DataTransform(merged_data).transform()
            print("Data Transformation Completed")
            model=Train().model_fit(X_train,y_train)
            Train().save_model(model)
            print("Model saved Successfully")
            # saving the Train data and test data for future use
            X_train.to_csv(join(self.artifacts_dir,"X_train.csv"))
            X_test.to_csv(join(self.artifacts_dir, "X_test.csv"))
            y_train.to_csv(join(self.artifacts_dir, "y_train.csv"))
            y_test.to_csv(join(self.artifacts_dir, "y_test.csv"))
            dataset.to_csv(join(self.artifacts_dir, "dataset.csv"))
            print("Artifacts Successfully")
        except Exception  as e:
            print(f"ERROR: {e}")


artifacts_dir= join(dirname(__file__), "artifacts")

if __name__ == '__main__':
    print("Starting the Run Model")
    RunModel(artifacts_dir).run()
    print("Run Model Completed")
