# Lesson 6 - Regularization and CNNs

## TODO
- [ ] create your own dropout layer in python
- [ ] recrete excel examples in python
- [ ] heatmaps generally
- [ ] kernels generally


## NOTES

- next week is neurIPS
- Jeremy has a new startup: platform.ai
- we're going to be diving into convolutions today
- but before we do, we need to discuss regularization again
- tabular learner 
    - we want to understand everything in the init and forward methods
- the Rossman dataset
    - trying to predict how many products they will sell in the next few weeks
    - testset is from a time period that is more recent than training set
    - evaluation metric is root means squarted percent error
    - you were allowed to add even more data as long as you shared it
    - we are skipping over joining datasets in this course
    - fastai provided it for you
    - we are not doing recurrent neural net with this timeseries model. instead they take the time piece of the data, and they add a bunch of metadata
    - the cleaning notebook
        - we are given date, and add a bunch of columns to it 
        - this helps you take timeseries data and deal with as tabular data
    - transforms
        - bits of code that takes a random value
    - preprocessers
        - run once, not every time. before you do any training
        - they run once on the training set, and any metadata thats created is shared with validation and test set
        - Categorify
            - takes strings, and makes list of them, and turns stirngs into numbers
        - CompetitionDistance
            - things that are missing are interestes, and we should keep that in a column
    - categorical variables
        - not just strings
        - could also be day+of_month
        - these create embedding matrix (what is an embedding matrix again)
        - what is CARDINALITY
    - continuous variables
        - 
- any time we are trying to predict sales, or population. these things have long tail distributions. care more about percent differences rather than aboslute. so you will do log=true
- use regularization to prevent overfitting
- one way is to use weight decay (fastai does this automatically)
- dropout is a kind of regularization. at random we throw away some pcertanage of the activations (not the weights/parametrrs). we just throw away some activations. for each mini-batch, we throw away a different set of activations. how many ... probability of 0.5% of them. this prevents any one activation from memorizing a particular imag
    - special drouput on the embedding layer
- how do you choose the size of the embeddings

BATCH NORM ND
its kinda unclear what this is
sorta of regularization
the research doesnt really know right now
but it does help
you can increase learning rate because its less bumpy!



DATA AUGMENTATION
anotehr regularization technique
jeremy is very excited about this
theres basically no cost to this
gives you better generalization without longer to train
look at the docs for the different transforms
music blog post has a cool data augmentation strategy


CONVOLUTION
kind of matrix muliply that has interesting propoerties
look at setosa's website

a kernal (a covoluiontal kernal). we do element wise multiuplication with reach of the nine items in our kernal
. then we add them up and show it on the right

we do lose some bits at the edge


output of a convolution is a channel

a convolution is just a matrix multiplication where some of the entries are set to zero... and things with same color are the same weight

we dont use matrxi muliutpication cause its slow tho so we do convultions directly

we have to think about padding. zero padding or reflection padding.


color images.. we have a rank 3 tensor. we want more activations on the green than the blue if we have a green frog detector. therefore, we need to create a 3x3x3 kernel. we actually do elememtwize mulitlication of 27 things. we pass a cube ove rthe image. just creates one number still


we then need another kernal to create another 5 x5 ..

stack those tegetoher,... finally we get a rank three tesnor output


sometimes we skip stuff.. this is called a Stride2 convultional



AVERAGE POOLING



lets instead average across the 512. that gives a single 11x11 matrix, and each grid point is the average of how activated was that area.


PYTORCH HOOKS





