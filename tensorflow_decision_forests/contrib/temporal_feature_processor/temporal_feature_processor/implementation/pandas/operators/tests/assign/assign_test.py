from absl.testing import absltest

from temporal_feature_processor.implementation.pandas.operators.assign import PandasAssignOperator
from temporal_feature_processor.implementation.pandas.operators.tests.assign.test_data import different_index
from temporal_feature_processor.implementation.pandas.operators.tests.assign.test_data import repeated_timestamps
from temporal_feature_processor.implementation.pandas.operators.tests.assign.test_data import with_idx_more_timestamps
from temporal_feature_processor.implementation.pandas.operators.tests.assign.test_data import with_idx_same_timestamps


class AssignOperatorTest(absltest.TestCase):
  base_data_dir = "temporal_feature_processor/tests/operators/assign/data"

  def setUp(self) -> None:
    self.operator = PandasAssignOperator()

  def test_different_index(self) -> None:
    self.assertRaisesRegex(IndexError,
                           "Assign sequences must have the same index names.",
                           self.operator, different_index.INPUT_1,
                           different_index.INPUT_2)

  def test_repeated_timestamps(self) -> None:
    self.assertRaisesRegex(
        ValueError,
        "Cannot have repeated timestamps in assigned EventSequence.",
        self.operator, repeated_timestamps.INPUT_1, repeated_timestamps.INPUT_1)

  def test_with_idx_same_timestamps(self) -> None:
    operator_output = self.operator(with_idx_same_timestamps.INPUT_1,
                                    with_idx_same_timestamps.INPUT_2)
    self.assertEqual(True,
                     with_idx_same_timestamps.OUTPUT.equals(operator_output))

  def test_with_idx_more_timestamps(self) -> None:
    operator_output = self.operator(with_idx_more_timestamps.INPUT_1,
                                    with_idx_more_timestamps.INPUT_2)
    self.assertEqual(True,
                     with_idx_more_timestamps.OUTPUT.equals(operator_output))


if __name__ == "__main__":
  absltest.main()
