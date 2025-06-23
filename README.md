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
| Pt    |    17.8  |    74.3  |  -113.5  |    21.3  |
| RawPt |   -23.4  |    88.5  |  -123.4  |    58.3  |
| AP    |     2.49 |     2.54 |     2.56 |     2.41 |
| RR    |    19.78 |    16.34 |    14.62 |    19.57 |
| WR    |    23.66 |    21.94 |    16.56 |    20.22 |
| DIR   |    13.98 |    10.75 |    10.32 |    12.69 |
| RenR  |    56.41 |    38.46 |    48.72 |    56.41 |
| A4R   |    71.79 |    79.49 |    69.23 |    79.49 |
| RWR   |    46.74 |    52.63 |    39.71 |    52.75 |
| RDIR  |    18.48 |     7.89 |    10.29 |     5.49 |
| APW   |  6085    |  6734    |  6587    |  7106    |
| APD   |  5977    |  5910    |  5669    |  5068    |
| 1st   |     9    |    11    |    10    |     9    |
| 2nd   |    13    |     4    |     9    |    13    |
| 3rd   |     6    |    16    |     8    |     9    |
| 4th   |    11    |     8    |    12    |     8    |
| HiScr | 56700    | 72200    | 58200    | 58000    |
| LoScr | -7400    | -5200    | -3300    |  2100    |
