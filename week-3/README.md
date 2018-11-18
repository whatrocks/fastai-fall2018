# week-3 notes

## Notes

* Multi-label
* Segmentation


NOTES
* videos.fast.ai
* andrew ng's machine learning course is very good for foundational, traditional academic approach to ML
* fast.ai also has an intro ml course that is top down

one label is always the weather
rest of labels are interesting features that it recognizes

data block makes each decision seperate for creating your data

this is a nice api

Dataset class
part of pytorch
it does nothing at all when you look at the source code
"dunda" for special python methods

dataset is not enough to train a model
we have to have a few items at a time so that our gpu can work in paralle. we call that a minibatch. the gpu goes through that time

another pytorch class called DataLoader
this takes a dataset and its constructor, and it grabs item at random and creates a batch of whatever sise you ask for and pop it on the gpu and send it off to the model for you


we need a separate validation set

there is a FastAi class called a DataBunch'


databunchs know how to draw themselves



transforms by default
shift tab to get the info
transforms by default will randomly flip horizontally
this makes sense for most pictures
on the other hand, satellite imagery could be flipped upside down
flip vert should be switched to True
max warp ... perspective warping



threshold

accuracy?? gives you source code


remember argmax?
the function that finds the biggest and returns the index is called argmax
to get the accuracy for pet detector was argmax to find out which lcass idea was the one we were looking at. compared tha tto the actual, and then took the average

we cant do that for satellite recognition. we are looking for lots of labesl

we we will use accuracy_thresh() in this case


partials are like function currying



recording your incorrect answer
you can record this
collect this feedback
what does fine tuning look like?
it looks like this...
createa new databunch with misclasffieid images
so maybe fit a higher learning rate. or run them through more epoches



find the STEEPEST slope with learning rate finder
then look for right before it ggoes up
and then go back about 10x, and go with the frozen learning rate divided by 5 or 10


LISTEN AGAIN to this resizing thing.
I didn't get that.



CAMVID

you need labeled segment masks
you should definitely cite it


you have to use open_mask cause using integers not floats with this image


training loss > valid loss means UNDERFIT
if youre undefitting, then train long
train last bit a lower learning rate
but if still underfitting, then decreate regularization
in the second half of this course, we talk about regularization
and specifically how to avoid overfitting and underfitting



UNET
neural net
originally biomedical image segmentation
but has more applications



fit one cycle
lr start low, get high, and get low again



Learning Rate Annealing .. going down

leslie smith recently said you should raise it too

HELP: what is the learnign rate again, what EXACTLY does the learning rate control. NEED TO LOOK THIS UP AGAIN.




MIXED PRECISION TRAINING
instead of single precision floating point
you can do half precision, 16bits instead of 32bits
the very idea of this is only very rcently
fp16() you need recent cuda drivers 
this makes things twice as fast
uses less GPU ram




CROSS ENTRYP LOSS
did you predict create class for classfiication


REGRESISION
mean squared error


TOKENIZATION
makes sure each token represents a single linguistic concept
it finds rare words like names and replaces with an unknown special token

next NUMERICALIZATION
make list of all tokens as the vocab

then we replace each review with list of numbers from the vocab


UNVIERSAL APPROXIMATION THEREOM
stacks of linear functions with nonlineary it can approxmiate any function!


we use gradient descent to find the weights


HOMEWORK
segmentation
multilabel classification problem



