import os
import os.path as osp
import json
import pandas as pd
from tabulate import tabulate

from utils import check_raw_data, int2bin, build_debug_csv, fix_data
from utils import entries_abbr as readme_entries, entries_switch

TG = "data/games.csv"
TR = "data/rounds.csv"
RAW = "raw_data"
README_T = "docs/README_temp.md"
README = "README.md"
STATS_DIR = "statistics"

players = ['LJL7', '0MRS', '5JMY', 'PARY']
players_map = {'wk': 'LJL7', 'gy': '0MRS', 'tb': '5JMY', 'cc': 'PARY'}
bonus_ml = [20000, -20000, -40000, -60000]  # MLeague马点
bonus_skis = [5000, -15000, -35000, -55000] # 最高位战马点
s1_base_pt_1000 = [298100, 81900, -94100, -288900]  # S1前期APP未开发时的初始分
n_regular_games = [0, 49, 50, 35, 50]   # 第0项为占位，此后每项为每个赛季常规赛的场次，常规赛未结束时不用记


def load_readme_template():
    """Load README template from file."""
    with open(README_T, 'r') as f:
        return f.read()


def initialize_season_stats():
    """Initialize statistics dictionaries for a season."""
    total_pt_1000 = {p: 0 for p in players}
    raw_pt_1000 = {p: 0 for p in players}
    acc_rank = {p: 0 for p in players}
    cnt_richi = {p: 0 for p in players}
    cnt_agari = {p: 0 for p in players}
    cnt_hoju = {p: 0 for p in players}
    cnt_1 = {p: 0 for p in players}
    cnt_2 = {p: 0 for p in players}
    cnt_3 = {p: 0 for p in players}
    cnt_4 = {p: 0 for p in players}
    cnt_ra = {p: 0 for p in players}
    cnt_rf = {p: 0 for p in players}
    agari_scr = {p: 0 for p in players}
    hoju_scr = {p: 0 for p in players}
    highest_scr = {p: 0 for p in players}
    lowest_scr = {p: 1000000 for p in players}
    
    return {
        'total_pt_1000': total_pt_1000,
        'raw_pt_1000': raw_pt_1000,
        'acc_rank': acc_rank,
        'cnt_richi': cnt_richi,
        'cnt_agari': cnt_agari,
        'cnt_hoju': cnt_hoju,
        'cnt_1': cnt_1,
        'cnt_2': cnt_2,
        'cnt_3': cnt_3,
        'cnt_4': cnt_4,
        'cnt_ra': cnt_ra,
        'cnt_rf': cnt_rf,
        'agari_scr': agari_scr,
        'hoju_scr': hoju_scr,
        'highest_scr': highest_scr,
        'lowest_scr': lowest_scr,
    }


def get_bonus_for_season(sid):
    """Get bonus points for a given season ID."""
    if sid in [1, 2]:   # 使用MLeague马点的赛季
        return bonus_ml
    elif sid in [3, 4]:  # 使用最高位战马点的赛季
        return bonus_skis
    else:
        raise ValueError(f"Unknown season ID {sid} for bonus points.")


