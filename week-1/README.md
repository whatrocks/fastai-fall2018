# Lecture One

## Platforms
- Salamander apparently lets you use your AWS credits
- GCP prepared an image special for Fast.ai

## Notes
- Right now, the DL frameworks require that you use an NVIDIA GPU.
- You (anyone!) can do DL
- Fastai
  - Software
  - Research
  - Education
  - Community
- 8-10 hours of homework per week
- Learn how it works before why it works
- Still lots of artisanship in DL, you only get that through experience. Best is to create lots of models, and study them carefully.
- You need images and labels. That's it.
- Their library will chop into a training set and a validation set.
- Why do the images need to be the same size? Because a GPU has to apply the exact same instruction set to the same thing at the same time to be fast, so the images need to be the same shape and size. This is a current limitation of DL. In part 1 of this course, we will always make things squares. In part 2, we will make some rectangles, but that introduces complexity.
- The DataBunch object
- Normalization
  - If data not normalized, it's difficult to train
  - It really helps if each RGB channel of an image has a mean of 0 and a standard deviation of 1
- Resnet works extremely well nearly all the time
- Learner will download pretrained weights
- Most of this course is transfer learning. Turns out you can train models if 1/100 time and similar drop with data with transfer learning. 
- Overfitting
- fit vs fit_one_cycle -- What does this mean? 
  - use one_cycle - it's better. Why?
- compare your solution to the paper or kaggle results
- Edge computing needs different architectures. Best to use REST APIs
- Learn.save saves the checkpoints. Can we adjust the path?
- Loss function
  - tells you how good your prediction ways
  - what were things we were most confident about that we got wrong
- Confusion Matrix
- most_confused()
- unfreeze. Please train the whole model.
- Matt Zeiler. Convolutional Networks paper.
  - you want intuition that layers of neural net represent differnet layers of semantic complexity
- learning rate
  - how quickly am i updating the paramers in my model
  - how does this impact loss
- if you run out of memory, just make the batch size smaller
- its fine to use smaller batch size, it just might take longer


## Cool projects from alumni

- Hamel Husain
  - Github issues
- Sarah Hooker
  - Works at google brain. Founded delta analytics. Deforestation in Africa
- Christine Payne
  - Works at OpenAi. Neural net music generator. Classical pianist. Pick one project and make it fantastic.
- Melissa Fabros
  - English lit PHD. Facial recognition for African women for Kiva. Won $1M grant from Crowdflower
- Carfik / Envision
  - app to help blind navigate
- Helena Sarin
  - artist with DL
- Splunk and TensorFlow
  - detecing fraud with pictures of mouse clicks and movement
  - idea: make spectrogram of sound and fit to image. make non images into images
- Hot dog or not
  - built by tim a fast.ai student 
