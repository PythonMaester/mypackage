def stop_words_http_remover(df):  
    '''
    replace split(), lower()
    '''      
    #tokenising the strings
    df_col=[ x.split()   for x in twitter_df['Tweets']]
    #removing the stop words
    no_sw=[[ c for c in new if not(c.lower() in stop_words_dict['stopwords'])] for new in df_col]
    #removing the urls and insert it to twitter dictionary
    twitter_df['Without Stop Words']=[[ x for x in dflist if not('http' in x)] for dflist in no_sw]
    return twitter_df
    pass