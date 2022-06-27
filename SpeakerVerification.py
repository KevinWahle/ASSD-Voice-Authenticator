import torchaudio
from speechbrain.pretrained import SpeakerRecognition

# Carga de archivo y normalizacion
def _loadFile(filePath):
    fs_norm = 16000     # Frecuencia de sampleo necesaria para hacer la comparacion
    
    signal, fs = torchaudio.load(filePath)

    # Conversion a mono
    if len(signal.shape) > 1:
        signal = signal.mean(axis=0)
    # signal.reshape(-1)

    # Si es necesario se realiza resampleo
    if fs != fs_norm:
        signal = torchaudio.transforms.Resample(fs, fs_norm)(signal)

    return signal

def verifySpeaker(file1, file2):

    #ECAPA-TDNN Model
    verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")

    TH = 0.5            # Limite donde se consideran iguales
    
    verify = lambda x, y: verification.verify_batch(x, y, threshold=TH)

    audio1 = _loadFile(file1)
    audio2 = _loadFile(file2)

    score, prediction = verify(audio1, audio2)
    
    score = score.item()
    prediction = prediction.item()

    return score, prediction


if __name__ == "__main__":
    print(verifySpeaker("audio_samples\Kevin-1.wav", "audio_samples\Kevin-2.wav"))
    print(verifySpeaker("audio_samples\Sergio-1.mp3", "audio_samples\Sergio-2.mp3"))
    print(verifySpeaker("audio_samples\Kevin-1.wav", "audio_samples\Sergio-1.mp3"))