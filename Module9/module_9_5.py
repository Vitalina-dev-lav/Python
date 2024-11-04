# ������ "Range - ��� ������":
# �������� ���������������� ����� ���������� StepValueError, ������� ����������� �� ValueError.
# ������������ ����������, ����� �������� ������ ��� ������ ��������� pass.
#
# �������� ����� Iterator, ������� �������� ���������� ����������:
# �������� �������:
# start - ����� ����� � �������� ���������� ��������.
# stop - ����� ����� �� ������� ������������� ��������.
# step - ��� � ������� ����������� ��������.
# pointer - ��������� �� ������� ����� � �������� (���������� start)
# ������:
# __init__(self, start, stop, step=1) - ����������� �������� ������ � ����� ��������,
# � ����� ����. � ���� ������ � ������ ������� ����������� step �� ��������� 0. ���� �����,
# �� ������������� ���������� StepValueError('��� �� ����� ���� ����� 0')
# __iter__ - ����� ������������ �������� pointer �� start � ������������ ��� ������ ���������.
# __next__ - ����� ������������� ������� pointer �� step. � ����������� �� ����� �������� step �������� �����������
# ���� ����� pointer ������ ������ stop, ���� ������ stop. ������ ��� ��� �������� ������.

# ������ ������:
# �������� ����� ���������� StepValueError.
# �������� ����� Iterator � ������� ��� �������� � ������.
# �������� ��������� �������� ������ Iterator � ��������� �������� � ���� ��� ������ ����� for.

class StepValueError(ValueError):
    pass

# �������� ����� Iterator, ������� �������� ���������� ����������:
class Iterator():

# __init__ (self, start, stop, step=1) - ����������� �������� ������ � ����� ��������, � ����� ����.
# � ���� ������ � ������ ������� ����������� step �� ��������� 0.
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('��� �� ����� ���� ����� 0')

        self.stop = stop
        self.step = step
        self.pointer = start

# __iter__ - ����� ������������ �������� pointer �� start � ������������ ��� ������ ���������
    def __iter__(self):
        self.pointer = self.start
        return self
# __next__ - ����� ������������� ������� pointer �� step
    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        current = self.pointer
        self.pointer += self.step
        return current


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print("��� �� ����� ���� ����� 'O'")

# �������� ��������
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

# ����� ����������
for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()