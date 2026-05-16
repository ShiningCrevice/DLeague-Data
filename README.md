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

**Data updated to S4 G59**

|       |      LJL7 |      0MRS |      5JMY |      PARY |
|-------|-----------|-----------|-----------|-----------|
| Pt    |   -174.7  |     46    |     78.8  |     49.8  |
| RawPt |   -108.4  |    -21.1  |    148.5  |    -19    |
| AP    |      2.63 |      2.41 |      2.41 |      2.53 |
| RR    |     19.29 |     21.6  |     18.48 |     19.57 |
| WR    |     20.11 |     21.88 |     20.52 |     21.47 |
| DIR   |     14.4  |     14.81 |     10.46 |     14.27 |
| RenR  |     49.15 |     54.24 |     54.24 |     44.07 |
| A4R   |     69.49 |     76.27 |     83.05 |     71.19 |
| RWR   |     44.37 |     50.94 |     47.79 |     48.61 |
| RDIR  |     14.79 |     11.32 |     11.03 |      6.94 |
| APW   |   7336    |   6903    |   7228    |   6772    |
| APD   |   6361    |   6143    |   5599    |   5770    |
| 1st   |     11    |     17    |     13    |     19    |
| 2nd   |     18    |     15    |     19    |      7    |
| 3rd   |     12    |     13    |     17    |     16    |
| 4th   |     18    |     14    |     10    |     17    |
| HiScr |  75200    |  84800    |  77200    |  94000    |
| LoScr | -52100    | -36500    | -14600    | -24200    |
