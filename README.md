# Russian Tweets Identification Model

#### Dataset
The data set included with this model is composed of a sample of Russian troll tweets from FiveThirtyEight's published data (https://github.com/fivethirtyeight/russian-troll-tweets), a sample of US politician's (senators, congressmen, and governors) tweets hydrated using Twarc with IDs from GWU's dataset (https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/2FIFLH). While politician's tweets were collected, only the news tweets were used in the model as it provided more interesting results.

News tweets were restricted to a selection of news outlets:
- Reuters
- AP
- Chicago Tribune
- ABC
- Politico
- WSJ
- NPR
- CNN
- USA Today
- Forbes
- NY Times
- Washington Post
- Fox News
- Huffington Post

#### Model
A naive Bayes models (from Scikit-Learn) was used to classify tweets as either being written by a troll or a news outlet.

#### Results
Using a 50/50 split of Russian and news tweets to train the model, an f1 score of ~0.84 was achieved. More interestingly, a scoring of news outlets was produced to rate outlets the average probability that their tweets would be classified as troll-authored. These results can help inform managers of these accounts on how their tweets may be perceived. Further, it may lead to insight into how certain tweets from media outlets may be written to grab the attention of readers, and suggest the quality of those outlets. For example, many of the troll-like news tweets appeared to use "clickbaiting" often exhibited by trolls to gain attention. On the other side of the spectrum, news-like troll tweets may suggest how trolls can attempt to appear as credible news sources while spreading misinformation.

Additionally, by extracting features and their significance to the model (i.e. the probability that, given a specific word from the text of the tweet, the tweet was authored by a troll or media outlet), we can see how certain words are used by either group. These can help news outlets understand how their media presence may make them appear more or less reliable.

#### Future Paths
Finally, by refining the model, it could help social media platforms assess the source of content posted by users to identify those who belong to troll groups. By using VPNs or other tactics to mask their source, these authors can be difficult to discover. However, by analyzing the content of their posts with NLP and machine learning, it may be possible to locate trolls using text alone. Additionally, by looking at which accounts trolls follow and performing network analysis, it may be possible to further improve the accuracy of the model.

Users of social media platforms and lawmakers are increasingly questioning platform’s responsibility in preventing the influence of troll groups and the spread of fake news. By implementing machine learning models that identify such groups, platforms can mitigate the liability and reputation risk posed by trolls.
