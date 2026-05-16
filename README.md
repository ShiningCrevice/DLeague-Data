# DLeague-Data

Data and its processing codes for our DLeague.  

## Usage

**Some** of the statstics are presented at the end. You may check [`docs/abbr_reference.md`](docs/abbr_reference.md) for abbreviations used in column-headers, or [`statistics`](statistics) for **all** calculated statistics.  

For data updates, modify `raw_data` and run `scripts/main.py`.  
To switch the rows shown in this README, modify `entries_switch` [here](scripts/utils.py#L22) and re-run `scripts/main.py`.  
To infer a hanchan's log-style flow from one game record, use `scripts/flow.py` with a game id such as `python scripts/flow.py -g S4/G37`. The script reads one `raw_data/S*/G*.json` file, infers each round's result using the stored scores and operation flags, and prints all plausible flows when a draw pattern is ambiguous.  

## Repo structure

[`raw_data`](raw_data) stores raw json files produced by *DLeague Light* and then concatenated manually.  
[`data`](data) stores two tables where each row records infos of a single game or round.  
[`scripts`](scripts) stores the python scripts used for proccessing data from raw.  

## Event Infos

The S3 season concluded on October 25, 2025, with player 0MRS emerging as the champion.

### Current Standings of S4

**Data updated to S4 G56**

|       |      LJL7 |      0MRS |      5JMY |      PARY |
|-------|-----------|-----------|-----------|-----------|
| Pt    |   -153.8  |    124.3  |    117.7  |    -88.2  |
| RawPt |    -97.5  |      7.2  |    157.3  |    -67    |
| AP    |      2.62 |      2.36 |      2.38 |      2.61 |
| RR    |     19.18 |     21.73 |     18.32 |     19.89 |
| WR    |     20.17 |     22.16 |     20.31 |     21.31 |
| DIR   |     14.35 |     14.77 |     10.23 |     14.63 |
| RenR  |     48.21 |     57.14 |     55.36 |     41.07 |
| A4R   |     69.64 |     76.79 |     83.93 |     69.64 |
| RWR   |     45.93 |     50.33 |     47.29 |     47.86 |
| RDIR  |     13.33 |     11.11 |      9.3  |      7.14 |
| APW   |   7394    |   6924    |   7365    |   6682    |
| APD   |   6461    |   6045    |   5575    |   5766    |
| 1st   |     11    |     17    |     13    |     16    |
| 2nd   |     16    |     15    |     18    |      7    |
| 3rd   |     12    |     11    |     16    |     16    |
| 4th   |     17    |     13    |      9    |     17    |
| HiScr |  75200    |  84800    |  77200    |  94000    |
| LoScr | -52100    | -36500    | -14600    | -24200    |
