import pandas as pd
from tqdm.notebook import tqdm
import os

class MakeMeta:
    def __init__(self, main_dir: str, **kwargs) -> None:
        """_summary_

        Args:
            main_dir (str): _description_
        """
        self.create_main = kwargs.get('main_count_meta', True)
        self.sub_dir = kwargs.get('sub_dir', "train_landmark_files")
        self.main_dir = kwargs.get('main_dir', main_dir)
        self.csv_name = kwargs.get('csv_name', "train.csv")
        self.df = pd.read_csv(main_dir + "/" + self.csv_name)
    

    def create_meta(self) -> pd.DataFrame():
        """_summary_

        Args:
            self (_type_): _description_
        """
        output_df = pd.DataFrame()
        for i, row in tqdm(self.df.iterrows(), total=len(self.df)):
            temp_df_pq = pd.read_parquet(f"{os.getcwd()}/{row['path']}")
            output_df = temp_df_pq["type"].value_counts().to_dict()
            dict_test = temp_df_pq.agg({"x": ["min", "max", "mean"],
                                        "y": ["min", "max", "mean"],
                                        "z": ["min", "max", "mean"],
                                        }).unstack().to_dict()
            for key, value in dict_test.items():
                output_df[key[0] + "_" + key[1]] = value
            output_df["frames_unique_count"] = temp_df_pq["frame"].nunique()
            output_df["file"] = row['path']




        

        


        