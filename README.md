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
| Pt    |    55.8  |  -103.9  |   -99.6  |   147.7  |
| RawPt |    15.8  |   -23.9  |   -59.6  |    67.7  |
| AP    |     2.39 |     2.72 |     2.61 |     2.28 |
| RR    |    20.56 |    15.42 |    15.89 |    22.43 |
| WR    |    23.36 |    19.16 |    16.82 |    21.96 |
| DIR   |    12.62 |    12.62 |    10.75 |    14.02 |
| RenR  |    61.11 |    27.78 |    44.44 |    66.67 |
| A4R   |    72.22 |    77.78 |    66.67 |    83.33 |
| RWR   |    56.82 |    51.52 |    41.18 |    56.25 |
| RDIR  |    13.64 |    18.18 |     5.88 |     2.08 |
| APW   |  6208    |  7405    |  6742    |  7040    |
| APD   |  5756    |  6526    |  6683    |  4123    |
| 1st   |     5    |     4    |     5    |     4    |
| 2nd   |     6    |     1    |     3    |     8    |
| 3rd   |     2    |     9    |     4    |     3    |
| 4th   |     5    |     4    |     6    |     3    |
| HiScr | 54600    | 72200    | 58200    | 56500    |
| LoScr | -7400    | -5200    |  -300    | 10200    |
