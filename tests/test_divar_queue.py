import asyncio

from top_divar.divar.queue import DivarRequestQueue


class FakeClock:
    def __init__(self):
        self.now = 1000.0

    def __call__(self):
        return self.now

    def advance(self, seconds):
        self.now += seconds


class SleepRecorder:
    def __init__(self, clock):
        self.clock = clock
        self.waits = []

    async def __call__(self, seconds):
        self.waits.append(seconds)
        self.clock.advance(seconds)


def _run(coro):
    return asyncio.run(coro)


class TestSerialQueue:
    def test_first_requests_never_wait(self):
        clock = FakeClock()
        sleeper = SleepRecorder(clock)
        queue = DivarRequestQueue(
            search_min_interval=30.0, detail_min_interval=60.0, clock=clock, sleeper=sleeper
        )
        order = []

        async def main():
            await queue.run_search(lambda: asyncio.sleep(0, result=order.append("search")))
            await queue.run_detail(lambda: asyncio.sleep(0, result=order.append("detail")))

        _run(main())
        assert order == ["search", "detail"]
        assert sleeper.waits == []

    def test_same_kind_spacing_is_enforced(self):
        clock = FakeClock()
        sleeper = SleepRecorder(clock)
        queue = DivarRequestQueue(
            search_min_interval=30.0, detail_min_interval=60.0, clock=clock, sleeper=sleeper
        )

        async def main():
            await queue.run_search(lambda: asyncio.sleep(0))
            clock.advance(10.0)  # فقط ۱۰ ثانیه گذشته
            await queue.run_search(lambda: asyncio.sleep(0))

        _run(main())
        assert sleeper.waits == [20.0]  # ۳۰ − ۱۰

    def test_detail_interval_is_independent(self):
        clock = FakeClock()
        sleeper = SleepRecorder(clock)
        queue = DivarRequestQueue(
            search_min_interval=30.0, detail_min_interval=60.0, clock=clock, sleeper=sleeper
        )

        async def main():
            await queue.run_detail(lambda: asyncio.sleep(0))
            clock.advance(45.0)  # برای search کافی است، برای detail نه
            await queue.run_search(lambda: asyncio.sleep(0))
            await queue.run_detail(lambda: asyncio.sleep(0))

        _run(main())
        # search بدون انتظار؛ detail باید ۱۵ ثانیه صبر کند
        assert sleeper.waits == [15.0]

    def test_serial_execution_no_overlap(self):
        clock = FakeClock()
        sleeper = SleepRecorder(clock)
        queue = DivarRequestQueue(
            search_min_interval=0.0, detail_min_interval=0.0, clock=clock, sleeper=sleeper
        )
        active = []
        max_overlap = 0
        started = []

        async def work(name):
            nonlocal max_overlap
            active.append(name)
            max_overlap = max(max_overlap, len(active))
            started.append(name)
            clock.advance(1.0)
            active.remove(name)

        async def main():
            await asyncio.gather(
                queue.run_search(lambda: work("s")),
                queue.run_detail(lambda: work("d1")),
                queue.run_detail(lambda: work("d2")),
            )

        _run(main())
        assert max_overlap == 1  # هیچ درخواستی هم‌زمان با دیگری نبود
        assert started.index("d1") < started.index("d2")  # صف جزئیات FIFO

    def test_detail_queue_is_fifo(self):
        clock = FakeClock()
        sleeper = SleepRecorder(clock)
        queue = DivarRequestQueue(
            search_min_interval=0.0, detail_min_interval=0.0, clock=clock, sleeper=sleeper
        )
        order = []

        async def work(name):
            order.append(name)

        async def main():
            await asyncio.gather(
                queue.run_detail(lambda: work("a")),
                queue.run_detail(lambda: work("b")),
                queue.run_detail(lambda: work("c")),
            )

        _run(main())
        assert order == ["a", "b", "c"]

    def test_unknown_kind_rejected(self):
        queue = DivarRequestQueue(search_min_interval=1, detail_min_interval=1)

        async def main():
            await queue.execute("bogus", lambda: asyncio.sleep(0))

        try:
            _run(main())
        except ValueError as exc:
            assert "bogus" in str(exc)
        else:
            raise AssertionError("باید ValueError می‌داد")
