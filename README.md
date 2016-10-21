# SeqGAN

## Requirements: 
* Tensorflow r0.10  
* Cuda 7.5 (for GPU)  
* nltk python package

## Introduction
Apply Generative Adversarial Nets to generating sequences of discrete tokens.

![](https://github.com/LantaoYu/SeqGAN/blob/master/figures/seqgan.png)

The illustration of SeqGAN. Left: D is trained over the real data and the generated data by G. Right: G is trained by policy gradient where the final reward signal is provided by D and is passed back to the intermediate action value via Monte Carlo search.  

For full information, see the paper:  
SeqGAN: Sequence Generative Adversarial Nets with Policy Gradient (http://arxiv.org/abs/1609.05473)  

We provide example codes to repeat the synthetic data experiments with oracle evaluation mechanisms.
Move to MLE_SeqGAN folder and run
```
python pretrain_experiment.py
```
will start maximum likelihood training with default parameters.
In the same folder, run
```
python sequence_gan.py
```
will start SeqGAN training.
After installing nltk python package, move to pg_bleu folder and run
```
python pg_bleu.py
```
will start policy gradient algorithm with BLEU score (PG-BLEU), where the final reward for MC search comes  
from a predefined score function instead of a CNN classifier.
Finally, move to schedule_sampling folder and run
```
python schedule_sampling.py
```
will launch SS algorithm with default parameters.

Note: this code is based on the [previous work by ofirnachum](https://github.com/ofirnachum/sequence_gan). Many thanks to [ofirnachum](https://github.com/ofirnachum).

After running the experiments, the learning curve should be like this:  
![](https://github.com/LantaoYu/SeqGAN/blob/master/figures/lc.png)

##Text Generation Example
To test how the model generates text, the original oracle has been replaced by TextGenerator, which reads randomly selected sequences of text from arbitrary .txt file and saves them in file MLE_SeqGAN/real_data that is used for further training of discriminator and generator
For testing, Dicken's novel A Christmas Carol has been used. Below are examples of generated sequences:

illustrate thescriptures. There were cains and abels, pharaoh's daughters, queens ofsheba, angelic messengers descending through
, mince-pies, plum-puddings, barrels of oysters, red-hot chestnuts, cherry-cheeked apples, juicy oranges, luscious pears
poultry, brawn, meat, pigs, sausages, oysters, pies, puddings, fruit, nor the
designed to illustrate thescriptures. There were cains and abels, pharaoh's daughters, queens ofsheba, angelic messengers
designed to its ankle, whocried piteously at being unable to assist a nobody in thecopper. Why did
yet, dotting the woman, bless christmas! Speakcomfort to me, woe upon the gentleman. His
, mince-pies, plum-puddings, barrels of oysters, red-hot chestnuts, cherry-cheeked apples, juicy oranges, luscious pears
poultry, brawn, great joints of read into their death-cold table and his daughter leaning fondly on him,
, andpleasant shufflings ankle deep through withered leaves; there werenorfolk biffins, squab and swarthy, setting off the
poultry, brawn, great joints of meat, sucking-pigs, long wreaths of sausages, mince-pies, plum-puddings,

To test the current code, just run pretrain_experiment.py and sequence_gan.py the same way as described above. After training is completed, run text_generator.py in MLE_SeqGAN
