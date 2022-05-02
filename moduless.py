import os
import requests
import json
import csv
import pandas as pd
import numpy as np

evidence_csv = "evidence.csv"
dataset_directory = "datasets"
output_directory = "outputs"


def check_directory(directory_name):
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
    return


def get_data_from_evidence():
    evidence_list = []
    print("Started Reading JSON file with multiple json")
    download_file_name = "00000"
    for i in range(200):
        print(f"Fetching File: {download_file_name}.json")
        with open(f'evidence/{download_file_name}.json') as f:
            for jsonObj in f:
                # evidenceDict = json.loads(jsonObj)
                evidence_list.append(json.loads(jsonObj))

        # update name
        download_file_name = str(int(download_file_name) + 1).zfill(5)

    check_directory(dataset_directory)
    with open(dataset_directory + "/" + evidence_csv, "w", newline="") as output:
        writer = csv.writer(output)
        print("Saving Json into a CSV")
        header = ['targetId', 'diseaseId', 'score']
        writer.writerow(header)
        count = 0
        for evidence in evidence_list:
            row = [f"{evidence['targetId']}", f"{evidence['diseaseId']}", evidence['score']]
            writer.writerow(row)
            count += 1

    print(f"Total Saved Data: {count}")
    check_directory(output_directory)
    df = pd.read_csv(dataset_directory + '/evidence.csv')
    df.to_json(output_directory + '/evidence.json', lines=True, orient='records')
    return


def target_target_connection_share():
    dataframe = pd.read_csv(dataset_directory+"/"+evidence_csv)
    print("Total size of the dataframe :" + str(len(dataframe)))

    target_df = dataframe.drop_duplicates(subset='targetId')
    disease_df = dataframe.drop_duplicates(subset='diseaseId')
    filtered_target_list = target_df['targetId']
    filtered_disease_list = disease_df['diseaseId']

    tdf = np.array(filtered_target_list)
    ddf = np.array(filtered_disease_list)

    # count of target to target pairs share a connection to at least two disease
    boolean_ndf = (dataframe['targetId'].isin(tdf)) & (dataframe['diseaseId'].isin(ddf))
    ndf = dataframe[boolean_ndf]
    duplicate_df = ndf.groupby(['targetId']).size().to_frame('size')
    duplicate_df = duplicate_df.loc[duplicate_df['size'] >= 2]
    check_directory(dataset_directory)
    duplicate_df.to_csv(dataset_directory + '/target_target.csv', index=False)
    check_directory(output_directory)
    duplicate_df.to_json(output_directory + '/target_target.json', lines=True, orient='records')
    print(f"Total count of target-target pairs share a connection to at least two diseases: {len(duplicate_df)}")
    return


def median_for_each_target_disease_pair():
    dataframe = pd.read_csv(dataset_directory+"/"+evidence_csv)
    print("Total size of the dataframe :" + str(len(dataframe)))

    # Median of each targetId and diseaseId pair
    mdf = dataframe.groupby(['targetId', 'diseaseId']).median().sort_values(['score', 'targetId', 'diseaseId'], ascending=True)
    check_directory(dataset_directory)
    mdf.to_csv(dataset_directory + '/target_disease_median_pairs.csv')
    check_directory(output_directory)
    df = pd.read_csv(dataset_directory + '/target_disease_median_pairs.csv')
    df.to_json(output_directory + '/median_pairs.json', lines=True, orient='records')
    print(mdf)
    print(len(mdf))
    return


def find_greatest_3_score():
    dataframe = pd.read_csv(dataset_directory+"/"+evidence_csv)
    print("Total size of the dataframe :" + str(len(dataframe)))

    ndf = dataframe.groupby(['targetId', 'diseaseId']).head(3).sort_values(['targetId', 'diseaseId', 'score'],
                                                                           ascending=False)
    check_directory(dataset_directory)
    ndf.to_csv(dataset_directory + '/great_3_data.csv', index=False)
    check_directory(output_directory)
    ndf.to_json(output_directory + '/great_3_data.json', lines=True, orient='records')
    print(ndf)
    print(len(ndf))
    return


def download_diseases():
    # url = "http://ftp.ebi.ac.uk/pub/databases/opentargets/platform/21.11/output/etl/json/diseases/"

    # download json files
    name = "00000"

    check_directory("disease")

    for i in range(16):
        print(f"Downloading diseases/{name}.json file.")
        url = "http://ftp.ebi.ac.uk/pub/databases/opentargets/platform/21.11/output/etl/json/diseases/" + \
              f"part-{name}-773deead-54e9-4934-b648-b26a4bbed763-c000.json"

        r = requests.get(url)
        with open("diseases/" + name + ".json", "wb") as f:
            f.write(r.content)

        # update name
        name = str(int(name) + 1).zfill(5)

    return


def download_targets():
    # url = "http://ftp.ebi.ac.uk/pub/databases/opentargets/platform/21.11/output/etl/json/targets/"

    # download json files
    name = "00000"

    check_directory("targets")

    for i in range(200):
        print(f"Downlaoding targets/{name}.json file.")
        url = "http://ftp.ebi.ac.uk/pub/databases/opentargets/platform/21.11/output/etl/json/targets/" + \
              f"part-{name}-9befc20b-ce53-4029-bd62-39c5b631aa3f-c000.json"

        r = requests.get(url)
        with open("targets/" + name + ".json", "wb") as f:
            f.write(r.content)

        # update name
        name = str(int(name) + 1).zfill(5)
    return


def download_evidence():
    # url = "http://ftp.ebi.ac.uk/pub/databases/opentargets/platform/latest/output/etl/json/evidence/sourceId%3Deva/"

    # download json files
    name = "00000"

    check_directory("evidence")

    for i in range(200):
        print(f"Downloading evidence/{name}.json file")
        url = "http://ftp.ebi.ac.uk/pub/databases/opentargets/platform/latest/output/etl/json/evidence/sourceId%3Deva/" + \
              f"part-{name}-c3e6253f-370b-4b63-8151-c735e5f6c98f.c000.json"
        # part-00001-c3e6253f-370b-4b63-8151-c735e5f6c98f.c000.json
        r = requests.get(url)
        with open("evidence/" + name + ".json", "wb") as f:
            f.write(r.content)
        # update name
        name = str(int(name) + 1).zfill(5)

    return
