Directory for ASR

Instructions for install:

1. Install kaldi from here: https://github.com/kaldi-asr/kaldi
2. Create a folder "malasakit-digits" in the egs directory under kaldi-master
3. Put all the files from ASR folder in this github into the malasakit-digits folder.


Usage of ASR:

Usage: . ./recognize_gmm.sh <audio_file_name> <language> [ <model_version> <confidence_eqn_no> ]

inputs:

audio_file_name: 	full path of the audio file to be recognized
language: 		[ eng, fil, ceb, ilk ] (default is fil) eng for English, fil for Filipino, ceb for Cebuano, ilk for Ilokano
model_version:		(optional, default is tri2) [ tri1, tri2, tri3 ] tri1 for the model trained utilizing double delta features, tri2 for 				double delta with LDA and MLLT, tri3 for double delta with LDA, MLLT, and SAT
confidence_eqn_no:    	(optional, default is 2) (under experimentation) [ 1, 2 ]

outputs:

recognition/recognized_digit.txt:	the recognized digit in numerical form
recognition/recognized_word.txt:	the recognized digit in word form
recognition/confidence_score.txt:	confidence value [ 0 - 1 ]