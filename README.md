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
| Pt    |    54.8  |  -207.1  |  -102.4  |   254.7  |
| RawPt |    14.8  |   -47.1  |   -82.4  |   114.7  |
| AP    |     2.43 |     2.77 |     2.53 |     2.27 |
| RR    |    20.06 |    15.88 |    15.6  |    20.89 |
| WR    |    23.96 |    19.22 |    16.99 |    21.45 |
| DIR   |    13.65 |    11.7  |    10.31 |    13.65 |
| RenR  |    60    |    30    |    46.67 |    63.33 |
| A4R   |    70    |    73.33 |    73.33 |    83.33 |
| RWR   |    48.61 |    50.88 |    41.07 |    53.33 |
| RDIR  |    18.06 |    10.53 |    10.71 |     5.33 |
| APW   |  5936    |  6517    |  6403    |  7330    |
| APD   |  5657    |  6043    |  5968    |  4643    |
| 1st   |     8    |     6    |     8    |     8    |
| 2nd   |    10    |     3    |     6    |    11    |
| 3rd   |     3    |    13    |     8    |     6    |
| 4th   |     9    |     8    |     8    |     5    |
| HiScr | 56700    | 72200    | 58200    | 58000    |
| LoScr | -7400    | -5200    | -3300    |  7500    |
