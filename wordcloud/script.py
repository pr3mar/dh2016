import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

cs = open('../tweets.txt', 'r', encoding="utf8").read()
cs += open('../dragonhack.txt', 'r', encoding="utf8").read()

cs = cs.replace("HackKean", " ")
cs = cs.replace("https", "MajorLeagueHacking")
cs = cs.replace("AnvilHackII", "UniversityOfLjubljana DragonHackLJ")
cs = cs.replace("AnvilHack", "DragonHack")
cs = cs.replace("CUCCHack", "DragonHack Ljubljana")

img = Image.open("dragonhacklogo.png")
img = img.resize((1134, 1080), Image.ANTIALIAS)
#hcmask = np.array(255 - img)
hcmask = np.array(img)

wc = WordCloud(background_color="black", max_words=10000, mask=hcmask, stopwords=STOPWORDS)
wc.generate(cs)
wc.to_file("wc.png")
plt.imshow(wc)
plt.axis("off")
plt.figure()
plt.imshow(hcmask, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
#plt.savefig('wc.png')


