import os
import pandas as pd

if __name__ == "__main__":
    full_data = pd.DataFrame()
    data_all_dir = './data/all/'
    data_classification_dir = './data/classification/'
    count = 0
    # Read files from all and classification directories
    for path in os.scandir(data_all_dir):
        try:
            file_name = path.name
            df_all = pd.read_json(data_all_dir+file_name)
            df_classification = pd.read_json(data_classification_dir+file_name)
            df_all = pd.concat([df_all, df_classification], axis=1)
            df_all['file_name'] = pd.Series([file_name]).repeat(10).reset_index(drop=True)
            full_data = pd.concat([full_data, df_all])
            count = count + 1
            print(count)
        except Exception as e:
            print(e)

    full_data.to_csv('./data/all_and_classification.csv', index=False)

