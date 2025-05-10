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
| Pt    |    20.7  |  -130.1  |   -94.9  |   204.3  |
| RawPt |     0.7  |   -30.1  |   -74.9  |   104.3  |
| AP    |     2.46 |     2.69 |     2.54 |     2.31 |
| RR    |    19.81 |    16.88 |    15.91 |    20.45 |
| WR    |    23.7  |    20.78 |    17.21 |    21.43 |
| DIR   |    12.99 |    12.34 |    11.36 |    13.96 |
| RenR  |    57.69 |    30.77 |    50    |    61.54 |
| A4R   |    69.23 |    76.92 |    69.23 |    84.62 |
| RWR   |    52.46 |    53.85 |    40.82 |    53.97 |
| RDIR  |    14.75 |    11.54 |     8.16 |     4.76 |
| APW   |  5730    |  6448    |  6260    |  7183    |
| APD   |  5515    |  6261    |  5777    |  4233    |
| 1st   |     7    |     6    |     7    |     6    |
| 2nd   |     8    |     2    |     6    |    10    |
| 3rd   |     3    |    12    |     5    |     6    |
| 4th   |     8    |     6    |     8    |     4    |
| HiScr | 54600    | 72200    | 58200    | 58000    |
| LoScr | -7400    | -5200    | -3300    | 10200    |
