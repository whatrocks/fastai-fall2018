# todo list
- [ ] Kaggle setup for FloydHub
- [ ] Kaggle integration
- [ ] Reach out to PG&E about blog post ideas
- [ ] create api from week one
- [ ] meme clean up tool as blog post from 'Show your work'
- [ ] children's artwork GAN
- [ ] YC company logo - will they fail or not based on their logo
- [ ] set up Starlette on serving jobs
- [ ] learn scientific notation
- [ ] spit things to tensorboard with fastai
- [ ] np.argmax (look this up)
- Adam Geitgey (blogger) https://medium.com/@ageitgey
- [ ] animated through the images like a slot machine, or pull from google images (frog project)
- [ ] make gif from a jupyter notebook (visaliing the animation)
- [ ] can i eat this mushroom ?

## pre-class notes

* "further discussion" is for advanced students who already know DL, rest of discssuion is for beginners
* Crestle GPU is now free for next few months

## notes

* Computer vision
* meme cleanup tool
* turning sounds into pictures and using lesson one approach is genius
* we will go back to computer vision and nlp several times
* process
    - code first: focus on learning from experiment
    - the whle game: its like learning soccer as a code
    - concepts not details: we will dig into them all later
    - do lesson 2: even if you dont understand it all
* if you're stuck, keep going!
* download notebook
* how to create your own classifier with your own images
* create a teddy bear detector, separating teddy bears, from grizzly bears, to black bears
* don't forget to remove things that aren't images
* get_transforms() - relisten to this
* it is important to always have the same validation set. he liks the random seed.
* you could do better if your dataset was less noisy, so we want to clean it up
* computer expert + human learner is a good skill. this is a great skill. combine your domain expert with computer science.
* serving model
    - run on a CPU
    - most people running inference apps are using CPUs
    - path in databunch is where our model lives
    - Starlette is like Flask (you can use async-await)
    - PythonAnywhere
    - Simon uses a Docker thing
    - Doesn't need to cost you any money
    - Jeremy wants to see what you can make of that.
* you can build apps in jupyter notebook
* he thinks creating apps within notebooks is really need and underused
* Problems
    - learning rate too high or low
    - epochs number is too high or low
* learning rate
    - too high. Validation loss goes really high.
    - learning rate too small, error rate gets better but too slowly
        - traning loss higher than validation loss. this is bad. learning rate is too low, number of epoches is too low
* too few epochs
    -  looks similar to too low learning rate
    - 
* too many epochs
    - it will learn your teddies but not teddies in general
* overfitting: error rate will improve for a while, and then gets a bit worse. that's the only way you know if you're overfitting.

training loss > validation loss is overfitting. THIS IS NOT TRUE

sign of overfit. ERROR IS GETTING WORSE.

* predictors are functions of pixel value
*np.argmax( returns the index of the highest value)
* metrics in the functions use validation set 
* was using 3 with learning rate before? 3e-3 is a really good default learning rate. then try ten times less than that.
* go to khan academy and listen to the refresher
* why use linear algebra. check out computational linear algebra for coders from rachel. is a great free course. will make your life much easier.
* jeremy hates writing loops and code
* dot product and matrix product
* matrix multiplication.xyz
* how do you know if you dont have enough data. your accuracy isnt great. theres no shortcut. most of the time you need less data than you think. organization spend too much gathering data.
* what do you do with unbalanced classes? do nothing. try it. it works.
* resnet24 is an "architecture". it is just a function, not a model. 
* why not unfreeze directly? he will get to that later.
* pytorch really doesnt like loops. really prefers linear algebra type ways
* SGD:
    - stocastic gradient descent
    - stocastic grad student descent. lolz
* Tensor sounds scary. if you are physisit it is scary. in DL it means array of a regular shape. not a jagged array. any array with rectangular or cube shape where every row and column are the same length
* rank - how many axes are there (dimension)

images are rank 3 tensors

* : in a vector means every single row of column zero
* pytorch function ends in underscore means replace it

* element-wise arithmetic

bkacward calculates the derivative

run this nb with lots of diferent ;learning rates to see what it feels like


SGD uses minibtaches. linear regreation doesn not.

Watch video and check the vocab and make an anki deck

Make anki-deck as a github repo

* rachels talk no such thing that theres not a match person


OVERFITTING / UNDERFITTING

how to make sure we dont overfit
- regularization. techniques to make sure that when we train our model it will work well on data that it hasnt seen yet. the most important thing.
- most imrpotant is how well does it work on data that it hasn't seen yet.
- idea of a vlidation set is really important for evaluation of AI solutions. teach your managers about this. make sure that the models will generalize. lots of details to get right when designing your validation set. read rachels piece of the fast.ai blog.
