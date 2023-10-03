# functions for feature selection

def format_df_green(s, green_value=1):
    if s == green_value: color = 'lightgreen'
    else: color = 'white'
    return 'background-color: %s' % color 

def save_selected(features, name_model, all_labels, results):
    for var in all_labels:
        if var in features:
            results.loc[var, name_model]=1
        else:
            results.loc[var, name_model]=0