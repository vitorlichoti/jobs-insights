from src.pre_built.counter import count_ocurrences


def test_counter() -> int:
    results_python = count_ocurrences('data/jobs.csv', 'Python')
    assert results_python == 1639
    results_javascript = count_ocurrences('data/jobs.csv', 'JavaScript')
    assert results_javascript == 122
