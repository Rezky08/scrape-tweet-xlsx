import twint
import pandas as pd
import os
import datetime

keywords = pd.read_excel("./KEYWORDS.xlsx")

for index,keyword in keywords.iterrows():
    c = twint.Config()
    output_dir = "Result/{}".format(datetime.date.today())
    output_file_path = "{}/{}".format(output_dir,keyword['keyword'])
    os.makedirs(output_dir,mode=777,exist_ok=True)
    print("Searching {} output {}".format(keyword['keyword'],output_file_path))
    c.Search = keyword['keyword']
    if pd.notna(keyword['limit']) :
        c.Limit = keyword['limit']
    else:
        c.Limit = 100

    if pd.notna(keyword['user']):
        c.Username = keyword['user']

    c.Custom['tweet'] = ['username','tweet']
    c.Pandas = True
    c.Hide_output = True
    twint.run.Search(c)
    twint.output.panda.Tweets_df.loc[:,['username','tweet']].to_excel("{}.xlsx".format(output_file_path),index=False)



