from pathlib import Path

import pandas as pd

data_path = Path(__file__).parents[1] / "afe_1.xlsx"


def load_real_gdp() -> pd.DataFrame:
    real_gdp = pd.read_excel(data_path, sheet_name=0).set_index("Date")
    real_gdp = real_gdp.rename(
        columns={"EHGDUSY Index  (R1)": "USA", "EHGDFRY Index  (R2)": "France", "EHGDJPY Index  (L1)": "Japan"}
    ).sort_index()
    return real_gdp.resample("YE").last() / 100


def load_real_interest_rate() -> pd.DataFrame:
    inflation = pd.read_excel(data_path, sheet_name=1).set_index("Date").sort_index()

    inflation = (
        inflation.rename(
            columns={
                "GTFRF10YR @BGN Corp  (R1)": "France_10Y",
                "GJGB10 Index  (L1)": "Japan_10Y",
                "USGG10YR Index  (R2)": "USA_10Y",
                "JNCPIYOY Index  (L2)": "Japan_CPI",
                "FRCPIYOY Index  (L3)": "France_CPI",
                "CPI YOY Index  (R3)": "USA_CPI",
            }
        )
        .resample("YE")
        .last()
    )
    # Values are in bps, and also need to shift nominal rates by 1 year to match w/ inflation rates.
    inflation_rates = inflation[["Japan_CPI", "France_CPI", "USA_CPI"]].div(100)
    nominal_rates = inflation[["Japan_10Y", "France_10Y", "USA_10Y"]].div(100).shift(1)

    # Calculate real interest rates using Fisher equation: r = i - pi, as they are quite close anyway
    return pd.DataFrame(
        (nominal_rates.to_numpy() - inflation_rates.to_numpy()),
        index=inflation_rates.index,
        columns=["Japan", "France", "USA"],
    )


def load_stock_returns() -> pd.DataFrame:
    stock_returns = pd.read_excel(data_path, sheet_name=2).set_index("Date").sort_index()
    stock_returns = stock_returns.rename(
        columns={"CAC Index  (R1)": "France", "NKY Index  (L1)": "Japan", "SPX Index  (R1)": "USA"}
    ).pct_change() 
    return stock_returns.resample("YE").last()


def aggregate_data() -> pd.DataFrame:
    real_gdp = load_real_gdp()
    real_interest_rate = load_real_interest_rate()
    stock_returns = load_stock_returns()

    # Merge the dataframes
    df = real_gdp.merge(real_interest_rate, left_index=True, right_index=True, how="outer", suffixes=("_gdp", "_ir"))
    df = df.merge(stock_returns, left_index=True, right_index=True, how="outer")

    # Drop rows with any NaN values
    df = df.dropna()
    for country in ["Japan", "France", "USA"]:
        df[f"equity_premium_{country}"] = df[f"{country}"] - df[f"{country}_ir"]

    # Melt the dataframe
    df = df.melt(var_name="name", value_name="value", ignore_index=False)

    # Add a column indicating the source
    df["source"] = df["name"].apply(
        lambda x: "real_gdp" if "_gdp" in x else ("real_interest_rate" if "_ir" in x else (
            "equity_premium" if "equity_premium" in x else "stock_returns"
        ))
    )
    df["name"] = df["name"].apply(lambda x: x.replace("_gdp", "").replace("_ir", "").replace("equity_premium_", ""))
    
    df.index.name = "Date"

    return df

if __name__ == "__main__":
    with Path(__file__).parents[2] / "site" / "sources" / "series" / "series_1.csv" as f:
        aggregate_data().to_csv(f)
