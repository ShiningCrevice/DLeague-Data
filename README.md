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
| Pt    |   -62.4  |   -31.7  |  -119.9  |   214    |
| RawPt |   -32.4  |    38.3  |   -89.9  |    84    |
| AP    |     2.54 |     2.6  |     2.54 |     2.31 |
| RR    |    20.14 |    15.11 |    15.35 |    19.66 |
| WR    |    22.78 |    21.58 |    17.27 |    21.1  |
| DIR   |    13.91 |    11.03 |    10.31 |    13.19 |
| RenR  |    54.29 |    37.14 |    48.57 |    60    |
| A4R   |    68.57 |    77.14 |    71.43 |    82.86 |
| RWR   |    46.43 |    52.38 |    39.06 |    53.66 |
| RDIR  |    16.67 |     9.52 |    10.94 |     6.1  |
| APW   |  6035    |  6613    |  6562    |  7047    |
| APD   |  5705    |  6067    |  5826    |  4687    |
| 1st   |     8    |     9    |     9    |     9    |
| 2nd   |    11    |     4    |     8    |    12    |
| 3rd   |     5    |    14    |     8    |     8    |
| 4th   |    11    |     8    |    10    |     6    |
| HiScr | 56700    | 72200    | 58200    | 58000    |
| LoScr | -7400    | -5200    | -3300    |  7200    |
