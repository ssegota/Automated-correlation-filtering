import pandas as pd






def remove_low_corr_inputs(df, LIMIT=0.01):
# removes those inpus which are not correlated with the target
# assumes target is at 0th column
    # create a correlation matrix using pearson

    corr_p = df.corr(method='pearson')

    # do the same with spearman

    corr_s = df.corr(method='spearman')

    # and kendall

    corr_k = df.corr(method='kendall')

    low_corr = []

    for i in range(1, len(corr_p)):
        if abs(corr_p.iloc[0, i]) < 0.01:
            low_corr.append(i)
        if abs(corr_s.iloc[0, i]) < 0.01:
            low_corr.append(i)    
        if abs(corr_k.iloc[0, i]) < 0.01:
            low_corr.append(i)

    # remove duplicates from the list
            
    low_corr = list(set(low_corr))

    print(low_corr)

    df = df.drop(df.columns[low_corr], axis=1)
    return df

def remove_high_corr_inputs(df, LIMIT=0.95):

# removes thos inputs which are highly correlated with each other
# assumes target is at 0th column

    # create a correlation matrix using pearson

    corr_p = df.corr(method='pearson')

    # do the same with spearman

    corr_s = df.corr(method='spearman')

    # and kendall

    corr_k = df.corr(method='kendall')

    # for eacch correlation matrix, note variables which have a correlation higher than 0.95, excluding column 0 Save them to a list

    high_corr_p = []

    high_corr_s = []

    high_corr_k = []

    for i in range(1, len(corr_p)):
        for j in range(i + 1, len(corr_p)):
            if abs(corr_p.iloc[i, j]) > LIMIT:
                high_corr_p.append(j)

            if abs(corr_s.iloc[i, j]) > LIMIT:
                high_corr_s.append(j)

            if abs(corr_k.iloc[i, j]) > LIMIT:
                high_corr_k.append(j)


    # remove duplicates from the lists
                
    high_corr_p = list(set(high_corr_p))

    high_corr_s = list(set(high_corr_s))

    high_corr_k = list(set(high_corr_k))

    # create a union of the three lists

    high_corr = list(set(high_corr_p + high_corr_s + high_corr_k))

    # remove duplicates from the union

    high_corr = list(set(high_corr))
    print(high_corr)
    # drop columns in high_corr from the dataframe

    df = df.drop(df.columns[high_corr], axis=1)
    return df

# pd read wdbc.data as CSV

df = pd.read_csv('wdbc.data', header=None)

# drop first column

df = df.drop(df.columns[0], axis=1)

# replace M and B with 1 and 0

df[1] = df[1].replace('M', 1)

df[1] = df[1].replace('B', 0)

df = remove_low_corr_inputs(df)

df = remove_high_corr_inputs(df)
df = remove_low_corr_inputs(df)

# save df to file named filtered_ wdbc.data

df.to_csv('filtered_wdbc.data', index=False, header=False)