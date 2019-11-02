import string
import pandas as pd
import re

df = pd.read_csv("outputwithheader.csv", header=[0])
oldArr  = ['Nearly   Fired TWICE to Winning The SEC! | Mizzou 5-Year Rebuild | NCAA Football 14 (69/126)',
       'How to make Modern R&B Beats for Summer Walker & Bryson Tiller [Tutorial]',
       'Kanye West Airpool Karaoke',
       'Dreamville - Down Bad feat. J.I.D, Bas, J. Cole, EarthGang, & Young Nudy  (Official Music Video)',
       'Dolemite 1975 full movie']


def myfunc(a):
    return a != ""


for i in range(df.shape[0]):
    w = df.iloc[i].title
    df.at[i, 'title'] = w
    p = {}
    for j in re.findall("\W", w):
        if j == " ":
            continue
        elif j in p:
            p[j] += 1
        else:
            p[j] = 1
    for x in string.punctuation:
        w = w.replace(x, " ")
    a = w.split(' ')
    a = filter(myfunc, a)
    w = ' '.join(a)
    for k in p.keys():
        w += " " + (k * p[k])

    print(w)
df.to_csv("formttedInput.csv")
df.to_json("formattedInput.json", orient='records')