def adjust_bonus_for_ties(sorted_score, bonus):
    """Adjust bonus points for ties in rankings."""
    # 处理同分情况
    if sorted_score[0] == sorted_score[3]:
        return [-25000] * 4
    elif sorted_score[0] == sorted_score[2]:
        return [(bonus[0] + bonus[1] + bonus[2]) // 3] * 3 + [bonus[3]]
    elif sorted_score[1] == sorted_score[3]:
        return [bonus[0]] + [(bonus[1] + bonus[2] + bonus[3]) // 3] * 3
    elif sorted_score[0] == sorted_score[1] and sorted_score[2] == sorted_score[3]:
        return [(bonus[0] + bonus[1]) // 2] * 2 + [(bonus[2] + bonus[3]) // 2] * 2
    elif sorted_score[0] == sorted_score[1]:
        return [(bonus[0] + bonus[1]) // 2] * 2 + bonus[2:]
    elif sorted_score[1] == sorted_score[2]:
        return [bonus[0]] + [(bonus[1] + bonus[2]) // 2] * 2 + [bonus[3]]
    elif sorted_score[2] == sorted_score[3]:
        return bonus[:2] + [(bonus[2] + bonus[3]) // 2] * 2
    return bonus


def process_json_game(file_path, sid, gid, stats, game_data_accumulators, round_data_accumulators):
    """Process a single JSON game file."""
    fix_data(file_path)  # 修正PlayerId
    with open(file_path) as f:
        data = json.load(f)
    
    if sid != 1:  # S1 doesn't need validation
        legal, msg = check_raw_data(data)
        if not legal:
            print(f"Error in S{sid}/G{gid:02d}: {msg}")
            build_debug_csv(f'S{sid}/G{gid:02d}')
            return False
        else:
            if osp.exists(f"debug_S{sid}_G{gid:02d}.csv"):
                os.remove(f"debug_S{sid}_G{gid:02d}.csv")
                print(f"Removed debug_S{sid}_G{gid:02d}.csv.")
    
    p = [data[i]['PlayerId'] for i in range(4)]
    final_score = [data[i]['Score'][-1] for i in range(4)]
    sorted_score = sorted(final_score, reverse=True)
    ranking = [sorted_score.index(s) + 1 for s in final_score]
    
    bonus = get_bonus_for_season(sid)
    bonus = adjust_bonus_for_ties(sorted_score, bonus)
    
    points_1000 = [s + bonus[sorted_score.index(s)] for s in final_score]
    raw_points_1000 = [s - 25000 for s in final_score]
    points = [round(p / 1000, 1) for p in points_1000]
    
    # Accumulate game data
    SID, GID, Date, E, S, W, N = game_data_accumulators['SID'], game_data_accumulators['GID'], game_data_accumulators['Date'], game_data_accumulators['E'], game_data_accumulators['S'], game_data_accumulators['W'], game_data_accumulators['N']
    Scr_E, Scr_S, Scr_W, Scr_N = game_data_accumulators['Scr_E'], game_data_accumulators['Scr_S'], game_data_accumulators['Scr_W'], game_data_accumulators['Scr_N']
    Rk_E, Rk_S, Rk_W, Rk_N = game_data_accumulators['Rk_E'], game_data_accumulators['Rk_S'], game_data_accumulators['Rk_W'], game_data_accumulators['Rk_N']
    Pts_E, Pts_S, Pts_W, Pts_N = game_data_accumulators['Pts_E'], game_data_accumulators['Pts_S'], game_data_accumulators['Pts_W'], game_data_accumulators['Pts_N']
    
    SID.append(data[0]['SID'])
    GID.append(data[0]['GID'])
    Date.append(data[0]['Time'].split('_')[0])
    E.append(p[0])
    S.append(p[1])
    W.append(p[2])
    N.append(p[3])
    Scr_E.append(final_score[0])
    Scr_S.append(final_score[1])
    Scr_W.append(final_score[2])
    Scr_N.append(final_score[3])
    Rk_E.append(ranking[0])
    Rk_S.append(ranking[1])
    Rk_W.append(ranking[2])
    Rk_N.append(ranking[3])
    Pts_E.append(points[0])
    Pts_S.append(points[1])
    Pts_W.append(points[2])
    Pts_N.append(points[3])
    
    # Update statistics
    for i in range(4):
        if gid <= n_regular_games[sid if sid < len(n_regular_games) else 0]:
            stats['total_pt_1000'][p[i]] += points_1000[i] / 2
        else:
            stats['total_pt_1000'][p[i]] += points_1000[i]
        stats['raw_pt_1000'][p[i]] += raw_points_1000[i]
        stats['acc_rank'][p[i]] += ranking[i]
        
        if ranking[i] == 1:
            stats['cnt_1'][p[i]] += 1
        elif ranking[i] == 2:
            stats['cnt_2'][p[i]] += 1
        elif ranking[i] == 3:
            stats['cnt_3'][p[i]] += 1
        elif ranking[i] == 4:
            stats['cnt_4'][p[i]] += 1
        
        if final_score[i] > stats['highest_scr'][p[i]]:
            stats['highest_scr'][p[i]] = final_score[i]
        if final_score[i] < stats['lowest_scr'][p[i]]:
            stats['lowest_scr'][p[i]] = final_score[i]
    
    # Process round data
    score = [data[i]['Score'] for i in range(4)]
    ops = [data[i]['Operations'] for i in range(4)]
    
    SID_r, GID_r, RID, Ryukyo, Richi, Agari, Hoju = round_data_accumulators['SID_r'], round_data_accumulators['GID_r'], round_data_accumulators['RID'], round_data_accumulators['Ryukyo'], round_data_accumulators['Richi'], round_data_accumulators['Agari'], round_data_accumulators['Hoju']
    Var_E, Var_S, Var_W, Var_N = round_data_accumulators['Var_E'], round_data_accumulators['Var_S'], round_data_accumulators['Var_W'], round_data_accumulators['Var_N']
    
    for k in range(1, len(score[0])):
        RID.append(k)
        SID_r.append(data[0]['SID'])
        GID_r.append(data[0]['GID'])
        Ryukyo.append(int2bin(1 if all(['N' in ops[i][k] for i in range(4)]) else 0))
        Richi.append(int2bin(sum([1 << i for i in range(4) if 'R' in ops[i][k]])))
        Agari.append(int2bin(sum([1 << i for i in range(4) if 'A' in ops[i][k]])))
        Hoju.append(int2bin(sum([1 << i for i in range(4) if 'F' in ops[i][k]])))
        Var_E.append(score[0][k] - score[0][k-1])
        Var_S.append(score[1][k] - score[1][k-1])
        Var_W.append(score[2][k] - score[2][k-1])
        Var_N.append(score[3][k] - score[3][k-1])
        
        for i in range(4):
            stats['cnt_richi'][p[i]] += 1 if 'R' in ops[i][k] else 0
            stats['cnt_agari'][p[i]] += 1 if 'A' in ops[i][k] else 0
            stats['cnt_hoju'][p[i]] += 1 if 'F' in ops[i][k] else 0
            stats['cnt_ra'][p[i]] += 1 if 'R' in ops[i][k] and 'A' in ops[i][k] else 0
            stats['cnt_rf'][p[i]] += 1 if 'R' in ops[i][k] and 'F' in ops[i][k] else 0
            if 'A' in ops[i][k]:
                stats['agari_scr'][p[i]] += score[i][k] - score[i][k-1]
            if 'F' in ops[i][k]:
                stats['hoju_scr'][p[i]] += score[i][k-1] - score[i][k]
    
    return True


def process_txt_game(file_path, sid, gid, stats, game_data_accumulators):
    """Process a single TXT game file."""
    data = []
    with open(file_path) as f:
        for line in f:
            data.append(line.strip().split())
    
    p = [players_map[data[i][0]] for i in range(4)]
    final_score = [int(data[i][1]) for i in range(4)]
    sorted_score = sorted(final_score, reverse=True)
    ranking = [sorted_score.index(s) + 1 for s in final_score]
    points_1000 = [s + bonus_ml[sorted_score.index(s)] for s in final_score]
    raw_points_1000 = [s - 25000 for s in final_score]
    points = [round(p / 1000, 1) for p in points_1000]
    
    # Accumulate game data
    SID, GID, Date, E, S, W, N = game_data_accumulators['SID'], game_data_accumulators['GID'], game_data_accumulators['Date'], game_data_accumulators['E'], game_data_accumulators['S'], game_data_accumulators['W'], game_data_accumulators['N']
    Scr_E, Scr_S, Scr_W, Scr_N = game_data_accumulators['Scr_E'], game_data_accumulators['Scr_S'], game_data_accumulators['Scr_W'], game_data_accumulators['Scr_N']
    Rk_E, Rk_S, Rk_W, Rk_N = game_data_accumulators['Rk_E'], game_data_accumulators['Rk_S'], game_data_accumulators['Rk_W'], game_data_accumulators['Rk_N']
    Pts_E, Pts_S, Pts_W, Pts_N = game_data_accumulators['Pts_E'], game_data_accumulators['Pts_S'], game_data_accumulators['Pts_W'], game_data_accumulators['Pts_N']
    
    SID.append(sid)
    GID.append(gid)
    Date.append('Unknown')
    E.append(p[0])
    S.append(p[1])
    W.append(p[2])
    N.append(p[3])
    Scr_E.append(final_score[0])
    Scr_S.append(final_score[1])
    Scr_W.append(final_score[2])
    Scr_N.append(final_score[3])
    Rk_E.append(ranking[0])
    Rk_S.append(ranking[1])
    Rk_W.append(ranking[2])
    Rk_N.append(ranking[3])
    Pts_E.append(points[0])
    Pts_S.append(points[1])
    Pts_W.append(points[2])
    Pts_N.append(points[3])
    
    # Update statistics
    for i in range(4):
        if gid <= n_regular_games[sid if sid < len(n_regular_games) else 0]:
            stats['total_pt_1000'][p[i]] += points_1000[i] / 2
        else:
            stats['total_pt_1000'][p[i]] += points_1000[i]
        stats['raw_pt_1000'][p[i]] += raw_points_1000[i]
        stats['acc_rank'][p[i]] += ranking[i]
        
        if ranking[i] == 1:
            stats['cnt_1'][p[i]] += 1
        elif ranking[i] == 2:
            stats['cnt_2'][p[i]] += 1
        elif ranking[i] == 3:
            stats['cnt_3'][p[i]] += 1
        elif ranking[i] == 4:
            stats['cnt_4'][p[i]] += 1
        
        if final_score[i] > stats['highest_scr'][p[i]]:
            stats['highest_scr'][p[i]] = final_score[i]
        if final_score[i] < stats['lowest_scr'][p[i]]:
            stats['lowest_scr'][p[i]] = final_score[i]
    
    return True


def calculate_season_statistics(stats, cnt_g, cnt_r, sid):
    """Calculate statistics for a season and return DataFrame."""
    statistics = {}
    for i in range(4):
        player = players[i]
        total_pt = stats['total_pt_1000'][player]
        if sid == 1:
            total_pt += s1_base_pt_1000[i] / 2
        
        statistics[player] = [
            round(total_pt / 1000, 1),
            round(stats['raw_pt_1000'][player] / 1000, 1),
            round(stats['acc_rank'][player] / cnt_g, 2),
            round(100 * stats['cnt_richi'][player] / cnt_r, 2) if cnt_r > 0 else 0,
            round(100 * stats['cnt_agari'][player] / cnt_r, 2) if cnt_r > 0 else 0,
            round(100 * stats['cnt_hoju'][player] / cnt_r, 2) if cnt_r > 0 else 0,
            round(100 * (stats['cnt_1'][player] + stats['cnt_2'][player]) / cnt_g, 2) if cnt_g > 0 else 0,
            round(100 * (stats['cnt_1'][player] + stats['cnt_2'][player] + stats['cnt_3'][player]) / cnt_g, 2) if cnt_g > 0 else 0,
            round(100 * stats['cnt_ra'][player] / stats['cnt_richi'][player], 2) if stats['cnt_richi'][player] != 0 else 0,
            round(100 * stats['cnt_rf'][player] / stats['cnt_richi'][player], 2) if stats['cnt_richi'][player] != 0 else 0,
            round(stats['agari_scr'][player] / stats['cnt_agari'][player]) if stats['cnt_agari'][player] != 0 else 0,
            round(stats['hoju_scr'][player] / stats['cnt_hoju'][player]) if stats['cnt_hoju'][player] != 0 else 0,
            stats['cnt_1'][player],
            stats['cnt_2'][player],
            stats['cnt_3'][player],
            stats['cnt_4'][player],
            stats['highest_scr'][player],
            stats['lowest_scr'][player]
        ]
    
    statistics_df = pd.DataFrame(statistics, columns=players, index=readme_entries)
    return statistics_df


def save_season_csv(statistics_df, season_name):
    """Save season statistics to CSV file."""
    statistics_df.to_csv(osp.join(STATS_DIR, f"{season_name}.csv"))


def update_readme_with_season(readme, statistics_df, sid, cnt_g, is_latest_season):
    """Update README with season statistics."""
    statistics_df = statistics_df.loc[entries_switch]
    
    if is_latest_season:
        # Add current season hanchan count information
        readme += f"\n**Data updated to S{sid} G{cnt_g}**\n\n"
        readme += f"{tabulate(statistics_df, headers='keys', tablefmt='github')}\n"
    # Only latest season gets added to README (original behavior)
    
    return readme


def save_games_csv(game_data):
    """Save games data to CSV file."""
    tg = pd.DataFrame({
        'SID': game_data['SID'],
        'GID': game_data['GID'],
        'Date': game_data['Date'],
        'E': game_data['E'],
        'S': game_data['S'],
        'W': game_data['W'],
        'N': game_data['N'],
        'Scr-E': game_data['Scr_E'],
        'Scr-S': game_data['Scr_S'],
        'Scr-W': game_data['Scr_W'],
        'Scr-N': game_data['Scr_N'],
        'Rk-E': game_data['Rk_E'],
        'Rk-S': game_data['Rk_S'],
        'Rk-W': game_data['Rk_W'],
        'Rk-N': game_data['Rk_N'],
        'Pts-E': game_data['Pts_E'],
        'Pts-S': game_data['Pts_S'],
        'Pts-W': game_data['Pts_W'],
        'Pts-N': game_data['Pts_N']
    })
    tg.sort_values(by=['SID', 'GID'], ascending=[False, False], inplace=True)
    tg.to_csv(TG, index=False)


def save_rounds_csv(round_data):
    """Save rounds data to CSV file."""
    tr = pd.DataFrame({
        'SID': round_data['SID_r'],
        'GID': round_data['GID_r'],
        'RID': round_data['RID'],
        'Ryukyo': round_data['Ryukyo'],
        'Richi': round_data['Richi'],
        'Agari': round_data['Agari'],
        'Hoju': round_data['Hoju'],
        'Var-E': round_data['Var_E'],
        'Var-S': round_data['Var_S'],
        'Var-W': round_data['Var_W'],
        'Var-N': round_data['Var_N']
    })
    tr.sort_values(by=['SID', 'GID', 'RID'], ascending=[False, False, False], inplace=True)
    tr.to_csv(TR, index=False)


def process_data():
    """Main data processing function."""
    # Initialize data accumulators
    game_data = {
        'SID': [], 'GID': [], 'Date': [], 'E': [], 'S': [], 'W': [], 'N': [],
        'Scr_E': [], 'Scr_S': [], 'Scr_W': [], 'Scr_N': [],
        'Rk_E': [], 'Rk_S': [], 'Rk_W': [], 'Rk_N': [],
        'Pts_E': [], 'Pts_S': [], 'Pts_W': [], 'Pts_N': []
    }
    
    round_data = {
        'SID_r': [], 'GID_r': [], 'RID': [], 'Ryukyo': [], 'Richi': [], 'Agari': [], 'Hoju': [],
        'Var_E': [], 'Var_S': [], 'Var_W': [], 'Var_N': []
    }
    
    readme = load_readme_template()
    seasons = sorted(os.listdir(RAW), key=lambda x: int(x[1:]), reverse=True)
    
    for season_name in seasons:
        sid = int(season_name[1:])
        stats = initialize_season_stats()
        cnt_g = 0
        cnt_r = 0
        
        games = os.listdir(osp.join(RAW, season_name))
        # Handle duplicate file names
        unique_names = {}
        for f in games:
            b, e = osp.splitext(f)
            if b not in unique_names or e == '.json':
                unique_names[b] = f
            else:
                print(f"Warning: Duplicate file name {f} in {season_name}.")
        games = list(unique_names.values())
        games.sort(key=lambda x: int(osp.splitext(x)[0][1:]))
        
        for game_file in games:
            gid = int(osp.splitext(game_file)[0][1:])
            file_path = osp.join(RAW, season_name, game_file)
            
            if osp.splitext(game_file)[1] == '.json':
                success = process_json_game(file_path, sid, gid, stats, game_data, round_data)
                if not success:
                    continue
                
                # Count rounds from JSON data
                with open(file_path) as f:
                    data = json.load(f)
                cnt_r += len(data[0]['Score']) - 1  # Number of rounds
                cnt_g += 1
                
            elif osp.splitext(game_file)[1] == '.txt':
                success = process_txt_game(file_path, sid, gid, stats, game_data)
                if not success:
                    continue
                cnt_g += 1
                # TXT files don't have round data
            else:
                print(f"Error: Unknown file type in {season_name}/{game_file}")
                continue
        
        # Calculate and save season statistics
        statistics_df = calculate_season_statistics(stats, cnt_g, cnt_r, sid)
        save_season_csv(statistics_df, season_name)
        
        # Update README with this season's data (only latest season gets full table)
        is_latest_season = (sid == len(seasons))
        readme = update_readme_with_season(readme, statistics_df, sid, cnt_g, is_latest_season)
    
    # Save all accumulated data to CSV files
    save_games_csv(game_data)
    save_rounds_csv(round_data)
    
    print("Updated data and statistics.")
    
    # Write final README
    with open(README, 'w') as f:
        f.write(readme)
    print("Updated README.")


if __name__ == '__main__':
    if os.getcwd().split('/')[-1] == 'scripts' or os.getcwd().split('\\')[-1] == 'scripts':
        os.chdir('..')
    process_data()