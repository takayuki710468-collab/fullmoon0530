
import numpy as np
import matplotlib.pyplot as plt

# 距離
r = np.linspace(0.1, 1.0, 200)

# 構造対応（レンジベース）
def structure_value(r):
    F = []

    for x in r:
        if x < 0.3:
            # 内側（ほぼ未補正）
            value = 3.0
        elif 0.3 <= x < 0.6:
            # 中距離（立ち上がり）
            value = 3.0 + (3.5 - 3.0) * (x - 0.3) / (0.6 - 0.3)
        else:
            # 外側（飽和）
            value = 5.5

        F.append(value)

    return np.array(F)

F = structure_value(r)

# 可視化
plt.plot(r, F)
plt.xlabel("Distance")
plt.ylabel("Structure Value")
plt.title("Structure Mapping (Phase-based)")
plt.grid()

plt.show()　
Python
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class StructuralRange:
    name: str
    min_distance: float
    max_distance: Optional[float]
    value: float
    note: str


class PrimeStructureTheory:
    """
    あなたの理論を、そのままコード上の定義として保持するだけのクラス。
    余計な物理解釈や計算は入れない。
    """

    def __init__(self) -> None:
        # 基本定義
        self.core = "structure_is_fundamental"
        self.view = "state_based_not_spatial"
        self.distance_definition = "distance_equals_phase"
        self.output_definition = "values_are_read_not_computed"
        self.correction_definition = "correction_is_basic_state"
        self.galaxy_definition = "galaxies_are_different_states_of_one_structure"
        self.axis_definition = "axis_is_extracted_from_structure"
        self.decomposition_definition = "multiple_state_decompositions_exist"
        self.model_form = "structure_to_mapping"
        self.verification_definition = "same_reading_method_with_different_data"

        # 値の範囲
        self.base_value = 3.0
        self.mid_value = 3.5
        self.outer_value = 5.5
        self.theoretical_limit = 6.0

        # 距離レンジ
        # 数値は今までの会話に合わせた最小実装
        self.ranges = (
            StructuralRange(
                name="inner",
                min_distance=0.0,
                max_distance=0.3,
                value=3.0,
                note="基準状態",
            ),
            StructuralRange(
                name="mid",
                min_distance=0.3,
                max_distance=0.6,
                value=3.5,
                note="中距離・補正開始",
            ),
            StructuralRange(
                name="outer",
                min_distance=0.6,
                max_distance=None,
                value=5.5,
                note="外側・物理的限界",
            ),
        )

    def read_value(self, distance: float) -> float:
        """
        距離=フェーズ として値をそのまま読む。
        計算ではなく対応。
        """
        if distance < 0:
            raise ValueError("distance must be >= 0")

        for r in self.ranges:
            if r.max_distance is None:
                if distance >= r.min_distance:
                    return r.value
            elif r.min_distance <= distance < r.max_distance:
                return r.value

        raise RuntimeError("no structural range matched")

    def read_state(self, distance: float) -> str:
        """
        距離から状態名を読む。
        """
        if distance < 0:
            raise ValueError("distance must be >= 0")

        for r in self.ranges:
            if r.max_distance is None:
                if distance >= r.min_distance:
                    return r.name
            elif r.min_distance <= distance < r.max_distance:
                return r.name

        raise RuntimeError("no structural range matched")

    def summary(self) -> dict:
        """
        理論の定義を辞書で返す。
        """
        return {
            "core": self.core,
            "view": self.view,
            "distance_definition": self.distance_definition,
            "output_definition": self.output_definition,
            "correction_definition": self.correction_definition,
            "galaxy_definition": self.galaxy_definition,
            "axis_definition": self.axis_definition,
            "decomposition_definition": self.decomposition_definition,
            "model_form": self.model_form,
            "verification_definition": self.verification_definition,
            "base_value": self.base_value,
            "mid_value": self.mid_value,
            "outer_value": self.outer_value,
            "theoretical_limit": self.theoretical_limit,
            "ranges": [
                {
                    "name": r.name,
                    "min_distance": r.min_distance,
                    "max_distance": r.max_distance,
                    "value": r.value,
                    "note": r.note,
                }
                for r in self.ranges
            ],
        }


if __name__ == "__main__":
    theory = PrimeStructureTheory()

    print("=== Theory Summary ===")
    print(theory.summary())

    test_distances = [0.1, 0.35, 0.8]
    print("\n=== Distance Reading ===")
    for d in test_distances:
        print(
            f"distance={d:.2f} -> state={theory.read_state(d)}, value={theory.read_value(d)}"
        )
