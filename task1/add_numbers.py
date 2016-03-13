
if __name__ == '__main__':

    with open('result/cloudasr.txt', 'r') as cloudasr_fi,\
         open('result/google.txt', 'r') as google_fi,\
         open('result/truth.txt', 'r') as truth_fi,\
         open('result/cloudasr_nr.txt', 'w') as cloudasr_fo,\
         open('result/google_nr.txt', 'w') as google_fo,\
         open('result/truth_nr.txt', 'w') as truth_fo:

        for i, (cloudasr, google, truth) in enumerate(zip(cloudasr_fi, google_fi, truth_fi)):

            cloudasr_fo.write('{} ({})\n'.format(cloudasr[:-1], i+1))
            google_fo.write('{} ({})\n'.format(google[:-1], i+1))
            truth_fo.write('{} ({})\n'.format(truth[:-1], i+1))
