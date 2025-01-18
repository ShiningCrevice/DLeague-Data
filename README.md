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

## Statistics

### S2 (Final)

|       |     LJL7 |     0MRS |     5JMY |     PARY |
|-------|----------|----------|----------|----------|
| Pt    |   111.9  |  -159.2  |    77.5  |   -30.1  |
| RawPt |    66.8  |  -121    |   102.8  |   -48.6  |
| AP    |     2.5  |     2.56 |     2.47 |     2.47 |
| RenR  |    50    |    51.52 |    46.97 |    51.52 |
| A4R   |    72.73 |    66.67 |    83.33 |    77.27 |
| 1st   |    18    |    17    |    15    |    16    |
| 2nd   |    15    |    17    |    16    |    18    |
| 3rd   |    15    |    10    |    24    |    17    |
| 4th   |    18    |    22    |    11    |    15    |
| HiScr | 66400    | 62600    | 70200    | 50800    |

### S1 (Final)

|       |     LJL7 |     0MRS |     5JMY |     PARY |
|-------|----------|----------|----------|----------|
| Pt    |    64.2  |  -156.5  |    35.6  |    55.1  |
| RawPt |    25.8  |  -134.2  |    19.1  |    89.3  |
| AP    |     2.46 |     2.85 |     2.38 |     2.31 |
| RenR  |    58.97 |    28.21 |    53.85 |    58.97 |
| A4R   |    79.49 |    66.67 |    79.49 |    74.36 |
| 1st   |     6    |     8    |    11    |    14    |
| 2nd   |    17    |     3    |    10    |     9    |
| 3rd   |     8    |    15    |    10    |     6    |
| 4th   |     8    |    13    |     8    |    10    |
| HiScr | 91700    | 61000    | 49300    | 77300    |