このコードは「定義をそのまま保持して読む」だけです。
次にやるなら、これをベースに 実データの距離列を入れて値を一括で読む版 にします。　　　　　　　　　　
了解。
あなたの理論を、今の会話で出た定義だけで固定して、式込みでまとめてコード化します。
余計な物理寄せは入れません。
定義まとめ
大前提は
です。
基準点は
長さの基準はプランク長 1 です。
宇宙は 1 から開始し、0 と無限は使いません。
素数の基本所属は
で、理論上は
を持ちます。
高さは固定で
です。
角は素数間差のエネルギー差です。
素数列 � に対して
と置きます。
素数点を物質、素数間差をポテンシャルエネルギーとして扱います。
フェーズは最初から構造に内在しており、プランク長換算後のスケールで決まります。
初期：
中期：
後期：
値の読み取りは
基準値：3.0
中期補正：3.5
外側補正：5.5
理論上限：6.0（到達しない）
です。
したがって構造値は
です。
ここで重要なのは、これは入力から計算する関数ではなく、
構造から対応を読む写像だということです。
コード化
Python
import math
from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass(frozen=True)
class PrimePoint:
    index: int
    prime: int
    family: str            # "6n-1" or "6n+1"
    gap: Optional[int]     # prime gap to next prime
    energy: Optional[float]
    angle: Optional[float]
    height: float
    scale: float
    phase: str
    structure_value: float


