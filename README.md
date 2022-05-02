# ETL

##

> Python 3.9.10

> pip 22.0.4

## Solution Approach
- Pandas 1.4.2 has been used to perform all the queries.

## Requirements

- Create and activate a virtual environment
- Run `pip install -r requirements.txt` to install all dependencies
- Run `python main.py` to Perform Task 1,2,5 and additional 1.

## Task Details
### Instructions

- Once you have downloaded the dataset, write a Python or Scala script that does the following:
> 1. Parse each evidence object and the `diseaseId`, `targetId`, and `score` fields.
> 2. For each `targetId` and `diseaseId` pair, calculate the median and 3 greatest `score`
values.
> 3. Join the targets and diseases datasets on the `targetId` = `target.id` and `diseaseId` =
`disease.id` fields.
> 4. Add the `target.approvedSymbol` and `disease.name` fields to your table
> 5. Output the resulting table in JSON format, sorted in ascending order by the median value of
the `score`.
- Each evidence object in the EVA evidence dataset defines a genetic association between a target
and a disease. Since there are a few hundred diseases and thousands of targets, different targets
will be connected to the same disease. Using the same dataset, extend your Python or Scala script to:
> 1. Count how many target-target pairs share a connection to at least two diseases.


## Step to solve the tasks
### Downloading required file
- GOTO folder of `evidence=eva`

- Point to the first file of the folder

- Create if not exists directory in local machine

- LOOP Download till the last file

### Task 1: Reading evidence object and save targetId, diseaseId and score
- DECLARE Empty EvidenceList

- LOOP till Json file exists

- JsonObject = Load Data From Json File

- EvidenceList.Append = JsonObject

- SAVE EvidenceList to csv

### Task 2.a: Calculating the median of targetId and diseaseId pair
- LOAD csv into Dataframe1
- Dataframe1 = GroupBy [TargetIdList, DiseaseIdList].Median.Sort by Score
- SAVE the Dataframe1

### Task 2.b: Finding out 3 greatest score of targetId and diseaseId pair
- LOAD csv into Dataframe1
- Dataframe1 = GroupBy [TargetIdList, DiseaseIdList].Get Top 3/Pair
- SAVE the Dataframe1

### Task Additional 1: Finding out how many the target target share connection with at least 2 disease 
- LOAD csv into Dataframe1
- FIND Unique values from targetId
- FIND Unique values from diseaseId
- CHECK if TargetIdList and DiseaseIdList IS IN Dataframe
- CREATE Dataframe2 = Duplicate values TargetIdList with size
- FIND Which targetId has at lease two duplicates
- SAVE the Dataframe2
- Display length of Dataframe2

### Task 3 and 4
- The given dataset of target and disease is fully different. There was no common column to join them. Having trouble to understand the problem, couldn't resolve the task 3 since task 4 is related to task 3, it is remain unsolved.

## Problem Outputs and Solution Screenshots
- **Task 1:** Fetched `evidence=eva` objects and collect `targetId`, `diseaseId` and `score`

![Task 1](https://enactbs.com/ebi/parsing_object_and_collect_task_1.JPG)

- **Task 2.a:** Find Median of each `targetId` and `diseaseId` pairs

![Task 2.a](https://enactbs.com/ebi/median_pairs.JPG)

- **Task 2.b:** Find greatest 3 values of each `targetId` and `diseaseId` pairs

![Task 2.b](https://enactbs.com/ebi/great_3_data.JPG)

- **Task 5:** Output the resulting table in JSON format, sorted in ascending order by the median value ofthe `score`.

![Task 5](https://enactbs.com/ebi/median_pairs.JPG)

- **Task Additional 1:** Count how many target-target pairs share a connection to at least two diseases. 

> Ans: 5013

![Task 5](https://enactbs.com/ebi/target_target_count_with_at_least_two_disease.JPG)