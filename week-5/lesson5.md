TODO
- [ ] best performing tweets collaborative filtering example


REgularization

read this: https://www.nytimes.com/2018/11/18/technology/artificial-intelligence-language.html

only two types of layers:

layers with parameters aka weights (things your model learns, you use gradient desent)


layers with activations:
* these are numbers
* these are calculated 
* inputs are a special activation isnce they are not really "calculated"
* come from matrix multiuplications or activation function

Activation Functions
* relu is one
* doesnt really matter which you pick
* just use relu

The Universal Approx Therem
* big enough and enoguh weight matrxies you can solve any arbitraryl complex math function to any level of accuracy, assuming you can train the parameters (assuming you have the time compute and data)

That is it! There's no trick after this.

We calculate the gradients, and then subtract the leargingrate times the gradient. This is back progpgation

BACK PROPOGATION
this sounds really impressive, you can replace it in your weight

Weights -= wreights (GO LISTEN TO THIS )
parameter = parameter - learning_rate * parameter.grad


When we do create CNN inf ast.ai... we kill last weight matrix, and add two new ones with a relu in between.

There are some defaults as to what sizes they are. But the second one, the size is as big as you need it to be. from your databunch, we know how many activations you need (classification .. nubmer of classes, regression its the numbers you need to predict)
it is of size data.c


The previous layers are good at something, so we dont need to train them right away.

The layers become more and more specific as you go further.

We definitely need to trian the new weights first, because they are random.
So we "freeze" the previous layers.

Then, we unfreeze, and gotta train the whole thing. But still have a pretty good sense, that our new layers still need more training.

So we split our model into a few sections, lets give differnt parts of the model differnt learning rates.
if you used a higher learning rate, it could make it work

this is called discriminative learning rates. there's not much online about it yet.



fit(number_of_epches, learning_Rate)

lr can be 
- single number (every layer gets same learning rate)
- slice(single number) -- final layers get what you gave it, previous layers get that divided by three
- slice(2 numbers) -- first layers get first nubmers and the rest are split equally between that second one



AFFINE FUNCTION
replace that in your head with maxtrix multiplication



EMBEDDING MATRICES
one-hot encodings
this is not part of a neral net. this is just preprocessing. its just making new inputs for the model


take input matrix, and do matrix multiply by the weight matrix. fifteen rows by fifteen columsn.

this one-hot-encoding version
this is very interesting. finds a particular row in the input matrix.

then we multiply those 2 sets together.

we can get the loss squared, and avergae loss.

that number is the same as thie other number. they are doing the same thing. weird. should try this out.

multiplying by zero is waste of time.

array lookup is same as one hot encodied mtraxie
aways do the arraw lookup version


we have a way fo doing that. this is an embedding
you might have heard this word all over the place

embedding means, look something up in a array. but note that this is mathematically same as matrix product as one hot encoded matrix

there fore embedding fits into neural netowkr. this is another layer, where we get to look tthings up in an array! this is a fast and emmeory efficiency way of multiuplying by a one hot encoded matrix

LATENT FEATURES
hidden things that were there all along'



n-hot encoding
movie can be in multiple genres


BIAS
Didnt get this. explain this.
"this user rates movies highler, this one rates them lower"
adding bias helps


add sigmoid to excel and you;ll get a better answer.

problem is that with sigmoid, you can 't actually predict five

you should let it go a little bit more than the max.


FACTORS means "width of the embedding matrix"

collaborative filutering is good for predicting likes on movies, for example



if we look at movie bias, we can fix problem of user bias (e.g. anime lover), once we account for specifics of this sort of movie, you get something specific to that movie itself.

movie bias numbers. what are the best movies

USERS AND ITEMS. they are convenient names. they are just words.



what is PCA?
someting to id the latent factors? This is cool



CollabLeaner


everything done in minibatch




"embeddings are amazing" ..we can still keep exploring!


"WD" is weight decay

weight decay is a type of REgularization

what is regularization?

complexity is not about number of parameters

More paramters, means more non-linearities, more curving bits. And that's what real-life is full of! but we dont want them to be more curvy than necessary

so lets use lots of parameters, and penalize complexity! One way to do this is to sum up the value of your paramters! what if sum up the square

we're going to take our loss, and take sum of squared paramters, and multiply it by wd. it should generally be 0.1


every learner can receive this



let's go back to Linear REgression in LEsson 2

i should go back and watch this port again


derivate of loss function at time t - minus one
computer calculates the derivative for us for free.



Loss is some function of our indepdenct varibles and our weights



minibatches



subclassing is very normal in Pytroch

override the constructor.
and implement forward


wd is only interestinf or training a neural net.. because we take the gradient of it
the only thing interesting about it is that we take its graident


the gradient of the loss is equal to gradient of each part and then added together

L2 regularization form vs weight decay...they are kind of mathematically identical. in some cases, they are not.



what is ADAM

finite differencing.. this is slow, but goot do check tings out



Momentum! we can speed up SGD
a tenth from the derivate, and 90% is the same direction as last time!
this is called momentum


take lesson 2 SGD and add momentum


RMS PROP
Jeff Hinton created it 
take bigger jumps over time 



what does fit one cycle really do

chart on left
plotting learning rate per batch
we use ADAM by default

on the right
the momentum plot
when lr is small, momentum is high
this is because we shoould go faster if we are going small lr
at the end if we want to go faster if we are moving slowly
one cycle is amazing but astonishing



CrossEntropyLoss
just another loss function
we already know MSE
same as an if-funciton for one-hot encoded
this is just like the embedding discussion


softmax
all the activations add up to one, greater than zero, and less than one


pytorch knows enough to do softmax with crossentropyloss

sometimes your predictions from omdels will come out looking like negative numbers. the reason is that pytorch that doesnt have a softmax in it, so you might have to do the softmax for it.





