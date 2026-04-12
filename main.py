
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