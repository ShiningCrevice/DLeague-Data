# DLeague-Data

Data and its processing codes for our DLeague.  

## Usage

**Some** of the statstics are presented at the end. You may check [`docs/abbr_reference.md`](docs/abbr_reference.md) for abbreviations used in column-headers, or [`statistics`](statistics) for **all** calculated statistics.  

For data updates, modify `raw_data` and run `scripts/main.py`.  
To switch the rows shown in this README, modify `entries_switch` [here](scripts/utils.py#L22) and re-run `scripts/main.py`.  

## Repo structure

[`raw_data`](raw_data) stores raw json files produced by *DLeague Light* and then concatenated manually.  
[`data`](data) stores two tables where each row records infos of a single game or round.  
[`scripts`](scripts) stores the python scripts used for proccessing data from raw.  

## Event Infos

The S3 season concluded on October 25, 2025, with player 0MRS emerging as the champion.

### Current Standings of S4

|       |     LJL7 |     0MRS |     5JMY |      PARY |
|-------|----------|----------|----------|-----------|
| Pt    |   -21.3  |  -102.1  |   243.5  |   -120.1  |
| RawPt |    -1.3  |   -52.1  |   133.5  |    -80.1  |
| AP    |     2.57 |     2.64 |     2.07 |      2.64 |
| RR    |    18.34 |    21.3  |    22.49 |     19.53 |
| WR    |    20.71 |    20.12 |    25.44 |     17.75 |
| DIR   |    15.38 |    18.34 |     9.47 |     18.34 |
| RenR  |    50    |    57.14 |    71.43 |     28.57 |
| A4R   |    71.43 |    64.29 |    85.71 |     78.57 |
| RWR   |    45.16 |    52.78 |    55.26 |     51.52 |
| RDIR  |     9.68 |    11.11 |    10.53 |      6.06 |
| APW   |  6963    |  6497    |  7198    |   6650    |
| APD   |  6658    |  6010    |  4756    |   6245    |
| 1st   |     3    |     2    |     5    |      4    |
| 2nd   |     4    |     6    |     5    |      0    |
| 3rd   |     3    |     1    |     2    |      7    |
| 4th   |     4    |     5    |     2    |      3    |
| HiScr | 57400    | 44600    | 77200    |  37100    |
| LoScr |  -200    |  2600    |  5000    | -24200    |
