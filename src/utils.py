import pandas as pd
import numpy as np
import sweetviz as sv
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import tqdm
from tqdm import tqdm

def wordcloud(df, col):
    text = " ".join(x for x in df[col])
    word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
    plt.imshow(word_cloud, interpolation='bilinear', cmap = 'gray')
    plt.axis("off")
    plt.show()
    
def data_type(df0, no_considerar = []):
    df = df0.copy()
    for col in tqdm([x for x in df.columns if x not in no_considerar]):
        if len(set(df[col]))<=20:
            df[col] = df[col].astype(str)
        else:
            df[col] = df[col].astype(float)
    return df


    
