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
| Pt    |     5.1  |    -7.4  |  -151    |   153.3  |
| RawPt |     5.1  |    -7.4  |   -71    |    73.3  |
| AP    |     2.5  |     2.5  |     3.17 |     1.83 |
| RR    |    20    |    18.46 |    13.85 |    20    |
| WR    |    24.62 |    21.54 |    13.85 |    29.23 |
| DIR   |     9.23 |    13.85 |    16.92 |    10.77 |
| RenR  |    66.67 |    33.33 |    33.33 |    66.67 |
| A4R   |    66.67 |    83.33 |    50    |   100    |
| RWR   |    61.54 |    50    |    33.33 |    76.92 |
| RDIR  |     0    |    25    |    11.11 |     0    |
| APW   |  5588    |  7057    |  6078    |  7258    |
| APD   |  3983    |  6800    |  5145    |  2571    |
| 1st   |     1    |     2    |     0    |     3    |
| 2nd   |     3    |     0    |     2    |     1    |
| 3rd   |     0    |     3    |     1    |     2    |
| 4th   |     2    |     1    |     3    |     0    |
| HiScr | 34900    | 44300    | 28400    | 56500    |
| LoScr | 12900    |  3800    |  -300    | 23200    |
