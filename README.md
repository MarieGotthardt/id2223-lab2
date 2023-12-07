# Swedish Speech Recognition Using a Fine-Tuned Whisper Small Model
Second Lab Assignment within the course ID2223 *Scalable Machine Learning and Deep Learning*.

## Description of our System
In this assignment, we fine-tuned a pre-trained transformer model (Whisper small) for Swedish speech recognition, following this blogpost: [Fine-Tune Whisper For Multilingual ASR with 🤗 Transformers](https://huggingface.co/blog/fine-tune-whisper) by Sanchit Gandhi. Furthermore, we created a serverless UI that utilizes our model. Our system consists of the following pipelines:

- Feature Pipeline (only requires CPU)
- Training Pipeline (requires GPU)
- Inference Pipeline

## Experiments for Performance Optimization
In order to improve the performance of our model, we performed experiments with model-centric optimization techniques and with data-centric optimization techniques. 

As part of the model-centric optimization, we experimented with the following techniques:
- adding dropout (dropout = 0.1)
- using different learning rates (learning rate = 1e-4, 1e-5)
- using different learning rate schedulers (linear learning rate scheduler, cosine with hard restarts scheduler)
- using different numbers of warmup steps (10, 200)

// TODO: maybe create table with the different settings and results for these settings

For the data-centric approach, we performed an experiment with a combination of the following data augmentations:
- Gaussian noise
- Time stretch
- Pitch shift

based on the article [Fine-Tuning Whisper ASR Models](https://wandb.ai/parambharat/whisper_finetuning/reports/Fine-Tuning-Whisper-ASR-Models---VmlldzozMTEzNDE5) by Bharat Ramanathan.

## Utilization of our Model: Recognition of Swedish Christmas Songs
To demonstrate how users could utilize our fine-tuned model to automatically create transcriptions for Swedish, we created an app that can automatically identify Swedish Christmas songs based on the created transcriptions.

## Discussion of our Approach
One technical challenge we had to face during training was our limited GPU access, as we needed a GPU to train our model. To counter this problem, we regularly checkpointed our model weights so we could resume model training from these checkpoints in case we lost access to our GPU. Nevertheless, this circumstance limited the extent to which we could perform experiments for model optimization.

One limitation to consider regarding the app we created to automatically identify Swedish Christmas songs is that we only used a selection of Swedish Christmas songs. Thus, if a user sings a song not included in our selection, our app is not able to identify it correctly.

Selected songs:
- Bella notte
- Bjällerklang
- Den vintertid nu kommer
- Det strålar en stjärna
- Gläns över sjö och strand
- Halleluja
- Hej mitt vinterland
- Hej tomtegubbar
- Jag drömmer om en jul hemma
- Jag såg mamma kyssa tomten
- Jul jul strålande jul
- Julbocken
- Mer jul
- Mössens julafton
- Nu tändas tusen juleljus
- Nu är det jul igen
- O helga natt
- Rudolph med röda mulen
- Sankta Lucia
- Sockerbagaren
- Stad i ljus
- Staffan var en stalledräng
- Staffansvisan
- Stilla Natt
- Tomtarnas julnatt
- Tomten jag vill ha en riktig jul
- Tre pepparkaksgubbar
- Tänd ett ljus

## Dependencies and Installing (not sure if necessary)

## Authors
Samuel Härner\
Marie Gotthardt

## References
[Blogpost: Fine-Tune Whisper For Multilingual ASR with 🤗 Transformers](https://huggingface.co/blog/fine-tune-whisper) \
[Article: Fine-Tuning Whisper ASR Models](https://wandb.ai/parambharat/whisper_finetuning/reports/Fine-Tuning-Whisper-ASR-Models---VmlldzozMTEzNDE5)

