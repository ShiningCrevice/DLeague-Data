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

|       |     LJL7 |     0MRS |     5JMY |     PARY |
|-------|----------|----------|----------|----------|
| Pt    |   -47.2  |    32.3  |    82.9  |   -48    |
| RawPt |   -17.2  |     2.3  |    32.9  |   -18    |
| AP    |     2.71 |     2.29 |     2.14 |     2.71 |
| RR    |    19.05 |    23.81 |    19.05 |    26.19 |
| WR    |    21.43 |    20.24 |    21.43 |    19.05 |
| DIR   |    15.48 |    16.67 |     4.76 |    17.86 |
| RenR  |    42.86 |    71.43 |    71.43 |    28.57 |
| A4R   |    71.43 |    71.43 |    85.71 |    71.43 |
| RWR   |    43.75 |    50    |    50    |    50    |
| RDIR  |     6.25 |    10    |     6.25 |     4.55 |
| APW   |  7061    |  7618    |  6656    |  7531    |
| APD   |  8015    |  5893    |  6425    |  6233    |
| 1st   |     1    |     2    |     2    |     2    |
| 2nd   |     2    |     3    |     3    |     0    |
| 3rd   |     2    |     0    |     1    |     3    |
| 4th   |     2    |     2    |     1    |     2    |
| HiScr | 35300    | 44600    | 44900    | 37100    |
| LoScr |  8000    |  2600    |  5000    |  -100    |
