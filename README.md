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
| Pt    |  -125.7  |   162.1  |   -10.6  |   -25.8  |
| RawPt |   -86.9  |   136.2  |   -80.5  |    31.2  |
| AP    |     2.58 |     2.49 |     2.49 |     2.44 |
| RR    |    19.59 |    15.53 |    14.6  |    20.15 |
| WR    |    22.18 |    22.55 |    16.82 |    20.89 |
| DIR   |    14.6  |    11.09 |    10.54 |    13.31 |
| RenR  |    51.11 |    42.22 |    53.33 |    53.33 |
| A4R   |    68.89 |    80    |    73.33 |    77.78 |
| RWR   |    45.28 |    55.95 |    40.51 |    45.87 |
| RDIR  |    16.98 |     8.33 |     8.86 |    10.09 |
| APW   |  6032    |  6708    |  6721    |  6704    |
| APD   |  5785    |  5725    |  5386    |  5296    |
| 1st   |    10    |    13    |    11    |    11    |
| 2nd   |    13    |     6    |    13    |    13    |
| 3rd   |     8    |    17    |     9    |    11    |
| 4th   |    14    |     9    |    12    |    10    |
| HiScr | 56700    | 72200    | 58200    | 58000    |
| LoScr | -7400    | -5200    | -3300    | -9400    |