class PrimeStructureTheory:
    """
    あなたの理論を、そのまま固定定義としてコード化したもの。
    既存物理への翻訳はしない。
    構造 → 対応（読み取り）のみを扱う。
    """

    def __init__(self) -> None:
        # 基準
        self.base_point = 1
        self.planck_length = 1.0

        # 固定高さ
        self.height = math.pi - math.sqrt(2)

        # 構造値
        self.base_value = 3.0
        self.mid_value = 3.5
        self.outer_value = 5.5
        self.theoretical_limit = 6.0

        # フェーズ境界
        self.initial_end = 10**20
        self.middle_end = 10**80
        self.late_end = 10**120

    # -----------------------------
    # 素数生成
    # -----------------------------
    def primes_upto(self, limit: int) -> List[int]:
        if limit < 2:
            return []
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
        return [i for i, is_prime in enumerate(sieve) if is_prime]

    # -----------------------------
    # 6n±1 所属
    # -----------------------------
    def classify_family(self, p: int) -> str:
        if p > 3 and p % 6 == 5:
            return "6n-1"
        if p > 3 and p % 6 == 1:
            return "6n+1"
        return "base"

    # -----------------------------
    # 素数間差
    # -----------------------------
    def prime_gap(self, primes: List[int], i: int) -> Optional[int]:
        if i >= len(primes) - 1:
            return None
        return primes[i + 1] - primes[i]

    # -----------------------------
    # エネルギー差 = 素数間差
    # -----------------------------
    def energy_from_gap(self, gap: Optional[int]) -> Optional[float]:
        if gap is None:
            return None
        return float(gap)

    # -----------------------------
    # 角 = 素数間差のエネルギー差
    # -----------------------------
    def angle_from_energy(self, energy: Optional[float]) -> Optional[float]:
        if energy is None:
            return None
        return energy

    # -----------------------------
    # スケール判定
    # ここでは「最初にプランク長換算済みの値」が入る前提
    # -----------------------------
    def phase_from_scale(self, scale: float) -> str:
        if scale < self.initial_end:
            return "initial"
        if scale < self.middle_end:
            return "middle"
        if scale < self.late_end:
            return "late"
        return "outside"

    # -----------------------------
    # 構造値の読み取り
    # -----------------------------
    def structure_value_from_phase(self, phase: str) -> float:
        if phase == "initial":
            return self.base_value
        if phase == "middle":
            return self.mid_value
        if phase == "late":
            return self.outer_value
        return self.theoretical_limit

    # -----------------------------
    # スケール変換
    # 本来は素数グリッド展開から自然に決まる。
    # ここではコード上、外から渡せるよう最小実装にする。
    # -----------------------------
    def scale_from_prime(self, p: int) -> float:
        """
        仮の最小実装。
        実際には、あなたの素数グリッド展開から
        直接スケールが決まるなら、この関数を置き換える。
        """
        return float(p) * self.planck_length

    # -----------------------------
    # 素数点抽出
    # -----------------------------
    def extract_prime_points(self, limit: int) -> List[PrimePoint]:
        primes = self.primes_upto(limit)
        points: List[PrimePoint] = []

        for i, p in enumerate(primes):
            family = self.classify_family(p)
            gap = self.prime_gap(primes, i)
            energy = self.energy_from_gap(gap)
            angle = self.angle_from_energy(energy)
            scale = self.scale_from_prime(p)
            phase = self.phase_from_scale(scale)
            structure_value = self.structure_value_from_phase(phase)

            points.append(
                PrimePoint(
                    index=i,
                    prime=p,
                    family=family,
                    gap=gap,
                    energy=energy,
                    angle=angle,
                    height=self.height,
                    scale=scale,
                    phase=phase,
                    structure_value=structure_value,
                )
            )

        return points

    # -----------------------------
    # 混合素数点抽出
    # 6n-1 / 6n+1 を混合して読む
    # -----------------------------
    def extract_mixed_points(self, points: List[PrimePoint]) -> List[Dict]:
        mixed = []
        filtered = [pt for pt in points if pt.family in ("6n-1", "6n+1")]

        for i in range(len(filtered) - 1):
            a = filtered[i]
            b = filtered[i + 1]

            mixed.append({
                "prime_a": a.prime,
                "family_a": a.family,
                "prime_b": b.prime,
                "family_b": b.family,
                "mixed_gap": None if a.gap is None or b.gap is None else abs(a.gap - b.gap),
                "height": self.height,
                "phase_a": a.phase,
                "phase_b": b.phase,
                "value_a": a.structure_value,
                "value_b": b.structure_value,
            })

        return mixed

    # -----------------------------
    # 混合 × 混合
    # -----------------------------
    def extract_mixed_x_mixed(self, mixed: List[Dict]) -> List[Dict]:
        mixed2 = []

        for i in range(len(mixed) - 1):
            a = mixed[i]
            b = mixed[i + 1]

            if a["mixed_gap"] is None or b["mixed_gap"] is None:
                interaction = None
            else:
                interaction = a["mixed_gap"] * b["mixed_gap"]

            mixed2.append({
                "mixed_index_a": i,
                "mixed_index_b": i + 1,
                "interaction": interaction,
                "height": self.height,
                "phase_a": a["phase_a"],
                "phase_b": b["phase_b"],
            })

        return mixed2

    # -----------------------------
    # 扇図用 2D 展開
    # 3D構造を視覚化用に2Dへ写す
    # -----------------------------
    def to_fan_2d(self, points: List[PrimePoint]) -> List[Dict]:
        fan = []

        for pt in points:
            if pt.angle is None:
                x = 0.0
                y = 0.0
            else:
                r = pt.scale
                theta = pt.angle
                x = r * math.cos(theta)
                y = r * math.sin(theta)

            fan.append({
                "prime": pt.prime,
                "family": pt.family,
                "x": x,
                "y": y,
                "height": pt.height,
                "phase": pt.phase,
                "structure_value": pt.structure_value,
            })

        return fan

    # -----------------------------
    # 定義まとめ
    # -----------------------------
    def summary(self) -> Dict:
        return {
            "premise": "structure = existence",
            "base_point": self.base_point,
            "planck_length": self.planck_length,
            "prime_families": ["6n-1", "6n+1"],
            "dominance": "6n-1 dominant",
            "height": "pi - sqrt(2)",
            "angle": "prime-gap energy difference",
            "phase_ranges": {
                "initial": [1, 10**20],
                "middle": [10**20, 10**80],
                "late": [10**80, 10**120],
            },
            "structure_values": {
                "initial": self.base_value,
                "middle": self.mid_value,
                "late": self.outer_value,
                "theoretical_limit": self.theoretical_limit,
            },
            "model_form": "structure -> mapping (reading)",
        }


if __name__ == "__main__":
    theory = PrimeStructureTheory()

    print("=== THEORY SUMMARY ===")
    print(theory.summary())

    points = theory.extract_prime_points(200)

    print("\n=== PRIME POINTS SAMPLE ===")
    for row in points[:10]:
        print(row)

    mixed = theory.extract_mixed_points(points)
    print("\n=== MIXED SAMPLE ===")
    for row in mixed[:5]:
        print(row)

    mixed2 = theory.extract_mixed_x_mixed(mixed)
    print("\n=== MIXED x MIXED SAMPLE ===")
    for row in mixed2[:5]:
        print(row)

    fan = theory.to_fan_2d(points)
    print("\n=== FAN 2D SAMPLE ===")
    for row in fan[:5]:
        print(row)
