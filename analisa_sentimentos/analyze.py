from carpet import (
    csv_to_list,
    evaluate_job_file,
    get_files_in_directory,
    order_by_key,
)

METRICS_FILENAME = 'metrics.csv'
JOBS_DIRECTORY = 'jobs'

if __name__ == '__main__':
    results = []
    metrics = csv_to_list(METRICS_FILENAME)
    job_files = get_files_in_directory(JOBS_DIRECTORY)
    # cont = 1
    # for i in job_files:
    #     print(u'{} - {}'.format(cont,i))
    #     cont+=1
    # print(len(job_files))
    #  ruim: 8 - 32 - 33 - 34 - 35

    for job_file in job_files[:-1]:
        # print(job_file)
        poor_level, match_words = evaluate_job_file(job_file, metrics)
        results.append({
            'job_file': job_file,
            'poor_level': poor_level,
            'match_words': match_words,
        })
    # [print(result) for result in results]
    results_by_poor_level = order_by_key(results, 'poor_level')
    # [print(result) for result in results_by_poor_level]
    for result in results_by_poor_level:
        print('Poor level: {} - Job file: {} - Words: {}'.format(
            result['poor_level'],
            result['job_file'],
            result['match_words'],
        ))
