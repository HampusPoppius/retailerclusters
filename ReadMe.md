Retailer Clustering 
===================

Basic purpose
-------------

This code uses the Latent Dirichlet Allocation (LDA) to cluster retailers based on their product ranges (list of products they 
offer). The output is a pre-specified number of clusters that are probability distributions over products. In addition, the 
algorithm generates a representation of each retailer as a probability distribution over the clusters. The LDA was initially 
developed to cluster text documents based on what "topics" they are about.

The full description is the same as on my [personal website](https://sites.google.com/view/hampuspoppius/extra/e-tailer-clustering "personal website")

Full description
----------------

When you do empirical research about online retailers, you might want to cluster or group the retailers. You want retailers in the same group to offer similar products but retailers in different groups should not. You might be interested in the groupings per se, but you could also just want to control for different industry-specific things.

There is a way to construct intuitive retailer clusters just based on what products they offer. Because many retailers offer many different types of products, you might not want binary classifications such as standard industry codes (e.g. SIC). Instead, you might find it likely that there are many different clusters that each describes a mix of products, but that retailers can belong to several of them and not only one. Moreover, the retailers might belong very strongly to one cluster, and just a little bit to some others. If you know some unsupervised machine learning and text analysis, you might start to think that this sounds like the Latent Dirichlet Allocation model, or “topic modeling”. That is exactly what it is.

The Latent Dirichlet Allocation is typically called “topic modeling” because it was developed by Blei, Ng, and Jordan (2003) to cluster text document into latent topics. It could for example be a set of news paper articles that a researcher wants to describe as mixes of different topics. However, the researchers have only the articles, but no idea of what potential topics they could be about. Reading them is not an option. To identify some topics and get information about what article belongs to which topics, the researcher need only feed the topic model with counts of words for each article. The researcher also needs to assume and specify how many topics (clusters) that exist. The topic model then identifies what words typically co-occur in articles (regardless of order and position in the text) and puts the words that do in clusters together. The allocation of words into clusters is not binary. Each topic is a probability distribution over words. For example, one topic could be 13% “interest”, 22% “money”, 9% “investment”, and so on, adding up to 100%. The researcher could use this information to understand that this topic is about finance. Then, based on these probability distributions, each article can be described as a probability distribution over topics. For example, an article in which “interest”,  “money”, and “investment” all occur could be 65% about the “finance” topic. The remaining 35% could be spread over several other topics depending on what other words occur in the article.

The analogy for retailers and their products is that each retailer is an article and the products are the words. The algorithm thus cluster products that typically co-occur in retailers’ product ranges together in topics that can be thought of as branches or trades. For example, if retailers that sell cycling shoes typically also sell cycling gloves and cycling pants, these products would create a cluster with other cycling gear. Retailers that mainly sell cycling gear would then load heavily on the cycling gear cluster. Below I show some clusters that result from running the LDA on the universe of online retailers in Sweden, scraped from a price comparison website on February 1, 2020. I only consider retailers that offer at least 20 different products (LDA works poorly for very short texts, e.g. tweets) and I disregard all products that are offered by less than five retailers (they are less informative and creates more noise). That results in 2247 retailers offering in total 173688 different products. I let the algorithm use this information to create 100 clusters.

To understand the nature of each cluster, let’s manually inspect for each cluster the five “most likely” products and the five “most likely” retailers. Here are some examples with labels that I deem appropriate based on the products:



Topic nr: 19 – “Golf gear”

Products: Garmin Approach S60, Big MAX Blade, Wilson Staff D7 Driver, Big MAX Autofold FF, Wilson Staff Infinite The Bean Putter

Retailers: Out-of-Bounds, Nordica Golf, Customclubs.se, Dimbo Golf, Golfbutik.se

 

Topic nr: 32 – “Board games”

Products: Exploding Kittens, Catan, Ticket to Ride: Europe, Mansions of Madness (2nd Edition), Kingdomino

Retailers: Alphaspel, Dragon's Lair , Allt på ett kort, Mantikora, Playoteket

 

Topic nr: 87 – ”Tires”

Products: Nokian Hakkapeliitta 9 195/65 R 15 95T Dubbdäck, Michelin Primacy 4 205/55 R 16 91V, Continental Viking Contact 7 225/55 R 17 101T, Michelin Primacy 4 225/50 R 17 98Y, Michelin Primacy 4 205/50 R 17 93W

Retailers: Tyred.se , Bythjul, Skruvat.se, Statusfälgar, Däck365

 

I have “organisationsnummer” for most of the retailers, so it is possible to match the clustering output to other datasets. Let me know if you want that and I’ll be happy to provide it for you.

 

 

Blei, David M, Ng, Andrew Y, & Jordan, Michael I. 2003. Latent dirichlet allocation. *Journal of machine Learning research*, 3(Jan), 993–1022.