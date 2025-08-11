import scrap_helper

# Get the data
ds_dict, ds_df = scrap_helper.scrap_pages('Data science')
ml_dict, ml_df = scrap_helper.scrap_pages('Machine learning')
ai_dict, ai_df = scrap_helper.scrap_pages('Artificial intelligence')

# Combine the data
combined_dict = scrap_helper.combine_dicts([ds_dict, ml_dict, ai_dict])
combined_df = scrap_helper.combine_dfs([ds_df, ml_df, ai_df])

# Save the data
combined_df.to_csv('data2.csv', index=False)

if __name__ == '__main__':
    print('Done')