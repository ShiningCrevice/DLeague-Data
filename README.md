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

|       |      LJL7 |      0MRS |     5JMY |      PARY |
|-------|-----------|-----------|----------|-----------|
| Pt    |   -210.5  |    -20.3  |   256.3  |    -25.5  |
| RawPt |    -80.5  |    -40.3  |   156.3  |    -35.5  |
| AP    |      2.78 |      2.43 |     2.26 |      2.48 |
| RR    |     20    |     22.76 |    19.31 |     21.72 |
| WR    |     19.31 |     21.72 |    22.07 |     20    |
| DIR   |     15.52 |     15.86 |     9.31 |     16.55 |
| RenR  |     43.48 |     60.87 |    56.52 |     43.48 |
| A4R   |     60.87 |     73.91 |    86.96 |     78.26 |
| RWR   |     39.66 |     50    |    51.79 |     47.62 |
| RDIR  |     12.07 |     12.12 |    10.71 |      3.17 |
| APW   |   7591    |   6810    |  7441    |   6919    |
| APD   |   7256    |   6587    |  4789    |   6160    |
| 1st   |      4    |      5    |     7    |      7    |
| 2nd   |      6    |      9    |     6    |      3    |
| 3rd   |      4    |      3    |     7    |      8    |
| 4th   |      9    |      6    |     3    |      5    |
| HiScr |  75200    |  77100    | 77200    |  73200    |
| LoScr | -52100    | -36500    | -3200    | -24200    |
