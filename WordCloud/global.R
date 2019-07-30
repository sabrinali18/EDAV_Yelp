library(tm)
library(wordcloud)
library(memoise)

# The list of valid books
review <<- list("1 star" = "star1_review_s.txt",
               "2 star" = "star2_review_s.txt",
               "3 star" = "star3_review_s.txt",
               "4 star" = "star4_review_s.txt",
               "5 star" = "star5_review_s.txt")

# Using "memoise" to automatically cache the results
getTermMatrix <- memoise(function(review) {
  # Careful not to let just any name slip in here; a
  # malicious user could manipulate this value.
  if (!(review %in% review))
    stop("Unknown info")
  
  text <- readLines(review,
                    encoding="UTF-8")
  
  myCorpus = Corpus(VectorSource(text))
  myCorpus = tm_map(myCorpus, content_transformer(tolower))
  myCorpus = tm_map(myCorpus, removePunctuation)
  myCorpus = tm_map(myCorpus, removeNumbers)
  myCorpus <- tm_map(myCorpus, removeWords, c("get", "just", "like", "said", "will", "got", "went", "came" ,"can", "food", "service"))
  myCorpus <- tm_map(myCorpus, removeWords, stopwords("english"))
  myDTM = TermDocumentMatrix(myCorpus,
                             control = list(minWordLength = 1))
  
  m = as.matrix(myDTM)
  
  sort(rowSums(m), decreasing = TRUE)
})

