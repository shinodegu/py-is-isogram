from app.main import is_isogram
import pytest

class TestIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            pytest.param(
                "pineapple",
                False,
                id="test with non isogram"
            ),
            pytest.param(
                "mad",
                True,
                id="test with isogram"
            ),
            pytest.param(
                "HuGe",
                True,
                id="test with uppercase"
            ),
            pytest.param(
                " ",
                True,
                id="test with empty str"
            )
        ]
    )
    def test_isogram(
            self,
            word: str,
            result: bool) -> None:
        assert is_isogram(word) == result
