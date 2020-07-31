# Deep Learning Project

For this project we explored the GAN Dissection framework presented by Bau et. al and their tool made available [here](https://github.com/CSAILVision/GANDissect). We used this on a few different GAN models and wrote up a report of our results.

Team members: James Lee and Lalithya Kuntamukkala

### Directories
---
* `report/` contains the final report for our class project
* `scripts/` contains various helper scripts and modifications to the python files of the original GANDissect repo we made to use the tool with different GANs
* `results/` contains links to Google Drive downloads for results from the dissections
* `models/` contains links to Google Drive downloads for all of the models we dissected
* `presentation/` contains a powerpoint presentation of a lecture we delivered on the paper.

### Resources
---
* [Network Dissection](http://netdissect.csail.mit.edu/). the paper that introduces the framework for dissecting CNNs. They experiment with it on numerous models and find some interesting results about the interpretability of individual units and the discriminative power of the network. Basically, the interpretability into seperable (disentangled representations as they call it) unit is some specific/unique alignment of the network, and adjusting the network in a way that doesn't affect discriminative power but messes up the interpretability of the representations (so that concept representations become some unique combination of many units, rather than a single unit) points to the idea that the interpretability is some special alignment that the network converges to based on how it's trained and set up. They also test this dissection method on a lot of networks using a lot of data, including tasks that aren't restricted to image classification, such as predicting ambient audio from frames, and analyze their results.

* [GAN Dissection](https://gandissect.csail.mit.edu/). takes the above framework and applies it to GANs. So now rather than just recognizing internal object representations through labels, in a generative model they can mess around with these internal representations to see how they're expressed in the generated output. 