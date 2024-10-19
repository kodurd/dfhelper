import pandas as pd
from dfhelper.viz import df_view, df_info_view, df_shape_view
from dfhelper.scout import summarize_df, summarize_dfs


# viz
df1 = pd.DataFrame(
            {"A": [1, 0, 0, None],
             "B": [1, 1, 2, 2],
             "C": [None, None, None, None]}
        )

df2 = pd.DataFrame(
            {"A": [1, 5, 0, 10],
             "B": [1, 1, 2, 2],
             "C": [None, 4, 16, 101]}
        )

df_view(df1, df2)

df_info_view(df1, df2)

df_shape_view(df1, df2)

# scount
summarize_df(df1)
summarize_dfs(df1, df2)

