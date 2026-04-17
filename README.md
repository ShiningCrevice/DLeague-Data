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

**Data updated to S4 G40**

|       |      LJL7 |      0MRS |     5JMY |      PARY |
|-------|-----------|-----------|----------|-----------|
| Pt    |   -420.8  |    107.4  |   280.8  |     32.6  |
| RawPt |   -160.8  |    -22.6  |   190.8  |     -7.4  |
| AP    |      2.83 |      2.33 |     2.38 |      2.45 |
| RR    |     19.8  |     22.02 |    18.18 |     20.61 |
| WR    |     19.6  |     22.42 |    20.81 |     22.22 |
| DIR   |     14.95 |     15.15 |    10.71 |     14.95 |
| RenR  |     37.5  |     62.5  |    55    |     47.5  |
| A4R   |     65    |     77.5  |    85    |     72.5  |
| RWR   |     40.82 |     49.54 |    47.78 |     50.98 |
| RDIR  |     14.29 |     11.93 |     8.89 |      6.86 |
| APW   |   7018    |   6717    |  7652    |   6624    |
| APD   |   6838    |   6207    |  5072    |   5742    |
| 1st   |      6    |     11    |     9    |     14    |
| 2nd   |      9    |     14    |    13    |      5    |
| 3rd   |     11    |      6    |    12    |     10    |
| 4th   |     14    |      9    |     6    |     11    |
| HiScr |  75200    |  77100    | 77200    |  73200    |
| LoScr | -52100    | -36500    | -3200    | -24200    |
