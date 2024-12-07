
import unittest
import logging

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')


    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner_name = 'test_runner'
            runner = Runner(runner_name, -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.warning(f'"test_runner" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")

    def test_run(self):
        try:
            runner_name = 123
            runner = Runner(runner_name)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")



    def test_challenge(self):
        runner1_name = 'test_runner1'
        runner2_name = 'test_runner2'
        runner1 = Runner(runner1_name)
        runner2 = Runner(runner2_name)
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


first = Runner('Вося', 10)
second = Runner('Илья', 5)
third = Runner('Арсен',  10)

t = Tournament(101, first, second)
print(t.start())

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_test.log", encoding="utf-8", format = "%(asctime)s - %(levelname)s - %(message)s")
    unittest.main()
