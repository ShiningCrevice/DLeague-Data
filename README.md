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
| Pt    |    44.9  |   -99.9  |   -59.6  |   114.6  |
| RawPt |    24.9  |   -39.9  |   -39.6  |    54.6  |
| AP    |     2.4  |     2.8  |     2.6  |     2.2  |
| RR    |    20.87 |    18.26 |    16.52 |    25.22 |
| WR    |    25.22 |    18.26 |    17.39 |    24.35 |
| DIR   |    11.3  |    13.91 |    13.04 |    13.04 |
| RenR  |    60    |    30    |    50    |    60    |
| A4R   |    80    |    70    |    60    |    90    |
| RWR   |    54.17 |    42.86 |    42.11 |    58.62 |
| RDIR  |     8.33 |    28.57 |     5.26 |     3.45 |
| APW   |  5945    |  6905    |  6850    |  7204    |
| APD   |  4885    |  6600    |  5620    |  4607    |
| 1st   |     2    |     2    |     3    |     3    |
| 2nd   |     4    |     1    |     2    |     3    |
| 3rd   |     2    |     4    |     1    |     3    |
| 4th   |     2    |     3    |     4    |     1    |
| HiScr | 54600    | 44300    | 48000    | 56500    |
| LoScr | 12900    |  3800    |  -300    | 10200    |
