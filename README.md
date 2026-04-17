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

**Data updated to S4 Hanchan #37**

|       |      LJL7 |      0MRS |     5JMY |      PARY |
|-------|-----------|-----------|----------|-----------|
| Pt    |   -428.3  |     77.8  |   386.9  |    -36.4  |
| RawPt |   -158.3  |    -22.2  |   226.9  |    -46.4  |
| AP    |      2.86 |      2.35 |     2.27 |      2.49 |
| RR    |     20.17 |     21.91 |    17.79 |     21.26 |
| WR    |     19.52 |     22.13 |    21.48 |     21.91 |
| DIR   |     15.4  |     15.18 |    10.63 |     15.18 |
| RenR  |     35.14 |     62.16 |    59.46 |     45.95 |
| A4R   |     62.16 |     75.68 |    89.19 |     72.97 |
| RWR   |     39.78 |     48.51 |    48.78 |     51.02 |
| RDIR  |     13.98 |     12.87 |     9.76 |      6.12 |
| APW   |   7092    |   6733    |  7658    |   6474    |
| APD   |   6968    |   6227    |  4794    |   5944    |
| 1st   |      6    |     10    |     9    |     12    |
| 2nd   |      7    |     13    |    13    |      5    |
| 3rd   |     10    |      5    |    11    |     10    |
| 4th   |     14    |      9    |     4    |     10    |
| HiScr |  75200    |  77100    | 77200    |  73200    |
| LoScr | -52100    | -36500    | -3200    | -24200    |
