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

|       |     LJL7 |      0MRS |     5JMY |      PARY |
|-------|----------|-----------|----------|-----------|
| Pt    |   -11.2  |   -232.6  |   336.4  |    -92.6  |
| RawPt |    18.8  |   -132.6  |   176.4  |    -62.6  |
| AP    |     2.59 |      2.76 |     2    |      2.59 |
| RR    |    20.37 |     20.37 |    19.91 |     20.37 |
| WR    |    20.83 |     19.91 |    24.07 |     18.06 |
| DIR   |    14.81 |     18.06 |     7.87 |     18.52 |
| RenR  |    52.94 |     47.06 |    70.59 |     35.29 |
| A4R   |    70.59 |     64.71 |    88.24 |     76.47 |
| RWR   |    45.45 |     50    |    55.81 |     47.73 |
| RDIR  |     9.09 |     15.91 |     9.3  |      4.55 |
| APW   |  7667    |   6235    |  7492    |   7038    |
| APD   |  6788    |   7036    |  4965    |   5895    |
| 1st   |     3    |      2    |     7    |      5    |
| 2nd   |     6    |      6    |     5    |      1    |
| 3rd   |     3    |      3    |     3    |      7    |
| 4th   |     5    |      6    |     2    |      4    |
| HiScr | 57400    |  44600    | 77200    |  73200    |
| LoScr |  -700    | -36500    |  5000    | -24200    |
