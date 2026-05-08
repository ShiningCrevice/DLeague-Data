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

**Data updated to S4 G50**

|       |      LJL7 |      0MRS |     5JMY |      PARY |
|-------|-----------|-----------|----------|-----------|
| Pt    |   -167.5  |     45.7  |   319.3  |   -197.5  |
| RawPt |    -47.5  |    -54.3  |   199.3  |    -97.5  |
| AP    |      2.62 |      2.38 |     2.36 |      2.6  |
| RR    |     19.64 |     21.75 |    18.34 |     19.81 |
| WR    |     21.43 |     21.43 |    20.62 |     21.1  |
| DIR   |     14.45 |     14.45 |    10.71 |     15.42 |
| RenR  |     48    |     58    |    54    |     42    |
| A4R   |     70    |     76    |    86    |     68    |
| RWR   |     46.28 |     47.76 |    48.67 |     46.72 |
| RDIR  |     13.22 |     11.19 |     8.85 |      7.38 |
| APW   |   7271    |   6759    |  7537    |   6578    |
| APD   |   6566    |   6291    |  5367    |   5667    |
| 1st   |     10    |     14    |    12    |     15    |
| 2nd   |     14    |     15    |    15    |      6    |
| 3rd   |     11    |      9    |    16    |     13    |
| 4th   |     15    |     12    |     7    |     16    |
| HiScr |  75200    |  77100    | 77200    |  73200    |
| LoScr | -52100    | -36500    | -3200    | -24200    |
