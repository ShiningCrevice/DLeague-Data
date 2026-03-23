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
| Pt    |   -448.2  |    109.4  |   352.3  |    -13.5  |
| RawPt |   -178.2  |      9.4  |   192.3  |    -23.5  |
| AP    |      2.91 |      2.33 |     2.24 |      2.48 |
| RR    |     20.99 |     21.73 |    18.52 |     20.25 |
| WR    |     18.77 |     22.47 |    21.48 |     21.98 |
| DIR   |     15.56 |     15.31 |    10.37 |     15.06 |
| RenR  |     36.36 |     60.61 |    60.61 |     45.45 |
| A4R   |     57.58 |     75.76 |    90.91 |     75.76 |
| RWR   |     38.82 |     51.14 |    49.33 |     52.44 |
| RDIR  |     14.12 |     12.5  |    10.67 |      3.66 |
| APW   |   7108    |   6875    |  7605    |   6525    |
| APD   |   7129    |   6224    |  4762    |   6043    |
| 1st   |      5    |     10    |     8    |     10    |
| 2nd   |      7    |     10    |    12    |      5    |
| 3rd   |      7    |      5    |    10    |     10    |
| 4th   |     14    |      8    |     3    |      8    |
| HiScr |  75200    |  77100    | 77200    |  73200    |
| LoScr | -52100    | -36500    | -3200    | -24200    |
