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
| Pt    |   -55.6  |   -24    |   184.5  |   -104.9  |
| RawPt |   -15.6  |   -14    |    94.5  |    -64.9  |
| AP    |     2.7  |     2.5  |     2    |      2.7  |
| RR    |    19.83 |    23.14 |    22.31 |     21.49 |
| WR    |    20.66 |    19.83 |    24.79 |     18.18 |
| DIR   |    15.7  |    14.88 |     6.61 |     19.01 |
| RenR  |    50    |    60    |    70    |     30    |
| A4R   |    70    |    70    |    90    |     70    |
| RWR   |    41.67 |    46.43 |    55.56 |     50    |
| RDIR  |    12.5  |    14.29 |    11.11 |      7.69 |
| APW   |  7276    |  7317    |  7667    |   7036    |
| APD   |  7158    |  6567    |  5688    |   6904    |
| 1st   |     1    |     2    |     4    |      3    |
| 2nd   |     4    |     4    |     3    |      0    |
| 3rd   |     2    |     1    |     2    |      4    |
| 4th   |     3    |     3    |     1    |      3    |
| HiScr | 35300    | 44600    | 74000    |  37100    |
| LoScr |  8000    |  2600    |  5000    | -24200    |
