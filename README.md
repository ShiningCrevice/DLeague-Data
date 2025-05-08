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
| Pt    |    40.5  |  -120.1  |   -31    |   110.6  |
| RawPt |    10.5  |   -30.1  |   -41    |    60.6  |
| AP    |     2.43 |     2.7  |     2.48 |     2.39 |
| RR    |    21.27 |    16.04 |    15.67 |    21.64 |
| WR    |    23.88 |    20.52 |    17.16 |    20.52 |
| DIR   |    13.81 |    12.31 |    11.19 |    13.81 |
| RenR  |    60.87 |    30.43 |    52.17 |    56.52 |
| A4R   |    69.57 |    73.91 |    73.91 |    82.61 |
| RWR   |    54.39 |    58.14 |    42.86 |    53.45 |
| RDIR  |    14.04 |    13.95 |     7.14 |     5.17 |
| APW   |  5781    |  6604    |  6680    |  6998    |
| APD   |  5384    |  6467    |  6100    |  4286    |
| 1st   |     6    |     6    |     6    |     5    |
| 2nd   |     8    |     1    |     6    |     8    |
| 3rd   |     2    |    10    |     5    |     6    |
| 4th   |     7    |     6    |     6    |     4    |
| HiScr | 54600    | 72200    | 58200    | 56500    |
| LoScr | -7400    | -5200    |  -300    | 10200    |
