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
| Pt    |   -32.5  |   -174.8  |   251.9  |    -44.6  |
| RawPt |    27.5  |   -124.8  |   141.9  |    -44.6  |
| AP    |     2.65 |      2.6  |     2.2  |      2.5  |
| RR    |    19.46 |     21.4  |    19.84 |     21.01 |
| WR    |    20.62 |     19.07 |    21.79 |     20.62 |
| DIR   |    15.18 |     16.73 |     9.73 |     17.51 |
| RenR  |    50    |     55    |    60    |     40    |
| A4R   |    65    |     70    |    85    |     80    |
| RWR   |    46    |     43.64 |    50.98 |     46.3  |
| RDIR  |     8    |     14.55 |    11.76 |      3.7  |
| APW   |  7932    |   6288    |  7412    |   6560    |
| APD   |  6682    |   6784    |  5004    |   6193    |
| 1st   |     4    |      3    |     7    |      6    |
| 2nd   |     6    |      8    |     5    |      2    |
| 3rd   |     3    |      3    |     5    |      8    |
| 4th   |     7    |      6    |     3    |      4    |
| HiScr | 75200    |  44600    | 77200    |  73200    |
| LoScr |  -700    | -36500    | -3200    | -24200    |