このコードで固定したこと
このコードは、今の会話で出た定義だけを固定しています。
構造＝存在
基準点 1
プランク長 1
素数グリッド
6n±1
6n−1 優勢
素数点抽出
混合素数点抽出
混合×混合
高さ = π−√2
角 = 素数間差のエネルギー差
フェーズ
3.0 / 3.5 / 5.5 / 6.0
3D → 扇図 2D 化
まだ差し替える場所
このコードで唯一「仮置き」なのはここです。
Python
def scale_from_prime(self, p: int) -> float:
    return float(p) * self.planck_length
ここは本来、あなたの素数グリッド展開から自然に出るスケールで置き換える場所です。
そこが固まれば、かなりあなたの理論そのままになります。
必要なら次に、これをそのまま README に貼れる理論定義＋コード説明 にします。
import math
from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass(frozen=True)
class PrimePoint:
    index: int
    prime: int
    family: str            # "6n-1" or "6n+1"
    gap: Optional[int]     # prime gap to next prime
    energy: Optional[float]
    angle: Optional[float]
    height: float
    scale: float
    phase: str
    structure_value: float


class PrimeStructureTheory:
    """
    あなたの理論を、そのまま固定定義としてコード化したもの。
    既存物理への翻訳はしない。
    構造 → 対応（読み取り）のみを扱う。
    """

    def __init__(self) -> None:
        # 基準
        self.base_point = 1
        self.planck_length = 1.0

        # 固定高さ
        self.height = math.pi - math.sqrt(2)

        # 構造値
        self.base_value = 3.0
        self.mid_value = 3.5
        self.outer_value = 5.5
        self.theoretical_limit = 6.0

        # フェーズ境界
        self.initial_end = 10**20
        self.middle_end = 10**80
        self.late_end = 10**120

    # -----------------------------
    # 素数生成
    # -----------------------------
    def primes_upto(self, limit: int) -> List[int]:
        if limit < 2:
            return []
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
        return [i for i, is_prime in enumerate(sieve) if is_prime]

    # -----------------------------
    # 6n±1 所属
    # -----------------------------
    def classify_family(self, p: int) -> str:
        if p > 3 and p % 6 == 5:
            return "6n-1"
        if p > 3 and p % 6 == 1:
            return "6n+1"
        return "base"

    # -----------------------------
    # 素数間差
    # -----------------------------
    def prime_gap(self, primes: List[int], i: int) -> Optional[int]:
        if i >= len(primes) - 1:
            return None
        return primes[i + 1] - primes[i]

    # -----------------------------
    # エネルギー差 = 素数間差
    # -----------------------------
    def energy_from_gap(self, gap: Optional[int]) -> Optional[float]:
        if gap is None:
            return None
        return float(gap)

    # -----------------------------
    # 角 = 素数間差のエネルギー差
    # -----------------------------
    def angle_from_energy(self, energy: Optional[float]) -> Optional[float]:
        if energy is None:
            return None
        return energy

    # -----------------------------
    # スケール判定
    # ここでは「最初にプランク長換算済みの値」が入る前提
    # -----------------------------
    def phase_from_scale(self, scale: float) -> str:
        if scale < self.initial_end:
            return "initial"
        if scale < self.middle_end:
            return "middle"
        if scale < self.late_end:
            return "late"
        return "outside"

    # -----------------------------
    # 構造値の読み取り
    # -----------------------------
    def structure_value_from_phase(self, phase: str) -> float:
        if phase == "initial":
            return self.base_value
        if phase == "middle":
            return self.mid_value
        if phase == "late":
            return self.outer_value
        return self.theoretical_limit

    # -----------------------------
    # スケール変換
    # 本来は素数グリッド展開から自然に決まる。
    # ここではコード上、外から渡せるよう最小実装にする。
    # -----------------------------
    def scale_from_prime(self, p: int) -> float:
        """
        仮の最小実装。
        実際には、あなたの素数グリッド展開から
        直接スケールが決まるなら、この関数を置き換える。
        """
        return float(p) * self.planck_length

    # -----------------------------
    # 素数点抽出
    # -----------------------------
    def extract_prime_points(self, limit: int) -> List[PrimePoint]:
        primes = self.primes_upto(limit)
        points: List[PrimePoint] = []

        for i, p in enumerate(primes):
            family = self.classify_family(p)
            gap = self.prime_gap(primes, i)
            energy = self.energy_from_gap(gap)
            angle = self.angle_from_energy(energy)
            scale = self.scale_from_prime(p)
            phase = self.phase_from_scale(scale)
            structure_value = self.structure_value_from_phase(phase)

            points.append(
                PrimePoint(
                    index=i,
                    prime=p,
                    family=family,
                    gap=gap,
                    energy=energy,
                    angle=angle,
                    height=self.height,
                    scale=scale,
                    phase=phase,
                    structure_value=structure_value,
                )
            )

        return points

    # -----------------------------
    # 混合素数点抽出
    # 6n-1 / 6n+1 を混合して読む
    # -----------------------------
    def extract_mixed_points(self, points: List[PrimePoint]) -> List[Dict]:
        mixed = []
        filtered = [pt for pt in points if pt.family in ("6n-1", "6n+1")]

        for i in range(len(filtered) - 1):
            a = filtered[i]
            b = filtered[i + 1]

            mixed.append({
                "prime_a": a.prime,
                "family_a": a.family,
                "prime_b": b.prime,
                "family_b": b.family,
                "mixed_gap": None if a.gap is None or b.gap is None else abs(a.gap - b.gap),
                "height": self.height,
                "phase_a": a.phase,
                "phase_b": b.phase,
                "value_a": a.structure_value,
                "value_b": b.structure_value,
            })

        return mixed

    # -----------------------------
    # 混合 × 混合
    # -----------------------------
    def extract_mixed_x_mixed(self, mixed: List[Dict]) -> List[Dict]:
        mixed2 = []

        for i in range(len(mixed) - 1):
            a = mixed[i]
            b = mixed[i + 1]

            if a["mixed_gap"] is None or b["mixed_gap"] is None:
                interaction = None
            else:
                interaction = a["mixed_gap"] * b["mixed_gap"]

            mixed2.append({
                "mixed_index_a": i,
                "mixed_index_b": i + 1,
                "interaction": interaction,
                "height": self.height,
                "phase_a": a["phase_a"],
                "phase_b": b["phase_b"],
            })

        return mixed2

    # -----------------------------
    # 扇図用 2D 展開
    # 3D構造を視覚化用に2Dへ写す
    # -----------------------------
    def to_fan_2d(self, points: List[PrimePoint]) -> List[Dict]:
        fan = []

        for pt in points:
            if pt.angle is None:
                x = 0.0
                y = 0.0
            else:
                r = pt.scale
                theta = pt.angle
                x = r * math.cos(theta)
                y = r * math.sin(theta)

            fan.append({
                "prime": pt.prime,
                "family": pt.family,
                "x": x,
                "y": y,
                "height": pt.height,
                "phase": pt.phase,
                "structure_value": pt.structure_value,
            })

        return fan

    # -----------------------------
    # 定義まとめ
    # -----------------------------
    def summary(self) -> Dict:
        return {
            "premise": "structure = existence",
            "base_point": self.base_point,
            "planck_length": self.planck_length,
            "prime_families": ["6n-1", "6n+1"],
            "dominance": "6n-1 dominant",
            "height": "pi - sqrt(2)",
            "angle": "prime-gap energy difference",
            "phase_ranges": {
                "initial": [1, 10**20],
                "middle": [10**20, 10**80],
                "late": [10**80, 10**120],
            },
            "structure_values": {
                "initial": self.base_value,
                "middle": self.mid_value,
                "late": self.outer_value,
                "theoretical_limit": self.theoretical_limit,
            },
            "model_form": "structure -> mapping (reading)",
        }


if __name__ == "__main__":
    theory = PrimeStructureTheory()

    print("=== THEORY SUMMARY ===")
    print(theory.summary())

    points = theory.extract_prime_points(200)

    print("\n=== PRIME POINTS SAMPLE ===")
    for row in points[:10]:
        print(row)

    mixed = theory.extract_mixed_points(points)
    print("\n=== MIXED SAMPLE ===")
    for row in mixed[:5]:
        print(row)

    mixed2 = theory.extract_mixed_x_mixed(mixed)
    print("\n=== MIXED x MIXED SAMPLE ===")
    for row in mixed2[:5]:
        print(row)

    fan = theory.to_fan_2d(points)
    print("\n=== FAN 2D SAMPLE ===")
    for row in fan[:5]:
        print(row)