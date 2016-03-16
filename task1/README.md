# Task #1 - 2

- `microphone.py` record voice from the microphone and print the transcribed text (Google) to `stdout`
- `cloudasr.py` transribe first 200 records by both Google and CloudASR dumping the output to `result/` directory
- `result/` - each line in each file corresponds to a single record transcription

One should have `python3` with `speech_recognition` package (and it's dependencies) installed in order to run the scripts.

## Google

```
[petr@hellmut result (master ✗)]$ sclite -r truth.txt -h google.txt -i rm
sclite: 2.10 TK Version 1.3
Begin alignment of Ref File: 'truth_nr.txt' and Hyp File: 'google_nr.txt'
Error: extract_speaker can't locate RM id (1)
    Alignment# 1 for speaker           Error: extract_speaker can't locate RM id (2)
    Alignment# 2 for speaker           Error: extract_speaker can't locate RM id (3)
    Alignment# 3 for speaker           Error: extract_speaker can't locate RM id (4)
...
    Alignment# 198 for speaker           Error: extract_speaker can't locate RM id (199)
    Alignment# 199 for speaker           Error: extract_speaker can't locate RM id (200)
    Alignment# 200 for speaker

                     SYSTEM SUMMARY PERCENTAGES by SPEAKER                      

      ,-----------------------------------------------------------------.
      |                           google.txt                            |
      |-----------------------------------------------------------------|
      | SPKR   | # Snt  # Wrd | Corr    Sub    Del    Ins    Err  S.Err |
      |--------+--------------+-----------------------------------------|
      |        |  200    1153 | 34.1   20.8   45.1    0.8   66.7   83.0 |
      |=================================================================|
      | Sum/Avg|  200    1153 | 34.1   20.8   45.1    0.8   66.7   83.0 |
      |=================================================================|
      |  Mean  |200.0  1153.0 | 34.1   20.8   45.1    0.8   66.7   83.0 |
      |  S.D.  |  0.0    0.0  |  0.0    0.0    0.0    0.0    0.0    0.0 |
      | Median |200.0  1153.0 | 34.1   20.8   45.1    0.8   66.7   83.0 |
      `-----------------------------------------------------------------'


Successful Completion
```

## CloudASR
```
[petr@hellmut result (master ✗)]$ sclite -r truth.txt -h cloudasr.txt -i rm
sclite: 2.10 TK Version 1.3
Begin alignment of Ref File: 'truth_nr.txt' and Hyp File: 'cloudasr_nr.txt'
Error: extract_speaker can't locate RM id (1)
    Alignment# 1 for speaker           Error: extract_speaker can't locate RM id (2)
    Alignment# 2 for speaker           Error: extract_speaker can't locate RM id (3)
    Alignment# 3 for speaker           Error: extract_speaker can't locate RM id (4)
...
    Alignment# 198 for speaker           Error: extract_speaker can't locate RM id (199)
    Alignment# 199 for speaker           Error: extract_speaker can't locate RM id (200)
    Alignment# 200 for speaker

                     SYSTEM SUMMARY PERCENTAGES by SPEAKER                      

      ,-----------------------------------------------------------------.
      |                          cloudasr.txt                           |
      |-----------------------------------------------------------------|
      | SPKR   | # Snt  # Wrd | Corr    Sub    Del    Ins    Err  S.Err |
      |--------+--------------+-----------------------------------------|
      |        |  200    1153 | 63.4   20.6   16.0    1.3   37.9   63.5 |
      |=================================================================|
      | Sum/Avg|  200    1153 | 63.4   20.6   16.0    1.3   37.9   63.5 |
      |=================================================================|
      |  Mean  |200.0  1153.0 | 63.4   20.6   16.0    1.3   37.9   63.5 |
      |  S.D.  |  0.0    0.0  |  0.0    0.0    0.0    0.0    0.0    0.0 |
      | Median |200.0  1153.0 | 63.4   20.6   16.0    1.3   37.9   63.5 |
      `-----------------------------------------------------------------'


Successful Completion
```
