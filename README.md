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

**Data updated to S4 G62**

|       |      LJL7 |      0MRS |      5JMY |      PARY |
|-------|-----------|-----------|-----------|-----------|
| Pt    |    -79.8  |     -2.5  |    105.3  |    -23.1  |
| RawPt |    -63.6  |    -39.6  |    165    |    -61.8  |
| AP    |      2.58 |      2.44 |      2.4  |      2.55 |
| RR    |     19.53 |     21.73 |     18.63 |     19.4  |
| WR    |     20.57 |     21.99 |     20.57 |     20.96 |
| DIR   |     14.23 |     14.62 |     10.61 |     14.36 |
| RenR  |     50    |     53.23 |     54.84 |     43.55 |
| A4R   |     70.97 |     75.81 |     83.87 |     69.35 |
| RWR   |     45.03 |     48.81 |     48.61 |     47.33 |
| RDIR  |     14.57 |     11.9  |     11.11 |      8    |
| APW   |   7390    |   6824    |   7225    |   6831    |
| APD   |   6383    |   6234    |   5434    |   5863    |
| 1st   |     13    |     17    |     13    |     20    |
| 2nd   |     18    |     16    |     21    |      7    |
| 3rd   |     13    |     14    |     18    |     16    |
| 4th   |     18    |     15    |     10    |     19    |
| HiScr |  75200    |  84800    |  77200    |  94000    |
| LoScr | -52100    | -36500    | -14600    | -24200    |
