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

**Data updated to S4 G53**

|       |      LJL7 |      0MRS |      5JMY |      PARY |
|-------|-----------|-----------|-----------|-----------|
| Pt    |   -181.3  |     88.2  |    108.7  |    -15.6  |
| RawPt |   -115.1  |      1.1  |    158.3  |    -44.3  |
| AP    |      2.64 |      2.38 |      2.38 |      2.57 |
| RR    |     19.22 |     21.62 |     18.62 |     20.12 |
| WR    |     20.42 |     21.92 |     20.42 |     21.47 |
| DIR   |     14.71 |     14.56 |     10.66 |     14.86 |
| RenR  |     47.17 |     56.6  |     54.72 |     43.4  |
| A4R   |     67.92 |     77.36 |     84.91 |     69.81 |
| RWR   |     45.31 |     50.69 |     47.58 |     47.01 |
| RDIR  |     13.28 |     10.42 |      9.68 |      7.46 |
| APW   |   7349    |   6984    |   7467    |   6709    |
| APD   |   6537    |   6179    |   5613    |   5672    |
| 1st   |     11    |     15    |     12    |     16    |
| 2nd   |     14    |     15    |     17    |      7    |
| 3rd   |     11    |     11    |     16    |     14    |
| 4th   |     17    |     12    |      8    |     16    |
| HiScr |  75200    |  84800    |  77200    |  94000    |
| LoScr | -52100    | -36500    | -14600    | -24200    |
