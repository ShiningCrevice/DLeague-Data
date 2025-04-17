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
| Pt    |   190.7  |  -146.4  |  -153.2  |   108.9  |
| RawPt |    80.7  |   -56.4  |   -83.2  |    58.9  |
| AP    |     2.08 |     2.85 |     2.77 |     2.31 |
| RR    |    23.18 |    16.56 |    17.22 |    25.83 |
| WR    |    27.81 |    16.56 |    14.57 |    23.84 |
| DIR   |    11.26 |    13.25 |    12.58 |    13.25 |
| RenR  |    69.23 |    23.08 |    46.15 |    61.54 |
| A4R   |    84.62 |    76.92 |    53.85 |    84.62 |
| RWR   |    60    |    44    |    38.46 |    56.41 |
| RDIR  |    11.43 |    24    |     3.85 |     2.56 |
| APW   |  6500    |  7164    |  6755    |  7053    |
| APD   |  5653    |  6305    |  6016    |  4865    |
| 1st   |     5    |     2    |     3    |     3    |
| 2nd   |     4    |     1    |     3    |     5    |
| 3rd   |     2    |     7    |     1    |     3    |
| 4th   |     2    |     3    |     6    |     2    |
| HiScr | 54600    | 44300    | 48000    | 56500    |
| LoScr | 12900    |  3300    |  -300    | 10200    |
