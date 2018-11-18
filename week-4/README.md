# week 4 notes
- NLP, Tabular, and Collaborative Filtering

### Notes

- change to the data block api from last week. the order is different
- NLP, Tabular, and Collaborative Filtering
- second half is more explanations for what we did in the first half
- camvid wasn't a fair comparison, because paper used a small subset, and we used all the classes. Accuracy went up even more when we used same subset.

#### NLP

- Natural language processing: taking text and doing something with it
- text classification is a practically useful application
- classifiying a document can be used for spam prevention, identifying fake news, to reading reports, to finding product mentions in twttier, so its very interesting,
- Legal Text Classifier with Universal Language Model Fine-tuning example (student in the course). LIM How Khang
- 25k movie reviews, and we have 1 bit of info for each
- remember neural networks are just matrix multiplies and nonlinearities.
- the weights start our random, and try to train them to recongize posivie vs negative.
- it's very tricky to really understand all the nuances of languages. for a long time, neural nets didnt doa good job of this. not enough information. so the trick is to use TRANSFER LEARNING. this is always the trick
- what if i try transer learning on nlp? i tried this last year, and it worked extraordinarily well, and now this is the hit thing. 
- the key is to start with the same kind of thing in computer vision. pretrained model trained to do something different
- imagenet was built for recognizing one of a 1000 categories
- our pretrained model can predict the next work of a stencne.
- needs world knowledge and english knowledge
- previous approches used n-grams for pairs and triplets of words. these are terrible for predicting next word.
-but neural nets are good at this. you actually have a lot information. every single word yo ucan try to predict the next word.
- learn how to speak english from wikipedia.
- wikitext103 dataset. simply a subset of the largest articles from wikipedia. with preprocessing.
- built a language model on top of it. a neural net to predict hte next word in each article. 
- this is useful because our model can complete our sentences, it knows about the world, and it knwos about english (E.g. what things can be hot)
- there is a theory of philosophy about this
- we can use transfer model to make a new language model that can predict the next word of movie reviews, pretrained with wikitext model. then that will know a lot about the world of movies.
- we dont need any labels at all for this ... built into dataset itself.
- then we finetune that to do what we want, to classify as positive or negative
- language models themselves can be quite powerful.

- numericalization

- jeremy likes using the datablock api

- it's always good to use transfer learning when you can

- why randomly split at 10% 
- even thought validation set is set aside, we only have to keep the labels aside. but can certainly use the indepdent varioables in the validation set to train the language model. concat training and validation, and then split out a smaller validation set. if doing nlp on kaggle, or just have a smaller subset of labeled data, use all the text you have to train your model.
- how to label it? language model has its own labels. 

langauge model learn
is an RNN
not a CNN

same basic structure
input into weight matrix, then multplierm, then replace with zeros, many times. same basic structure.,

Momentums (MOMS)
we will learn about this next week




encoder - understands the snetnece




Classifier
needs to use the very same vocab! from the lanugage model!

you only need to do the language model once for your domain, and then making classifiers on top of it is every easy


learning rate. 2.6 ^ 4
why 2.6?
basically, this number is whats difference how quickly lowest layer and highest layer
we found out that for nlp rnn, the answer is 2.6
i ran lots and lots of different models with lots of hyperparams, dropout, and created a random forest to predict how accurate nlp classifier would be


AUTOML
jeremy not a big fan of it on the whole











TABULAR DATA
spreadsheet
relational database
contains lots of different things
using neural nets for this .. people thought it was strange
Pinterest uses neural networks for something(?) ask them about this

fastai.tabular might be the first time this is really easy
we assume data is in a dataframe


categorial variables (indpdendnet variables), we will use embeddings for these
continuous variables (dependent variables), these can just be sent in like pixels

idenpdent abaribles



WATCH VISIDEO on PROCS. I wasn't paying attention.

FillMissing = replace with median and add new column

Normalization = whatever you do to training set, you have to do to validation or test set


layers= [200, 100]
this is like choosing resnet 
this is our architecture





COLLABORATIVE FILTERING
* where you have info about who bought, liked what. something like a user/reviewer and info about what they've bought, written about, or reviewed
- basic version is just two columns (user_id and movie_id)
- which user bought which item
- sparse matrix is interesting way to store, or just two columns

data set is called MovieLens ffrom GroupLens

cold start problem. when you want to be good about recommending movies is when you have a new user (or a new movie), and you dont have any data in your system. thees nothing currently in fastai for cold start problem. you can have a metadata driven model as a second model for new users or new movies




EMBEDDING IS A MATRIX OF WEIGHTS


how can we make it easy for the network to learn the right thing



vim tags to jump to the defintion
- watvh this video for jumping through the code in vim


linear algra
you shuld know how matricx mulitplication works, and how the the dimensions impact the resulting vector

actiation functions dont change the size, just the contents

can be any number of columnbs, but the rows should map nicely


LAYERS

activations are the numbers that are calcuated. reuslt of a matrix multiply or activation function

paramaters are stored, and generate the activations. nubmers inside the matrices that we multiply by


there are also special latyers

* input layer.. where you start
* output layers

outputs not special they are jsut activatoinsof a layer
. v


sigmoid is often the last layer (something between 2 values)



LOSS FUNCTION compares ground truth to the output layer
