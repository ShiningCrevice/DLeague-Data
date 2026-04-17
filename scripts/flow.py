import argparse
import json
import os
from dataclasses import dataclass
from typing import Iterable, List, Tuple


ROUND_WIND = ["东", "南", "西", "北"]
DRAW_DETAIL_PRIORITY = {"无人听牌": 0, "听牌": 1, "全员听牌": 2}


@dataclass(frozen=True)
class RoundState:
    hand_index: int
    dealer: int
    honba: int
    kyotaku: int


@dataclass
class Branch:
    state: RoundState
    logs: List[str]
    penalty: int = 0


def get_rule_name(game: str) -> str:
    season = os.path.normpath(game).split(os.sep)[0]
    if season in {"S1", "S2"}:
        return "MLeague马点时期"
    if season in {"S3", "S4"}:
        return "最高位战马点时期"
    return "未知规则"


def parse_game(game: str) -> str:
    game = game.strip()
    if game.endswith(".json"):
        path = game
    else:
        path = os.path.join("raw_data", f"{game}.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Game file not found: {path}")
    return path


def load_game(path: str) -> Tuple[List[str], List[List[int]], List[List[str]]]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    players = [data[i]["PlayerId"] for i in range(4)]
    scores = [data[i]["Score"] for i in range(4)]
    ops = [data[i]["Operations"] for i in range(4)]
    return players, scores, ops


