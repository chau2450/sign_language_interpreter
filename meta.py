import pandas as pd

class MakeMeta:
    def __init__(self, main_dir: str, sub_dir: str, **kwargs) -> None:
        self.create_main = kwargs.get('main_count_meta', True)
        self.sub_dir = kwargs.get('sub_dir', sub_dir)
        self.main_dir = kwargs.get('main_dir', main_dir)
    

    def create_meta(self) -> pd.DataFrame():


        