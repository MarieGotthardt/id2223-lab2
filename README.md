# Swedish Speech Recognition Using a Fine-Tuned Whisper Small Model
Second Lab Assignment within the course ID2223 *Scalable Machine Learning and Deep Learning*.

## Description of our System
In this assignment, we fine-tuned a pre-trained transformer model (Whisper small) for Swedish speech recognition, following this blogpost: [Fine-Tune Whisper For Multilingual ASR with 🤗 Transformers](https://huggingface.co/blog/fine-tune-whisper) by Sanchit Gandhi. Furthermore, we created a serverless UI that utilizes our model. Our system consists of the following pipelines:

- Feature Pipeline (only requires CPU)
- Training Pipeline (requires GPU)
- Inference Program (run as an app in a Hugging Face Space which you can find [here](https://huggingface.co/spaces/SamuelHarner/whisper-swedish))

## Experiments for Performance Optimization
In order to improve the performance of our model, we performed experiments with model-centric optimization techniques and with data-centric optimization techniques. 
To be able to compare our experimental results, we created a baseline model with the following configurations:

- lr = 1e-5, scheduler: linear, warmup steps = 200, dropout = 0.0, training steps = 1000
  
| Checkpoint | 200 | 400 | 600 | 800 | 1000|
|------------|-----|-----|-----|-----|-----|
|WER         |59.32|60.32|46.04|47.68|63.25|

### Model-centric Optimization
As part of the model-centric optimization, we experimented with the following techniques:
- adding dropout (dropout = 0.1)
- using different learning rates (learning rate = 1e-4, 1e-5)
- using different learning rate schedulers (linear learning rate scheduler, cosine with hard restarts scheduler)
- using different numbers of warmup steps (10, 20, 200)


**Experiments and Results**
- lr = 1e-4, lr scheduler: linear, warmup steps = 10, dropout = 0.0, training steps= 300

| Checkpoint | 100 | 200 | 300 | 
|------------|-----|-----|-----|
|WER         |70.71|25.37|23.95|
  
- lr = 1e-5, lr scheduler: linear, warmup steps = 20, dropout = 0.1, training steps = 200
  
| Checkpoint | 100 | 200| 
|------------|-----|-----|
|WER         |103.66|25.53|

- lr = 1e-4. lr scheduler: cosine with hard restarts, warmup steps = 200, dropout = 0.0, training steps = 1000: **WER** = 103.39
- lr = 1e-4, lr scheduler: linear, warmup steps = 10, dropout = 0.1, training steps = 800

| Checkpoint | 200 | 400 | 600 | 800 |
|------------|-----|-----|-----|-----|
|WER         |45.57|40.59|31.74|27.87|

- lr = 1e-5, lr scheduler: linear, warmup steps = 20, dropout = 0.1, training steps = 800

| Checkpoint | 200 | 400 | 600 | 800 |
|------------|-----|-----|-----|-----|
|WER         |25.21|23.69|22.66|22.10|

### Data-centric Optimization
For the data-centric approach, we performed an experiment with a combination of the following data augmentations:
- Gaussian noise
- Time stretch
- Pitch shift

based on the article [Fine-Tuning Whisper ASR Models](https://wandb.ai/parambharat/whisper_finetuning/reports/Fine-Tuning-Whisper-ASR-Models---VmlldzozMTEzNDE5) by Bharat Ramanathan.

  **Experiments and Results with Augmented Data**
  - lr = 1e-5, scheduler: linear, warmup steps = 200, dropout = 0.0, training steps = 1000
    
| Checkpoint |500|1000|
|---|---|---|
|WER|47.91|65.20|

  - lr=1e-4, scheduler: linear, warmup steps = 10, dropout = 0.1, training steps = 1000
    
| Checkpoint |200|400|600|800|1000|
|---|---|---|---|---|---|
|WER |45.30|37.32|31.74|27.40|31.09|

**Parameter Settings and Results of the Best Performing Model**
 - lr=1e-5, scheduler: linear, warmup steps = 20, dropout = 0.1, training steps = 1600

| Checkpoint |200|400|600|800|1000|1200|1400|1600|
|---|---|---|---|---|---|---|---|---|---|
|WER |25.21|23.69|22.66|22.10|22.34|22.30|21.91|21.76|
 

## Utilization of our Model: Recognition of Swedish Christmas Songs
To demonstrate how users could utilize our fine-tuned model to automatically create transcriptions for Swedish, we created an app that can automatically identify Swedish Christmas songs based on the created transcriptions.

The identification of songs was done by using [MinHashing](https://ekzhu.com/datasketch/minhash.html) for estimating the [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between the transcription and the lyrics of a selection of songs. The song which had the highest estimated Jaccard similarity with the transcription was chosen as the song identification guess.

## Discussion of our Results and Approach
By using different optimization techniques, we were able to considerably improve the WER (best WER = TODO) compared to our baseline model (best WER = 46.04). According to [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data?pivots=speech-studio), a WER of ~ 20% is acceptable for speech to text models although further improvements or more training should be considered. 
When comparing our results to other results on the Swedish common voice dataset achieved by different Whisper models ([Papers With Code: Automatic Speech Recognition on mozilla-foundation/common_voice_11_0 sv-SE](https://paperswithcode.com/sota/automatic-speech-recognition-on-mozilla-75)), we can see that we perform considerably better than the Whisper Small Swedish Fast (WER = 62.69) and the Whisper Tiny Swedish (44.19) but worse than the Whsiper Medium Sv (WER = 10.712). Furthermore, there are other state-of-the-art Wav2vec models trained on the Swedish common voice dataset ([Papers With Code: Speech Recognition on Common Voice Swedish](https://paperswithcode.com/sota/speech-recognition-on-common-voice-swedish)), that have achieved a WER as low as 6.472%. 

One technical challenge we had to face during training was our limited GPU access, as we needed a GPU to train our model. To counter this problem, we regularly checkpointed our model weights so we could resume model training from these checkpoints in case we lost access to our GPU. Nevertheless, this circumstance limited the extent to which we could perform experiments for model optimization. 

One limitation to consider regarding the app we created to automatically identify Swedish Christmas songs is that we only used a selection of Swedish Christmas songs. Thus, if a user sings a song not included in our selection, our app is not able to identify it correctly. The songs were manually chosen based on what Swedish Christmas songs are generally popular and the lyrics for the songs were gathered from various sources that appeared from Google Search results, many song lyrics were for example collected from the following website [julsånger.se](https://www.xn--julsnger-d0a.se/).

Songs in our selection:
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

Another limitation is that the MinHashing method is not guaranteed to provide a good guess for the song the user sang as it may provide incorrect guesses even if the user sings a song that is in our selection, however, the user can increase the likelihood of a correct guess by singing more clearly and singing more of the song lyrics.

## Development Environment
- Google Colab was used as the environment for running the pipelines
- Google Drive was used as the feature store to store training data
- For running the `song_guesser.py` program (used in Hugging Face app) the [`datasketch`](https://ekzhu.com/datasketch/index.html) library is necessary

## Authors
Samuel Härner\
Marie Gotthardt

## References
[Blogpost: Fine-Tune Whisper For Multilingual ASR with 🤗 Transformers](https://huggingface.co/blog/fine-tune-whisper) \
[Article: Fine-Tuning Whisper ASR Models](https://wandb.ai/parambharat/whisper_finetuning/reports/Fine-Tuning-Whisper-ASR-Models---VmlldzozMTEzNDE5) \
[Documentation: MinHash in datasketch library](https://ekzhu.com/datasketch/minhash.html) \
[Article: Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) \
[Website: Swedish Christmas songs (julsånger.se)](https://www.xn--julsnger-d0a.se/) \
[Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data?pivots=speech-studio) \
[Papers With Code: Automatic Speech Recognition on mozilla-foundation/common_voice_11_0 sv-SE](https://paperswithcode.com/sota/automatic-speech-recognition-on-mozilla-75) \
[Papers With Code: Speech Recognition on Common Voice Swedish](https://paperswithcode.com/sota/speech-recognition-on-common-voice-swedish)
