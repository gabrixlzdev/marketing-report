

def filter_campaings(df, column_campaings, selected_campaings):
    
    filtered_df = df[df[column_campaings].isin(selected_campaings)]

    return filtered_df