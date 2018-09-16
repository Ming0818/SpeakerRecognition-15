import pickle
import numpy as np
from scipy.io.wavfile import read
from sklearn.mixture import GMM 
from featureextraction import extract_features
import warnings
warnings.filterwarnings("ignore")

source   = "/home/binhnguyen/PycharmProjects/SpeakerIdentify/trainingData/"
dest = "/home/binhnguyen/PycharmProjects/SpeakerIdentify/Gmm/Speakers_models/"
train_file = "trainingDataPath.txt"        
file_paths = open(train_file,'r')

count = 1

features = np.asarray(())
for path in file_paths:    
    path = path.strip()   
    print path
    
    # read the audio
    sr,audio = read(source + path)
    print(audio)
    print(audio.shape)
    # extract 40 dimensional MFCC & delta MFCC features
    vector   = extract_features(audio,sr)
    print(vector.shape)
    if features.size == 0:
        features = vector
    else:
        features = np.vstack((features, vector))
    if count == 8:
        gmm = GMM(n_components = 16, n_iter = 200, covariance_type='diag',n_init = 3)
        gmm.fit(features)
        
        # dumping the trained gaussian model/binhnq/SpeakerIdentify/Gmm
        picklefile = path.split("/")[0]+".gmm"
        # picklefile = picklefile.replace(".wav","")
        pickle.dump(gmm,open(dest + picklefile,'w'))

        print '+ modeling complted for speaker:',picklefile," with data point = ",features.shape
        features = np.asarray(())
        count = 0
    count = count + 1
