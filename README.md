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

### Final Standings of S3

|       |     LJL7 |     0MRS |     5JMY |     PARY |
|-------|----------|----------|----------|----------|
| Pt    |  -167.8  |   130.3  |    63.5  |   -26.1  |
| RawPt |  -109    |   124.5  |   -46.4  |    30.9  |
| AP    |     2.59 |     2.51 |     2.45 |     2.45 |
| RR    |    19.77 |    15.32 |    14.83 |    19.93 |
| WR    |    22.24 |    22.08 |    17.13 |    21.09 |
| DIR   |    14    |    11.04 |    11.04 |    12.85 |
| RenR  |    50.98 |    41.18 |    54.9  |    52.94 |
| A4R   |    68.63 |    78.43 |    74.51 |    78.43 |
| RWR   |    43.33 |    54.84 |    44.44 |    46.28 |
| RDIR  |    16.67 |     8.6  |     7.78 |     9.92 |
| APW   |  6001    |  6681    |  7094    |  6708    |
| APD   |  5860    |  5607    |  5382    |  5288    |
| 1st   |    11    |    15    |    13    |    12    |
| 2nd   |    15    |     6    |    15    |    15    |
| 3rd   |     9    |    19    |    10    |    13    |
| 4th   |    16    |    11    |    13    |    11    |
| HiScr | 56700    | 72200    | 58200    | 58000    |
| LoScr | -7400    | -5200    | -3300    | -9400    |
