# DLeague-Data

Data and its processing codes for our DLeague.  

## Usage

**Some** of the statstics are presented at the end. You may check [`docs/abbr_reference.md`](docs/abbr_reference.md) for abbreviations used in column-headers, or [`statistics`](statistics) for **all** calculated statistics.  

For data updates, modify `raw_data` and run `scripts/main.py`.  
To switch the rows shown in this README, modify `entries_switch` [here](scripts/utils.py#L22) and re-run `scripts/main.py`.  
To infer a hanchan's log-style flow from one game record, use `scripts/flow.py` with a game id such as `python scripts/flow.py -g S4/G37`. The script reads one `raw_data/S*/G*.json` file, infers each round's result using the stored scores and operation flags, and prints all plausible flows when a draw pattern is ambiguous.  

Standings note: `Pt` is the weighted total score used by the season format. It is calculated from each game's final score plus the season's placement-point offset, with regular-season games weighted according to `n_regular_games` in `scripts/main.py`. `RawPt` is the unweighted raw point total, calculated as each game's final score minus 25000 and summed across all games. Because these two rows use different weighting rules, `Pt - RawPt` is not simply the placement-point total.  

## Repo structure

[`raw_data`](raw_data) stores raw json files produced by *DLeague Light* and then concatenated manually.  
[`data`](data) stores two tables where each row records infos of a single game or round.  
[`scripts`](scripts) stores the python scripts used for proccessing data from raw.  

## Event Infos

The S3 season concluded on October 25, 2025, with player 0MRS emerging as the champion.

### Current Standings of S4

**Data updated to S4 G67**

|       |      LJL7 |      0MRS |      5JMY |      PARY |
|-------|-----------|-----------|-----------|-----------|
| Pt    |    -48.2  |      4.8  |    155.2  |   -111.7  |
| RawPt |    -62    |    -22.4  |    184.8  |   -100.4  |
| AP    |      2.55 |      2.45 |      2.39 |      2.58 |
| RR    |     19.52 |     21.45 |     18.67 |     19.28 |
| WR    |     20.84 |     21.81 |     20.96 |     20.6  |
| DIR   |     14.7  |     13.98 |     10.72 |     14.22 |
| RenR  |     50.75 |     52.24 |     55.22 |     43.28 |
| A4R   |     73.13 |     74.63 |     83.58 |     68.66 |
| RWR   |     46.3  |     48.31 |     46.45 |     45.62 |
| RDIR  |     14.2  |     11.8  |     12.26 |      8.12 |
| APW   |   7407    |   6886    |   7206    |   6771    |
| APD   |   6326    |   6292    |   5383    |   5910    |
| 1st   |     14    |     19    |     15    |     20    |
| 2nd   |     20    |     16    |     22    |      9    |
| 3rd   |     15    |     15    |     19    |     17    |
| 4th   |     18    |     17    |     11    |     21    |
| HiScr |  75200    |  84800    |  77200    |  94000    |
| LoScr | -52100    | -36500    | -14600    | -24200    |
