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
| Pt    |   -16    |     5.5  |   -98    |   108.5  |
| RawPt |    -6    |    -4.5  |   -48    |    58.5  |
| AP    |     2.57 |     2.43 |     2.86 |     2.14 |
| RR    |    20.51 |    17.95 |    14.1  |    23.08 |
| WR    |    23.08 |    23.08 |    15.38 |    26.92 |
| DIR   |    11.54 |    14.1  |    15.38 |    11.54 |
| RenR  |    57.14 |    42.86 |    42.86 |    57.14 |
| A4R   |    71.43 |    85.71 |    57.14 |    85.71 |
| RWR   |    56.25 |    50    |    36.36 |    66.67 |
| RDIR  |     0    |    28.57 |     9.09 |     0    |
| APW   |  5789    |  6883    |  7483    |  6986    |
| APD   |  4544    |  6645    |  5175    |  3811    |
| 1st   |     1    |     2    |     1    |     3    |
| 2nd   |     3    |     1    |     2    |     1    |
| 3rd   |     1    |     3    |     1    |     2    |
| 4th   |     2    |     1    |     3    |     1    |
| HiScr | 34900    | 44300    | 48000    | 56500    |
| LoScr | 12900    |  3800    |  -300    | 10200    |
