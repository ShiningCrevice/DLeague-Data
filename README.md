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
| Pt    |   146.2  |  -131.2  |  -159.8  |   144.8  |
| RawPt |    66.2  |   -51.2  |   -79.8  |    64.8  |
| AP    |     2.17 |     2.83 |     2.83 |     2.17 |
| RR    |    22.54 |    16.9  |    15.49 |    26.76 |
| WR    |    26.06 |    16.9  |    14.79 |    25.35 |
| DIR   |    10.56 |    12.68 |    12.68 |    14.08 |
| RenR  |    66.67 |    25    |    41.67 |    66.67 |
| A4R   |    83.33 |    75    |    50    |    91.67 |
| RWR   |    59.38 |    41.67 |    40.91 |    57.89 |
| RDIR  |     9.38 |    25    |     4.55 |     2.63 |
| APW   |  6432    |  6962    |  6648    |  7053    |
| APD   |  5007    |  6367    |  5683    |  4865    |
| 1st   |     4    |     2    |     3    |     3    |
| 2nd   |     4    |     1    |     2    |     5    |
| 3rd   |     2    |     6    |     1    |     3    |
| 4th   |     2    |     3    |     6    |     1    |
| HiScr | 54600    | 44300    | 48000    | 56500    |
| LoScr | 12900    |  3300    |  -300    | 10200    |
