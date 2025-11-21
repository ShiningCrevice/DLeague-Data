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
| Pt    |     6.2  |    51.7  |   -36.1  |   -21.8  |
| RawPt |    -3.8  |    21.7  |    -6.1  |   -11.8  |
| AP    |     2.33 |     2    |     3    |     2.67 |
| RR    |    15.38 |    25.64 |    23.08 |    23.08 |
| WR    |    20.51 |    20.51 |    15.38 |    17.95 |
| DIR   |    17.95 |    12.82 |     5.13 |    23.08 |
| RenR  |    66.67 |    66.67 |    33.33 |    33.33 |
| A4R   |   100    |    66.67 |    66.67 |    66.67 |
| RWR   |    33.33 |    50    |    33.33 |    55.56 |
| RDIR  |    16.67 |    10    |     0    |     0    |
| APW   |  7000    |  8750    |  5283    |  8143    |
| APD   |  7957    |  6020    |  6250    |  6644    |
| 1st   |     0    |     2    |     0    |     1    |
| 2nd   |     2    |     0    |     1    |     0    |
| 3rd   |     1    |     0    |     1    |     1    |
| 4th   |     0    |     1    |     1    |     1    |
| HiScr | 30800    | 44600    | 39700    | 37100    |
| LoScr | 15800    | 14100    |  5000    |  -100    |
