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
| Pt    |   -19    |    35    |   -41.8  |    25.8  |
| RawPt |     1    |    15    |   -21.8  |     5.8  |
| AP    |     3    |     2    |     3    |     2    |
| RR    |    27.27 |    18.18 |    18.18 |    27.27 |
| WR    |    31.82 |    27.27 |     9.09 |    27.27 |
| DIR   |    18.18 |     9.09 |     4.55 |    22.73 |
| RenR  |    50    |    50    |    50    |    50    |
| A4R   |    50    |   100    |    50    |   100    |
| RWR   |    83.33 |    50    |    25    |    83.33 |
| RDIR  |     0    |    25    |     0    |     0    |
| APW   |  5686    |  7733    |  5500    |  6583    |
| APD   |  4600    |  8950    |  2000    |  2740    |
| 1st   |     0    |     1    |     0    |     1    |
| 2nd   |     1    |     0    |     1    |     0    |
| 3rd   |     0    |     1    |     0    |     1    |
| 4th   |     1    |     0    |     1    |     0    |
| HiScr | 31800    | 44300    | 27500    | 32600    |
| LoScr | 19200    | 20700    |   700    | 23200    |
