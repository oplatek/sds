# Task #1 - 2

- `microphone.py` record voice from the microphone and print the transcribed text (Google) to `stdout`
- `cloudasr.py` transribe first 200 records by both Google and CloudASR dumping the output to `result/` directory
- `add_numbers.py` append `(n)` to each line (save to `_nr` suffix files)
- `result/` - each line in each file corresponds to a single record transcription

One should have `python3` with `speech_recognition` package (and it's dependencies) installed in order to run the scripts.

## Google

```
$ sclite -r truth_nr.txt -h google_nr.txt -i rm

[petr@hellmut result (master ✗)]$ sclite -r truth_nr.txt -h google_nr.txt -i rm 
sclite: 2.10 TK Version 1.3
Begin alignment of Ref File: 'truth_nr.txt' and Hyp File: 'google_nr.txt'
Error: extract_speaker can't locate RM id (1)
    Alignment# 1 for speaker           Error: extract_speaker can't locate RM id (2)
    Alignment# 2 for speaker           Error: extract_speaker can't locate RM id (3)
    Alignment# 3 for speaker           Error: extract_speaker can't locate RM id (4)
...
    Alignment# 193 for speaker           Error: extract_speaker can't locate RM id (194)
    Alignment# 194 for speaker           Error: extract_speaker can't locate RM id (195)
    Alignment# 195 for speaker           

                     SYSTEM SUMMARY PERCENTAGES by SPEAKER                      

      ,-----------------------------------------------------------------.
      |                          google_nr.txt                          |
      |-----------------------------------------------------------------|
      | SPKR   | # Snt  # Wrd | Corr    Sub    Del    Ins    Err  S.Err |
      |--------+--------------+-----------------------------------------|
      |        |  195    1148 | 11.5   29.1   59.4   14.5  103.0   91.3 |
      |=================================================================|
      | Sum/Avg|  195    1148 | 11.5   29.1   59.4   14.5  103.0   91.3 |
      |=================================================================|
      |  Mean  |195.0  1148.0 | 11.5   29.1   59.4   14.5  103.0   91.3 |
      |  S.D.  |  0.0    0.0  |  0.0    0.0    0.0    0.0    0.0    0.0 |
      | Median |195.0  1148.0 | 11.5   29.1   59.4   14.5  103.0   91.3 |
      `-----------------------------------------------------------------'

Successful Completion
```

## CloudASR
```
[petr@hellmut result (master ✗)]$ sclite -r truth_nr.txt -h cloudasr_nr.txt -i rm 
sclite: 2.10 TK Version 1.3
Begin alignment of Ref File: 'truth_nr.txt' and Hyp File: 'cloudasr_nr.txt'
Error: extract_speaker can't locate RM id (1)
    Alignment# 1 for speaker           Error: extract_speaker can't locate RM id (2)
    Alignment# 2 for speaker           Error: extract_speaker can't locate RM id (3)
    Alignment# 3 for speaker           Error: extract_speaker can't locate RM id (4)
...
    Alignment# 193 for speaker           Error: extract_speaker can't locate RM id (194)
    Alignment# 194 for speaker           Error: extract_speaker can't locate RM id (195)
    Alignment# 195 for speaker           

                     SYSTEM SUMMARY PERCENTAGES by SPEAKER                      

      ,-----------------------------------------------------------------.
      |                         cloudasr_nr.txt                         |
      |-----------------------------------------------------------------|
      | SPKR   | # Snt  # Wrd | Corr    Sub    Del    Ins    Err  S.Err |
      |--------+--------------+-----------------------------------------|
      |        |  195    1148 | 19.7   42.1   38.2   40.2  120.6   90.3 |
      |=================================================================|
      | Sum/Avg|  195    1148 | 19.7   42.1   38.2   40.2  120.6   90.3 |
      |=================================================================|
      |  Mean  |195.0  1148.0 | 19.7   42.1   38.2   40.2  120.6   90.3 |
      |  S.D.  |  0.0    0.0  |  0.0    0.0    0.0    0.0    0.0    0.0 |
      | Median |195.0  1148.0 | 19.7   42.1   38.2   40.2  120.6   90.3 |
      `-----------------------------------------------------------------'

Successful Completion
```
