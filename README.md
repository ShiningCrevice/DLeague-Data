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
| Pt    |     3.3  |    82.2  |  -159.7  |    74.2  |
| RawPt |   -27.9  |    86.3  |  -139.6  |    81.2  |
| AP    |     2.5  |     2.53 |     2.61 |     2.37 |
| RR    |    20.26 |    15.64 |    14.54 |    19.82 |
| WR    |    23.79 |    22.03 |    16.3  |    20.7  |
| DIR   |    14.1  |    10.79 |    10.35 |    12.56 |
| RenR  |    55.26 |    39.47 |    47.37 |    57.89 |
| A4R   |    71.05 |    78.95 |    68.42 |    81.58 |
| RWR   |    46.74 |    54.93 |    37.88 |    53.33 |
| RDIR  |    18.48 |     8.45 |    10.61 |     5.56 |
| APW   |  6059    |  6747    |  6515    |  7106    |
| APD   |  6025    |  5867    |  5613    |  4879    |
| 1st   |     9    |    11    |     9    |     9    |
| 2nd   |    12    |     4    |     9    |    13    |
| 3rd   |     6    |    15    |     8    |     9    |
| 4th   |    11    |     8    |    12    |     7    |
| HiScr | 56700    | 72200    | 58200    | 58000    |
| LoScr | -7400    | -5200    | -3300    |  7200    |
