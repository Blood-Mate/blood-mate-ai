# blood-mate-ai

## Updates
- 2023.03.09 Meta AI's LLAMA 7B was used! 
- 2023.03.11 LLAMA was not good enough.. Changed it to Meta AI's blenderbot 3B model.

## Usage
### 0. Requirements
```bash
pip install transformers
pip install langdetect
conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia
```

### 1. Demo
![image](https://user-images.githubusercontent.com/78339280/224489986-518d359d-b70d-4e64-840f-6d1f2fb71243.png)
```py
python bot.py
```  
![image](https://user-images.githubusercontent.com/78339280/224490420-b4b5c722-20c2-4a65-96df-d5cf50f093d3.png)  
Answering time is only 0.6 seconds.

## Environments
```
OS: Windows 11
GPU: Nvidia RTX 4090 24GB 
```

## TODO
- Korean chatbot
- Find out some other chatbot..
- Finetune with our blood-about dataset to help people

