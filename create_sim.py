tags_df = pd.read_csv('Homework 2 data/sample-genome-scores.csv')
movie_ids = np.unique(tags_df['movieId'])
print(len(movie_ids))
tag_combinations = combinations(movie_ids, 2)    
sim_df = pd.DataFrame(columns = ['Item1','Item2','Sim'])
for tag1, tag2 in tag_combinations:
    if tag1 != tag2:
        item_tags1 = tags_df[tags_df['movieId'] == int(tag1)]['relevance'].values
        item_tags2 = tags_df[tags_df['movieId'] == int(tag2)]['relevance'].values
        if item_tags1.size > 0 and item_tags2.size > 0:
        #item_tags1.reshape(1,-1)
        #item_tags2.reshape(1,-1)
            sim = cosine_similarity([item_tags1], [item_tags2])
            sim_df.loc[len(sim_df.index)]=[tag1,tag2,float(sim)]
            #print(sim)
pickle.dump( results, open( f"results{factors}.p", "wb" ) )