def round_name(hand_index: int) -> str:
    wind = ROUND_WIND[(hand_index // 4) % len(ROUND_WIND)]
    kyoku = hand_index % 4 + 1
    return f"{wind}{kyoku}局"


def fmt_delta(v: int) -> str:
    if v > 0:
        return f"+{v}"
    return str(v)


def format_delta_list(players: List[str], deltas: List[int]) -> str:
    return ", ".join(f"{players[i]} {fmt_delta(deltas[i])}" for i in range(4))


def append_riichi_text(ops_round: List[str], players: List[str]) -> str:
    richiers = [players[i] for i in range(4) if "R" in ops_round[i]]
    if not richiers:
        return ""
    return "，" + "，".join(f"{p}立直" for p in richiers)


def infer_penalty(text: str, ops_round: List[str], used_explicit_hoju: bool) -> int:
    penalty = 0
    if "全员听牌" in text:
        penalty += 3
    if "无人听牌" in text:
        penalty += 2
    return penalty


def infer_draw_candidates(
    deltas: List[int], ops_round: List[str], state: RoundState, players: List[str]
) -> List[Tuple[RoundState, str, int]]:
    adjusted = [d + (1000 if "R" in ops_round[i] else 0) for i, d in enumerate(deltas)]
    candidates: List[Tuple[RoundState, str, int]] = []

    tenpai_patterns = []
    # t = 0 or 4 both imply no noten payment transfer.
    tenpai_patterns.append((set(), [0, 0, 0, 0], "无人听牌"))
    tenpai_patterns.append((set(range(4)), [0, 0, 0, 0], "全员听牌"))

    for tenpai_cnt in (1, 2, 3):
        tenpai_gain = 3000 // tenpai_cnt
        noten_loss = -3000 // (4 - tenpai_cnt)
        for mask in range(1 << 4):
            if mask.bit_count() != tenpai_cnt:
                continue
            tenpai_set = {i for i in range(4) if (mask >> i) & 1}
            vec = [tenpai_gain if i in tenpai_set else noten_loss for i in range(4)]
            tenpai_patterns.append(
                (tenpai_set, vec, "听牌: " + "/".join(players[i] for i in sorted(tenpai_set)))
            )

    seen = set()
    for tenpai_set, vec, detail in tenpai_patterns:
        if adjusted != vec:
            continue
        key = (tuple(sorted(tenpai_set)), tuple(adjusted))
        if key in seen:
            continue
        seen.add(key)

        dealer_tenpai = state.dealer in tenpai_set
        next_state = RoundState(
            hand_index=state.hand_index if dealer_tenpai else state.hand_index + 1,
            dealer=state.dealer if dealer_tenpai else (state.dealer + 1) % 4,
            honba=state.honba + 1,
            kyotaku=state.kyotaku + sum(1 for o in ops_round if "R" in o),
        )
        text = (
            f"{round_name(state.hand_index)}{state.honba}本场，场供{state.kyotaku * 1000}"
            f"{append_riichi_text(ops_round, players)}，流局（{detail}）。"
        )
        candidates.append((next_state, text, infer_penalty(text, ops_round, True)))

    return sorted(
        candidates,
        key=lambda item: (
            DRAW_DETAIL_PRIORITY.get(item[1].split("（", 1)[1].split("）。", 1)[0].split(":")[0], 99),
            item[1],
        ),
    )


def infer_ron_candidates(
    deltas: List[int], ops_round: List[str], state: RoundState, players: List[str]
) -> List[Tuple[RoundState, str, int]]:
    winners = [i for i in range(4) if "A" in ops_round[i]]
    dealins = [i for i in range(4) if "F" in ops_round[i]]
    if not winners or not dealins:
        return []

    r_cnt = sum(1 for o in ops_round if "R" in o)
    sticks = (state.kyotaku + r_cnt) * 1000
    adjusted = [
        deltas[i] + (1000 if "R" in ops_round[i] else 0) - (sticks if i in winners else 0)
        for i in range(4)
    ]

    candidates: List[Tuple[RoundState, str, int]] = []
    candidate_losers = dealins

    for w in winners:
        for l in candidate_losers:
            if l == w:
                continue
            if adjusted[w] <= 0:
                continue
            base = adjusted[w] - 300 * state.honba
            if base <= 0 or base % 100 != 0:
                continue

            ok = True
            for i in range(4):
                expect = 0
                if i == w:
                    expect = base + 300 * state.honba
                elif i == l:
                    expect = -base - 300 * state.honba
                if adjusted[i] != expect:
                    ok = False
                    break
            if not ok:
                continue

            dealer_cont = w == state.dealer
            next_state = RoundState(
                hand_index=state.hand_index if dealer_cont else state.hand_index + 1,
                dealer=state.dealer if dealer_cont else (state.dealer + 1) % 4,
                honba=state.honba + 1 if dealer_cont else 0,
                kyotaku=0,
            )
            text = (
                f"{round_name(state.hand_index)}{state.honba}本场，场供{state.kyotaku * 1000}"
                f"{append_riichi_text(ops_round, players)}，{players[l]}放铳，{players[w]}荣和{base}点。"
                f" 分差: {format_delta_list(players, deltas)}。"
            )
            candidates.append((next_state, text, infer_penalty(text, ops_round, True)))

    return dedup_candidates(candidates)


def infer_tsumo_candidates(
    deltas: List[int], ops_round: List[str], state: RoundState, players: List[str]
) -> List[Tuple[RoundState, str, int]]:
    winners = [i for i in range(4) if "A" in ops_round[i]]
    if len(winners) != 1:
        return []
    w = winners[0]

    r_cnt = sum(1 for o in ops_round if "R" in o)
    sticks = (state.kyotaku + r_cnt) * 1000
    adjusted = [
        deltas[i] + (1000 if "R" in ops_round[i] else 0) - (sticks if i == w else 0)
        for i in range(4)
    ]

    candidates: List[Tuple[RoundState, str, int]] = []
    others = [i for i in range(4) if i != w]
    dealer = state.dealer

    if w == dealer:
        pay = -adjusted[others[0]] - 100 * state.honba
        if pay > 0 and pay % 100 == 0:
            if all(adjusted[i] == -(pay + 100 * state.honba) for i in others):
                if adjusted[w] == 3 * pay + 300 * state.honba:
                    next_state = RoundState(
                        hand_index=state.hand_index,
                        dealer=state.dealer,
                        honba=state.honba + 1,
                        kyotaku=0,
                    )
                    text = (
                        f"{round_name(state.hand_index)}{state.honba}本场，场供{state.kyotaku * 1000}"
                        f"{append_riichi_text(ops_round, players)}，{players[w]}自摸。"
                        f" 三家各支付{pay}点（另含本场每家{100 * state.honba}点）。"
                        f" 分差: {format_delta_list(players, deltas)}。"
                    )
                    candidates.append((next_state, text, infer_penalty(text, ops_round, True)))
    else:
        nondealer_others = [i for i in others if i != dealer]
        pay_nd = -adjusted[nondealer_others[0]] - 100 * state.honba
        pay_d = -adjusted[dealer] - 100 * state.honba
        if pay_nd > 0 and pay_d > 0 and pay_nd % 100 == 0 and pay_d % 100 == 0:
            # Child tsumo payments are rounded independently, so dealer payment
            # is usually either exactly double or double minus 100.
            if pay_d in {2 * pay_nd, 2 * pay_nd - 100}:
                if (
                    adjusted[nondealer_others[0]] == -(pay_nd + 100 * state.honba)
                    and adjusted[nondealer_others[1]] == -(pay_nd + 100 * state.honba)
                    and adjusted[dealer] == -(pay_d + 100 * state.honba)
                    and adjusted[w] == pay_d + 2 * pay_nd + 300 * state.honba
                ):
                    next_state = RoundState(
                        hand_index=state.hand_index + 1,
                        dealer=(state.dealer + 1) % 4,
                        honba=0,
                        kyotaku=0,
                    )
                    text = (
                        f"{round_name(state.hand_index)}{state.honba}本场，场供{state.kyotaku * 1000}"
                        f"{append_riichi_text(ops_round, players)}，{players[w]}自摸。"
                        f" 庄家{players[dealer]}支付{pay_d}点，其他两家各支付{pay_nd}点"
                        f"（另含本场每家{100 * state.honba}点）。"
                        f" 分差: {format_delta_list(players, deltas)}。"
                    )
                    candidates.append((next_state, text, infer_penalty(text, ops_round, True)))

    return dedup_candidates(candidates)


def dedup_candidates(
    cands: Iterable[Tuple[RoundState, str, int]]
) -> List[Tuple[RoundState, str, int]]:
    out: List[Tuple[RoundState, str, int]] = []
    seen = set()
    for st, txt, penalty in cands:
        key = (st, txt, penalty)
        if key in seen:
            continue
        seen.add(key)
        out.append((st, txt, penalty))
    return out


def round_candidates(
    deltas: List[int], ops_round: List[str], state: RoundState, players: List[str]
) -> List[Tuple[RoundState, str, int]]:
    a_cnt = sum(1 for o in ops_round if "A" in o)
    f_cnt = sum(1 for o in ops_round if "F" in o)

    cands: List[Tuple[RoundState, str, int]] = []
    if a_cnt == 0:
        cands.extend(infer_draw_candidates(deltas, ops_round, state, players))
    elif f_cnt > 0:
        cands.extend(infer_ron_candidates(deltas, ops_round, state, players))
    else:
        cands.extend(infer_tsumo_candidates(deltas, ops_round, state, players))
    return dedup_candidates(cands)


def infer_all_flows(players: List[str], scores: List[List[int]], ops: List[List[str]]) -> List[Branch]:
    rounds = len(scores[0]) - 1
    branches = [Branch(state=RoundState(hand_index=0, dealer=0, honba=0, kyotaku=0), logs=[])]

    for k in range(1, rounds + 1):
        next_branches: List[Branch] = []
        deltas = [scores[i][k] - scores[i][k - 1] for i in range(4)]
        ops_round = [ops[i][k] for i in range(4)]
        for br in branches:
            cands = round_candidates(deltas, ops_round, br.state, players)
            for st, txt, penalty in cands:
                next_branches.append(
                    Branch(state=st, logs=br.logs + [txt], penalty=br.penalty + penalty)
                )

        if not next_branches:
            return sort_branches(
                [
                    Branch(
                        state=br.state,
                        logs=br.logs
                        + [f"[第{k}手无法推断] ops={ops_round}, deltas={deltas}, 当前状态={br.state}"],
                        penalty=br.penalty + 1000,
                    )
                    for br in branches
                ]
            )

        # Dedup by state + logs hash to control branch explosion.
        dedup = {}
        for nb in next_branches:
            key = (nb.state, tuple(nb.logs))
            prev = dedup.get(key)
            if prev is None or nb.penalty < prev.penalty:
                dedup[key] = nb
        branches = sort_branches(list(dedup.values()))

    return sort_branches(branches)


def sort_branches(branches: List[Branch]) -> List[Branch]:
    return sorted(
        branches,
        key=lambda br: (
            br.penalty,
            sum("全员听牌" in line for line in br.logs),
            sum("无人听牌" in line for line in br.logs),
            sum("无法推断" in line for line in br.logs),
            tuple(br.logs),
        ),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Infer mahjong log-style flow for one game.")
    parser.add_argument(
        "--game",
        "-g",
        required=True,
        help="Game id like S4/G37, or a JSON path.",
    )
    args = parser.parse_args()

    path = parse_game(args.game)
    players, scores, ops = load_game(path)
    branches = infer_all_flows(players, scores, ops)

    print(f"Game: {args.game}")
    print(f"Rule: {get_rule_name(args.game)}")
    print(f"Players(E,S,W,N): {', '.join(players)}")
    print(f"Possible flow count: {len(branches)}")
    print("-" * 60)
    for idx, br in enumerate(branches, 1):
        print(f"方案 {idx}:")
        for line in br.logs:
            print(line)
        print(
            f"结束状态: {round_name(br.state.hand_index)}，庄家={players[br.state.dealer]}，"
            f"{br.state.honba}本场，场供{br.state.kyotaku * 1000}"
        )
        print("-" * 60)


if __name__ == "__main__":
    main()
