# lesson 7

## todo

- [ ] build your own resnet
- [ ] take text off of race photos / probably not legit
- [ ] stick figures to comic book characters
- [ ] make your own crappification images
- [ ] make your own autotune ?
 

## notes

### RESNET
Resnets, unets, gans, and rnns

give you enough things to think about until part 2. this will be busy.


start with lesson7resnetmnist



stride
skips over pixels.
each convolution will half the grid size (WHAT?)
read the comments to figure out how matrix math happens to the "grid size"
flatten at the end will remove any unit axes... making it a vector at the end





Deep Residual Learning for Image Recognition
paper
deeper network has higher error!
RESBLOCKS
resnet
replace convultions with resblocks
this is a good trick


Visualizing the Loss Landscape of Neural Nets


this resnet is so popular, so libraries tend to optimize it



DENSENET
concatenate insteadf of plus
same as resnet...concat instead of plus


### UNETS

a guide to convolutional arthimetric for deep learning

how do we double the gride size? we do a stride 1/2 conv
traspose convolutional
 
nearest neighbor interpoliation is an "upsample" and then a stride 1 conv for some computation

bilinear interpolication could be a weighted average appraoch

unets also use identity connections, cand came before resnets actually
they are concatenated


the encoder
this is the left part!
in our case, a resnet34
in most cases, its an older architecture




IMAGE RESTORATION

creating a better image
take low res make high res
take bw and make it color
take photo and make it look like monet painting

use a pretained models so that it knows about stuff already


GAN
geneative adversarial netowkr
loss function actually calls another model
discriminator/critic

binary classification model
generated and real image.. learn to classify which is which?


gans hate momentum. right now at least.

