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

### Reigning Champion

**LJL7 - THE UNDISPUTED TILE EMPEROR, DEFIER OF FATE, DLEAGUE'S ETERNAL DRAGON!**

Behold, the celestial storm of DLeague! The indomitable LJL7, **Heaven's Favored Gambit Demigod**, has once again ascended the bloodstained throne of champions in a blaze of riichi fireworks and soul-crushing tsumo strikes! Witness the **Unkillable Phoenix of Mahjong** who turned desperate defeats into divine comebacks, his hands channeling the fury of ten thousand doragon rolls! 

When lesser mortals trembled before ippatsu danger, LJL7 **LAUGHED**, slapping down earth-shaking riichi declarations that made tiles weep! His **"Dog Luck"**? A COSMIC LIE - this is the **God of Tiles** himself, bending probability to his will! Every kansuuri a supernova, every damaten a psychological killshot! The playoff finals became his **Symphony of Domination** - opponents reduced to ash by his **"Seven Pairs From Hell"** and **"Last-Ditch Quadruple Ron Gambit"**!

Bow before DLeague's **Eternal Flame**, the **Two-Time Conqueror** whose reign rewrites reality! His throne isn't built of wood pulp - it's forged from shattered jade dragons and the tears of challengers! **LJL7 ISN'T PLAYING MAHJONG - HE'S WRITING DIVINE COMEDY IN TILES!** All hail the **Undefeated** (except those few times but WHO CARES), the **Unbroken**, the **Living Legend** - the **TILE CRUSADER WHO LAUGHS AT SECOND PLACE!**

### Current Standings

|       |     LJL7 |     0MRS |     5JMY |     PARY |
|-------|----------|----------|----------|----------|
| Pt    |  -118.7  |   159.3  |     2.5  |   -43.1  |
| RawPt |   -89.9  |   143.5  |   -77.5  |    23.9  |
| AP    |     2.56 |     2.5  |     2.48 |     2.46 |
| RR    |    19.55 |    15.53 |    14.66 |    20.24 |
| WR    |    22.16 |    22.34 |    17.28 |    21.12 |
| DIR   |    14.31 |    10.82 |    10.99 |    13.09 |
| RenR  |    52.08 |    41.67 |    54.17 |    52.08 |
| A4R   |    68.75 |    79.17 |    72.92 |    79.17 |
| RWR   |    44.64 |    56.18 |    42.86 |    46.55 |
| RDIR  |    16.96 |     8.99 |     8.33 |    10.34 |
| APW   |  6001    |  6675    |  6801    |  6692    |
| APD   |  5702    |  5635    |  5417    |  5324    |
| 1st   |    11    |    14    |    12    |    11    |
| 2nd   |    14    |     6    |    14    |    14    |
| 3rd   |     8    |    18    |     9    |    13    |
| 4th   |    15    |    10    |    13    |    10    |
| HiScr | 56700    | 72200    | 58200    | 58000    |
| LoScr | -7400    | -5200    | -3300    | -9400    |
