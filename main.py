from moduless import download_evidence, download_diseases, download_targets, get_data_from_evidence, \
    median_for_each_target_disease_pair, find_greatest_3_score, target_target_connection_share


def main():
    # print("Downloading evidence data")
    # download_evidence()

    # print("Downloading disease data")
    # download_diseases()

    # print("Downloading target data")
    # download_targets()

    print("Task 1")
    print("Generating CSV file with targetId, diseaseId and score from JSON")
    get_data_from_evidence()

    print("Task 2.A")
    print("Finding Median of each target disease pair")
    median_for_each_target_disease_pair()

    print("Task 2.B")
    print("Finding Greatest 3 values of each target disease pair")
    find_greatest_3_score()

    print("Task Additional 1")
    print("Total count of target-target pairs share a connection to at least two diseases")
    target_target_connection_share()


if __name__ == '__main__':
    main()
