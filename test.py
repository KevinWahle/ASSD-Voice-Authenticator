from speechbrain.pretrained import SpeakerRecognition
verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")

print("Same speaker:")
score, prediction = verification.verify_files("audio_samples\Kevin-1.wav", "audio_samples\Kevin-2.wav") # Same Speaker
print(score, prediction)
print()
print("Different speaker:")
score, prediction = verification.verify_files("audio_samples\Kevin-1.wav", "audio_samples\spk1_snt1.wav") # Different Speakers
print(score, prediction)
score, prediction = verification.verify_files("audio_samples\Kevin-1.wav", "audio_samples\spk2_snt1.wav") # Different Speaker
print(score, prediction)