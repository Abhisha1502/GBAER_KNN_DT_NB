import pandas as pd


def create_pollution_severity(df):
    """
    Create Pollution Severity target variable
    based on CO2 Emissions (in MT)
    """
    pollution_col = 'CO2 Emissions (in MT)'

    df['Pollution_Severity'] = pd.qcut(
        df[pollution_col],
        q=3,
        labels=['Low', 'Medium', 'High'],
        duplicates='drop'
    )

    return df
