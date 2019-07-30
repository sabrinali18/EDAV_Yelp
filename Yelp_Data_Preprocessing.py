#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Read data from JSON file

import json  
import pandas as pd

yelp_bus = []
with open('yelp_academic_dataset_business.json') as f:
    for line in f:
        yelp_bus.append(json.loads(line))


# In[ ]:


yelp_bus = pd.DataFrame(yelp_bus)


# In[ ]:


yelp_bus.to_csv("yelp_business.csv")


# In[ ]:


yelp_bus.head()


# In[ ]:


yelp_bus.state.unique()


# In[ ]:


yelp_bus.describe(include = 'all')


# In[ ]:


yelp_review = []
with open('yelp_academic_dataset_review.json') as f:
    for line in f:
        yelp_review.append(json.loads(line))
        
yelp_review = pd.DataFrame(yelp_review)


# In[ ]:


yelp_user = []
with open('yelp_academic_dataset_user.json') as f:
    for line in f:
        yelp_user.append(json.loads(line))
        
yelp_user = pd.DataFrame(yelp_user)


# In[ ]:


yelp_tip = []
with open('yelp_academic_dataset_tip.json') as f:
    for line in f:
        yelp_tip.append(json.loads(line))
        
yelp_tip = pd.DataFrame(yelp_tip)


# In[ ]:


yelp_review.to_csv("yelp_review.csv")

yelp_user.to_csv("yelp_user.csv")

yelp_tip.to_csv("yelp_tip.csv")


# In[ ]:


yelp_review.head(15)


# In[ ]:


review_small = yelp_review.sample(frac = 0.2)


# In[ ]:


#review_group = yelp_review.groupby('business_id')['text'].apply(list)


# In[ ]:


review_groupby_stars = yelp_review.groupby('stars')['text'].apply(list)


# In[ ]:


review_groupby_stars_small = review_small.groupby('stars')['text'].apply(list)


# In[ ]:


review_groupby_stars_small.to_csv("Group By Stars Review Small.csv")


# In[ ]:


review_group.to_csv("Grouped Review.csv")


# In[ ]:


review_groupby_stars = review_groupby_stars[1:]
review_groupby_stars.to_csv("Group By Stars Review.csv")


# In[ ]:


review_smaller = yelp_review.sample(frac = 0.001)
review_groupby_stars_smaller = review_smaller.groupby('stars')['text'].apply(list)
#review_groupby_stars_smaller = review_groupby_stars_smaller[1:]


# In[ ]:


#review_groupby_stars
star1 = review_groupby_stars_smaller.iloc[0]
with open("star1_review_s.txt", "w") as output:
    for review in star1:
        output.write(review)
        
star2 = review_groupby_stars_smaller.iloc[1]
with open("star2_review_s.txt", "w") as output:
    for review in star2:
        output.write(review)    
star3 = review_groupby_stars_smaller.iloc[2]
with open("star3_review_s.txt", "w") as output:
    for review in star3:
        output.write(review)
        
star4 = review_groupby_stars_smaller.iloc[3]
with open("star4_review_s.txt", "w") as output:
    for review in star4:
        output.write(review)
        
star5 = review_groupby_stars_smaller.iloc[4]
with open("star5_review_s.txt", "w") as output:
    for review in star5:
        output.write(review)


# In[ ]:


yelp_user.head(15)


# In[ ]:


yelp_tip.head(15)

