from PIL import Image
import requests
from io import BytesIO
import pandas as pd

#Original code to merge GB + US datasets, don't need anymore.
# na_df = pd.read_csv (r'dataset/USvideos.csv')
# gb_df = pd.read_csv(r'dataset/GBvideos.csv')
# concat_df = pd.concat([na_df, gb_df], axis=0, sort=False, ignore_index=True, verify_integrity=True)
# #concat_df.drop(concat_df.columns[[0]], axis=1)


merged = pd.read_csv('US_GB_merged.csv')
for i, j in merged.iterrows():
    print(j['video_id'], '\n')
    response = requests.get('https://img.youtube.com/vi/'+j['video_id']+'/0.jpg')
    img = Image.open(BytesIO(response.content))
    #can use img.show() to reveal the image in each loop.
    img.show()






