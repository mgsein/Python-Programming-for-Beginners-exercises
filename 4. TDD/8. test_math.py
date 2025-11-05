import pytest
from stuff.accum import Accumulator

@pytest.mark.math
def test_one_plus_one():
  assert 1 + 1 == 2

@pytest.mark.math
def test_one_plus_two():
  a = 1
  b = 2
  c = 3
  assert a + b == c

@pytest.mark.math
def test_divide_by_zero():
  with pytest.raises(ZeroDivisionError) as e:
    num = 1 / 0
 
  assert 'division by zero' in str(e.value)

@pytest.fixture
def accum():
  return Accumulator()

@pytest.mark.accumulator
def test_accumulator_init(accum):
  assert accum.count == 0

@pytest.mark.accumulator
def test_accumulator_add_one(accum):
  accum.add()
  assert accum.count == 1

@pytest.mark.accumulator
def test_accumulator_add_three(accum):
  accum.add(3)
  assert accum.count == 3

@pytest.mark.accumulator
def test_accumulator_add_twice(accum):
  accum.add()
  accum.add()
  assert accum.count == 2

@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly(accum):
  with pytest.raises(AttributeError, match=r"object has no setter") as e:
    accum.count = 10

