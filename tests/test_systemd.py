"""تست sd_notify و ضربان نگهبان (مرحلهٔ ۷) — ADR-0003/0012."""

import asyncio
import threading

from top_divar.systemd import heartbeat_loop, sd_notify, watchdog_interval_seconds


def test_sd_notify_without_socket_returns_false(monkeypatch):
    monkeypatch.delenv("NOTIFY_SOCKET", raising=False)
    assert sd_notify("READY=1") is False


def test_sd_notify_sends_datagram_to_unix_socket(monkeypatch, tmp_path):
    import socket

    server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    server_path = tmp_path / "notify.sock"
    server.bind(str(server_path))
    server.settimeout(1.0)
    monkeypatch.setenv("NOTIFY_SOCKET", str(server_path))
    assert sd_notify("READY=1") is True
    data = server.recv(1024)
    assert data == b"READY=1"
    server.close()


def test_sd_notify_abstract_socket(monkeypatch):
    import socket

    server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    server.bind("\0top-divar-test-notify")
    server.settimeout(1.0)
    monkeypatch.setenv("NOTIFY_SOCKET", "@top-divar-test-notify")
    assert sd_notify("WATCHDOG=1") is True
    assert server.recv(1024) == b"WATCHDOG=1"
    server.close()


def test_sd_notify_bad_socket_returns_false(monkeypatch):
    monkeypatch.setenv("NOTIFY_SOCKET", "/nonexistent/dir/notify.sock")
    assert sd_notify("READY=1") is False


def test_watchdog_interval_is_half_of_watchdog_usec(monkeypatch):
    monkeypatch.delenv("WATCHDOG_USEC", raising=False)
    assert watchdog_interval_seconds() is None
    monkeypatch.setenv("WATCHDOG_USEC", "300000000")  # WatchdogSec=300
    assert watchdog_interval_seconds() == 150.0
    monkeypatch.setenv("WATCHDOG_USEC", "1000000")
    assert watchdog_interval_seconds() == 1.0  # کف حداقل
    monkeypatch.setenv("WATCHDOG_USEC", "nonsense")
    assert watchdog_interval_seconds() is None


def test_heartbeat_loop_ticks_independently_until_stop():
    """ضربان نگهبان جدا از صف کاری تیک می‌زند (معیار پایان مرحلهٔ ۷)."""
    beats = []
    stop = threading.Event()
    ticks = 3

    async def _run():
        async def _fake_sleeper(seconds):
            assert seconds == 10.0
            if len(beats) >= ticks:
                stop.set()

        await heartbeat_loop(
            stop,
            interval=10.0,
            notify=lambda message: beats.append(message) or True,
            sleeper=_fake_sleeper,
        )

    asyncio.run(_run())
    assert beats == ["WATCHDOG=1"] * ticks


def test_heartbeat_loop_default_notify_uses_env(monkeypatch):
    import socket

    server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    server.bind("\0top-divar-test-heartbeat")
    server.settimeout(1.0)
    monkeypatch.setenv("NOTIFY_SOCKET", "@top-divar-test-heartbeat")
    stop = threading.Event()

    async def _run():
        async def _fake_sleeper(seconds):
            stop.set()

        await heartbeat_loop(stop, interval=5.0, sleeper=_fake_sleeper)

    asyncio.run(_run())
    assert server.recv(1024) == b"WATCHDOG=1"
    server.close()
