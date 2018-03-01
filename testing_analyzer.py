import csv


threshold = 0.6

with open('testing_analysis.csv', 'w', newline='') as csvfile:
    analysis_writer = csv.writer(csvfile, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
    analysis_writer.writerow(['threshold','false_positives','false_negatives','true_positives','true_negatives'])
    
    for step in range(110):
        threshold = step/100 
        false_positives = 0
        false_negatives = 0
        true_positives = 0
        true_negatives = 0
        with open('testing_results.csv', newline='') as csvfile:
            results_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in results_reader:
                if( float( row[4]) >= threshold ):
                    if(row[1] == row[3]):
                        true_positives += 1
                    else:
                        false_positives += 1
                else:
                    if(row[4] != row[3]):
                        true_negatives += 1
                    else:
                        false_negatives +=1
        total = false_positives + false_negatives + true_positives + true_negatives
        false_positives /= total
        false_negatives /= total
        true_positives /= total
        true_negatives /= total
        analysis_writer.writerow([threshold,false_positives,false_negatives,true_positives,true_negatives])









