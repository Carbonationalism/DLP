# Deep Learning Project (name/everything else TBD)

### Resources
---
* [Network Dissection](http://netdissect.csail.mit.edu/). the paper that introduces the framework for dissecting CNNs. They experiment with it on numerous models and find some interesting results about the interpretability of individual units and the discriminative power of the network. Basically, the interpretability into seperable (disentangled representations as they call it) unit is some specific/unique alignment of the network, and adjusting the network in a way that doesn't affect discriminative power but messes up the interpretability of the representations (so that concept representations become some unique combination of many units, rather than a single unit) points to the idea that the interpretability is some special alignment that the network converges to based on how it's trained and set up. They also test this dissection method on a lot of networks using a lot of data, including tasks that aren't restricted to image classification, such as predicting ambient audio from frames, and analyze their results.

* [GAN Dissection](https://gandissect.csail.mit.edu/). takes the above framework and applies it to GANs. So now rather than just recognizing internal object representations through labels, in a generative model they can mess around with these internal representations to see how they're expressed in the generated output. 

* [Synthesizing the preferred inputs for neurons in neural networks via deep generator networks](https://anhnguyen.me/project/synthesizing/). this paper (from Dr. Nguyen et al) uses GANs to construct prototypical images that maximize the activation of particular neurons (or possibly units of neurons, I'm not sure). So in a sense that Network Dissection measures the correlation between units and labels, this Activation Maximization (AM) method finds the input image that would maximize that correlation. There's definitely a bridge between AM and GAN Dissection, and finding it could be a good pursuit of this project.

* [Places: An Image Database for Deep Scene Understanding](https://arxiv.org/pdf/1610.02055.pdf). In this paper they create a model using the database to recognize the scene/setting of a particular image. In section 3.4 they use the visualization method (AM) presented above to visualize what neurons of each layer are recognizing (images which maximize their activation). Figure 12 shows this visualization, where the top one is an object recognizing network trained on ImageNet and the bottom is a scene recognizing network trained on Places. Figure 13 has the synthesized prototypical images for the final output layer, which is pretty interesting as the pictures do look similar to their classifications, but they also look distorted from actual reality.

* [Plug & Play Generative Networks: Conditional Iterative Generation of Images in Latent Space](https://anhnguyen.me/project/ppgn/). An extension on the AM methodology which introduces an additional prior on the latent code (the seed from which the image is generated). Conditional refers to the fact that the generative model receives a latent code conditional on something, for example, a specific class from ImageNet, so the generator is told to generate something from this category, they also used captioning as a condition. "PPGNs are composed of (1) a generator network G that is capable of drawing a wide range of image types and (2) a replaceable 'condition' network C that tells the generator what to draw." They also improve on feature visualization.

* [Multifaceted Feature Visualization: Uncovering the Different Types of Features Learned By Each Neuron in Deep Neural Networks](https://anhnguyen.me/project/mfv/)

* [Understanding Neural Networks Through Deep Visualization](https://anhnguyen.me/project/understanding-neural-networks-through-deep-visualization/)