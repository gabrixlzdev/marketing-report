

def filter_campaings(df, column_campaings, selected_campaings):
    
    filtered_df = df[df[column_campaings].isin(selected_campaings)]

    return filtered_df

def calculate_summary(df_filtered, config) -> dict:
    summary = {
        "total_spend": df_filtered[config["spend"]].sum(),
        "total_impressions": df_filtered[config["impressions"]].sum(),
        "total_reach": df_filtered[config["reach"]].sum(),
        "total_clicks": df_filtered[config["clicks"]].sum(),
        "total_conversions": df_filtered[config["conversions"]].sum(),
        "avg_cpl": df_filtered[config["cost_per_lead"]].mean(),
        "real_cpl": df_filtered[config["spend"]].sum()/df_filtered[config["conversions"]].sum() if df_filtered[config["conversions"]].sum() > 0 else 0,
        "total_new_contacts": df_filtered[config["new_contacts"]].sum()
    }

    return summary