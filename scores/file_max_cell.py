import pandas as pd

def file_max_cell(filename, column):
    df = pd.read_csv(filename)
    df_s = df.sort_values(by= column)

    return df_s.loc[df_s.index[-1], column], df_s.iloc[-1]