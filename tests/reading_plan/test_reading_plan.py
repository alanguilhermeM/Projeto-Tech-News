from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest

@pytest.fixture
def mock(mocker):
    return mocker.patch(
        'tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy'
        )


def test_reading_plan_group_news(mock):
    instance = ReadingPlanService()
    with pytest.raises(ValueError) as result:
        instance.group_news_for_available_time(-2)

    assert str(result.value) == "Valor 'available_time' deve ser maior que zero"

    mock.return_value = [
        {"title": "new", "reading_time": 11},
        {"title": "new2", "reading_time": 5},
    ]

    result = instance.group_news_for_available_time(10)
    expected = {
        "readable": [
            {
                "unfilled_time": 5,
                "chosen_news": [("new2", 5)],
            },
        ],
        "unreadable": [("new", 11)],
    }
    assert result == expected
