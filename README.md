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
| Pt    |    -9.4  |    78.7  |   -67.2  |    -2.1  |
| RawPt |   -40.6  |   102.8  |  -107.1  |    44.9  |
| AP    |     2.5  |     2.55 |     2.52 |     2.43 |
| RR    |    20.12 |    15.54 |    14.74 |    19.32 |
| WR    |    23.11 |    22.31 |    16.53 |    20.32 |
| DIR   |    13.75 |    10.56 |    10.76 |    12.95 |
| RenR  |    54.76 |    38.1  |    52.38 |    54.76 |
| A4R   |    71.43 |    78.57 |    71.43 |    78.57 |
| RWR   |    45.54 |    52.56 |    40.54 |    51.55 |
| RDIR  |    17.82 |     8.97 |     9.46 |     6.19 |
| APW   |  6030    |  6688    |  6722    |  6937    |
| APD   |  5886    |  5975    |  5322    |  5063    |
| 1st   |    10    |    12    |    10    |    10    |
| 2nd   |    13    |     4    |    12    |    13    |
| 3rd   |     7    |    17    |     8    |    10    |
| 4th   |    12    |     9    |    12    |     9    |
| HiScr | 56700    | 72200    | 58200    | 58000    |
| LoScr | -7400    | -5200    | -3300    |  2100    |
